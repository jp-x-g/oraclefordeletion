# Script to parse downloaded JSON logs of AfD pages, and use XTools to get revision/article information.
# JPxG, 2021 August 14
# Haven't written any software in a long time. This will be extremely painful. For me.

import sys
import traceback
import os
import time
# This is used so that happy programs can sleep warmly. Snooze snooze!
from pathlib import Path
# For filesystem interactions. Read read! Write write!
import requests
# For scraping webpages. Scrape scrape!
from html.parser import HTMLParser
# Required to use BeautifulSoup. Parse parse!
from bs4 import BeautifulSoup
# The real meat and potatoes of the HTML parsing. Slurp slurp!
# Documentation for this is recommended reading to get how the program works.
from datetime import datetime
from datetime import timedelta
from datetime import timezone
# Required to use time. Tick tock!
import json
# Required to parse json. Parse parse!
import argparse
# Required to parse arguments. Parse parse...!!

########################################
# Set all configuration variables.
########################################
version = "0.2"
userRunning = "JPxG"

# File system stuff below.
dataname = "data"
pagesname = "pages"
configname = "cfg"
tempname = "tmp"
configfilename = "config.txt"
logfilename = "run3.log"
outfilename = "output.html"
jsonprefix = "AfD-log-"
tmpfilename = "tmp.txt"

apiBase = "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvslots=*&rvprop=content&formatversion=2&format=json&titles="
today = datetime.utcnow().date()

########################################
# Parse arguments from command line.
########################################

parser = argparse.ArgumentParser(description="Oracle for Deletion, page info detailer (3 of 4). This will get wikitext from the en.wiki API, and use it to populate the JSON files of AfD log pages with information for both the articles (pageinfo) and and their deletion discussions (afdinfo). Feature counts (like refs, sections, and !votes) are approximate, and will miss some things. Note that all dates used by this program are in UTC, including timestamps in the runlog.", epilog="This one runs very quickly, since the en.wiki API allows batched queries.")
parser.add_argument("-b", "--back", metavar="DAYS", help="Days to go back. Default is 7.", default=7)
parser.add_argument("-l", "--latest", metavar="YYYY-MM-DD", help="Date to parse back from. Default is today (UTC).", default=today)
parser.add_argument("-s", "--sleep", metavar="S", help="Time, in seconds, to delay between receiving an API response and sending the next request. Default is 0.5.", default=0.5)
parser.add_argument("-q", "--querysize", metavar="N", help="Number of pairs to batch in each query. Default (and maximum allowed by the API) is 25.", default=25)
parser.add_argument("-m", "--max", help="Maximum queries to make before stopping. Default is 0 (parse all entries in the specified interval). Setting this will probably cut off execution in the middle of a logpage, so it's pretty stupid to do this unless you know what you're doing, or you're testing the script.", default=0)
parser.add_argument("-d", "--dryrun", help="Run the script without actually sending queries to the API. This may break stuff.", action="store_true")
parser.add_argument("-v", "--verbose", help="Spam the terminal AND runlog with insanely detailed information. Wheee!", action="store_true")
parser.add_argument("-c", "--configure", help="Set up directories and runlog, then show configuration data and exit.", action="store_true")
parser.add_argument("-x", "--explain", help="Display specific, detailed information about what this program does (including a full list of the fields it gets from the API), then exit.", action="store_true")

args = parser.parse_args()
today = datetime.fromisoformat(str(args.latest))

if args.explain:
	print("This is the third in a series of scripts.")
	print(" For happiness to bloom,")
	print("  all must work together.")
	print("   Without this one,")
	print("    the others cannot work,")
	print("     and without the others,")
	print("      this one cannot work.")
	print("       Such is life.")
	print("The specific task of this script is to populate the .JSONs of the previous script with detailed information scanned from the pages' wikitext, obtained from the en.wiki API. After this script is run, the renderer can generate a page.")
	print("This uses the \"revisions\" API endpoint, in its default mode, which supplies a single revision (the latest) of each page specified. The API's maximum batch size is 50; since each article is paired with an AfD page, the maximum batch size for this program is 25.")
	print("")
	print(" Page info | NOTE: Feature counts (refs, templates, etc) will probably not be precise")
	print("-----------+-------------------------------------------------------------------------")
	print("scrapetime | string | ISO timestamp of when the data is received by this program")
	print("error      | string | should be \"0\" unless the page is messed up")
	print("redirect   | number | 1 if \"#redirect [[\" is found, 0 otherwise")
	print("size       | number | number of characters in page wikitext (ignores transclusions)")
	print("lines      | number | newline characters found")
	print("refs       | number | \"</ref>\"s found")
	print("sections   | number | \"\\n==\"s found")
	print("templates  | number | \"{{\"s found")
	print("files      | number | \"[[File:\"s and \"[[Image:\"s found")
	print("cats       | number | \"[[Category:\"s found")
	print("links      | number | \"[[\"s found (minus categories and files)")
	print("")
	print(" AfD info  | NOTE: Detection is imperfect, and will fail to capture some !votes")
	print("-----------+-------------------------------------------------------------------------")
	print("scrapetime | string | ISO timestamp of when the data is received by this program")
	print("error      | string | should be \"0\" unless the page is messed up")
	print("size       | number | number of characters in page wikitext (ignores transclusions)")
	print("lines      | number | newline characters found")
	print("delsorts   | number | deletion sorting lines (\"<small class=\"delsort-notice\">\") found")
	print("open       | number | 1, but 0 if \"<div class=\"boilerplate afd vfd xfd-closed\"\" found")
	print("vkp        | number | number of parseable \"keep\"s")
	print("vdl        | number | number of parseable \"delete\"s")
	print("vsk        | number | number of parseable \"speedy keep\"s")
	print("vsd        | number | number of parseable \"speedy delete\"s")
	print("vmg        | number | number of parseable \"merge\"s")
	print("vrd        | number | number of parseable \"redirect\"s")
	print("vtw        | number | number of parseable \"transwiki\"s")
	print("vus        | number | number of parseable \"userfy\"s")
	print("vdr        | number | number of parseable \"draftify\"s")
	print("all        | number | sum of counts for all !vote types above")
	quit()

verbose = 0
if args.verbose:
	verbose = 1


queryBatchSize = 25
# This is half of the actual query batch size,
# since we're sending one query for the page and one for the AfD page.
# The API limits us to a batch size of 50, which means 25 is the limit.
if args.querysize:
	queryBatchSize = int(args.querysize)

forReal = 1
if args.dryrun:
	forReal = 0

limitMaxQueries = False
maxQueriesToMake = 69420
if (args.max != 0):
	limitMaxQueries = True
	maxQueriesToMake = args.max

numberOfDays = int(args.back)
sleepTime = float(args.sleep)

totalQueriesMade = 0

# Set configuration variables from args.
# This is awkward, but I wrote the script before I wrote the arg parser, lol.

########################################
# Here be file system stuff.
########################################

# This is the directory where all program-generated data should live.
data = Path(os.getcwd() + "/" + dataname)
# This is the directory that JSON encodings of AfD log pages will be parsed to.
pages = Path(os.getcwd() + "/" + dataname + "/" + pagesname)
# Config files live here.
config = Path(os.getcwd() + "/" + configname)
# Temporary file directory (doesn't need to persist between sessions)
tmp = Path(os.getcwd() + "/" + dataname + "/" + tempname)
tmpfile = Path(os.getcwd() + "/" + dataname + "/" + tempname + "/" + tmpfilename)
pagePath = Path(os.getcwd() + "/" + dataname + "/" + tempname + "/page.html")
configFilePath = Path(os.getcwd() + "/" + configname + "/" + configfilename)
logFilePath = Path(os.getcwd() + "/" + dataname + "/" + logfilename)
outputPath = Path(os.getcwd() + "/" + dataname + "/" + outfilename)

########################################
# Make sure those paths exist.
########################################

data.mkdir(mode=0o777, exist_ok = True)
pages.mkdir(mode=0o777, exist_ok = True)
config.mkdir(mode=0o777, exist_ok = True)
tmp.mkdir(mode=0o777, exist_ok = True)

########################################
# Function to log to the logfile.
########################################

def aLog(argument):
	try:
		dalogPath = open(str(logFilePath), 'rb')
		dalogContents = dalogPath.read().decode()
		dalogPath.close()
		dalog = open(str(logFilePath), 'w')
		dalog.write(dalogContents + "\n" + argument)
		dalog.close()
		print(argument)
	except (FileNotFoundError):
		daLog = open(str(logFilePath), 'w')
		daLog.write("\nSetting up runtime log at " + str(datetime.now(timezone.utc)) + "\n" + argument)
		daLog.close()
		print(argument)

########################################
# Function to be done with the program.
########################################

def closeOut():
	execTime = (datetime.now(timezone.utc) - startTime).total_seconds()
	aLog("FINISHED AT  : " + str(datetime.now(timezone.utc)))
	aLog("DAYS: " + str(numberOfDays) + " / TIME: " + str(round(execTime,3)) + " / QUERIES: " + str(totalQueriesMade))
	#aLog() + "s / " + str(round((execTime / totalQueriesMade),3)) + "s per query")
	try:
		tmphandlePath = open(str(tmpfile), 'rb')
		tmphandleContents = tmphandlePath.read().decode()
		profile = json.load(tmphandleContents)
		tmphandlePath.close()
		# Try to read from temp file.
		for param in ['main1', 'main2', 'detail1', 'detail2']:
			try:
				profile[param]
			except:
				profile[param] = 0.01
			# Zero out previous parameters, if not already set.
		profile['detailp1'] = execTime
		profile['detailp2'] = totalQueriesMade
		# Set params for this script.
		tmphandle = open(str(tmpfile), 'w')
		tmphandle.write(json.dumps(profile, indent=2, ensure_ascii=False))
		tmphandle.close()
		# Write out file.
	except (FileNotFoundError):
		print("Couldn't log execution time.")
		try:	
			profile = {
			'main1'    : 0.01,
			'main2'    : 0.01,
			'detail1'  : 0.01,
			'detail2'  : 0.01,
			'detailp1' : execTime,
			'detailp2' : totalQueriesMade
			}
			# Set zeroed params.
			tmphandle = open(str(tmpfile), 'w')
			tmphandle.write(json.dumps(profile, indent=2, ensure_ascii=False))
			tmphandle.close()
			# Write file.
		except:
			print("Couldn't save a fresh log either.")
			# Well, to hell with it.
	quit()

########################################
# Get everybody and their stuff together.
########################################

curTime = datetime.now(timezone.utc)
startTime = curTime
lastTime = curTime
delta = (curTime - lastTime).total_seconds()
# Might use these later, but probably won't.

aLog("Running Oracle for Deletion (mass propertizer), version " + version + ", at " + datetime.now(timezone.utc).isoformat() + " UTC, local time " + datetime.now().isoformat())
aLog("Arguments: " + str(args))

if verbose:
	aLog("File name  : " + __file__)
	aLog("Base path  : " + os.getcwd() + "/" + __file__)
	aLog("Data path  : " + str(data))
	aLog("Pages path : " + str(pages))
	aLog("Temp path  : " + str(tmp))
	aLog("Config file: " + str(configFilePath))
	aLog("Output file: " + str(outputPath))
	aLog("Log file   : " + str(logFilePath))
	aLog("Running as : " + os.getlogin())
	aLog("Cooldown   : " + str(sleepTime))
print("Running script for " + userRunning + ". Processing " + str(numberOfDays) + " days: " + today.strftime("%Y %B %d") + " back to " + (today - timedelta(days=numberOfDays)).strftime("%Y %B %d") + ".") 
if args.configure == True:
	quit()
	# If we're just showing the config data, we're done with the script. Let's scram.

########################################
# Okay -- three, two, one...
########################################


if numberOfDays > 30:
	word = "boat"
	if numberOfDays > 60:
		word = "crap"
	if numberOfDays > 120:
		word = "shit"
	if numberOfDays > 360:
		word = "fuck"
	if ((today - timedelta(days=numberOfDays)).year) < 2001:
		print("DANGER: Wikipedia doesn't go back that far, buddy!")
		aLog("ABORTING EXECUTION: invalid start date (" + (today - timedelta(days=numberOfDays)).isoformat() +")")
		quit()
	if ((today - timedelta(days=numberOfDays)).year) < 2006:
		print("CAUTION: AfDs back then were formatted differently.")
		print("This probably isn't going to work the way you want.")
	print("!!!!!  WARNING: This is a " + word + "load of pages.  !!!!!\n"
		+ "!!!!! I sure hope you know what you're doing. !!!!!")
	if numberOfDays > 60:
		time.sleep(5)


########################################
# Let's jam.
########################################

# initialize afdDay, which we'll be using to store all the day for the data.
afdDay = {}
# this will go from 0 (today) to numberOfDays (the furthest we want to go back)
for incr in range(0,numberOfDays):
	try:
		# the day we're going to be dealing with is today minus the increment:
		theDay = (today - timedelta(days=incr))
		# the day that the day is, formatted like a normal human being would choose
		dayDate = theDay.strftime("%Y-%m-%d")
		# the url for that day is, formatted like Wikipedia would choose:
		# note that it's %-d and not %d, because the AfD urls don't have zero-padded days
		dayText = theDay.strftime("%Y_%B_%-d")
		dayLogPath = str(pages) + "/" + str(jsonprefix) + dayDate + ".json"
		if verbose:
			aLog("Attempting to open logfile at " + dayLogPath)
		try:
			dayLogFile = open(dayLogPath, 'r')
			dlData = json.load(dayLogFile)
			dayLogFile.close()
			if verbose:
				aLog("Processing " + str(dlData["count"]) + " AfDs from " + dayLogPath)
		except:
			aLog("!!! FAILED TO OPEN: " + dayLogPath)
		# Generic XTools API URL:
		# https://xtools.wmflabs.org/api/page/articleinfo/en.wikipedia.org/Albert_Einstein
		# Tested this on "Slavoj Žižek" and it seems like it Just Works(R) with Unicode and spaces.
		#print(dlData["pgs"])
		cursor = 0
		# Progress through the whole list of pages.
		querylength = 0
		# How many pages have been added to current query.
		query = ""
		#print(dlData["pgs"])
		for page in dlData["pgs"]:
			try:
				# This iterates over every page in that day's AfD.
				#print(str(cursor) + " / " + str(page))
				key = dlData["pgs"][page]
				#print(key)
				if ((forReal) and (page != "")):
					querylength = querylength + 1
					cursor = cursor + 1
					# This will actually hit the XTools API.
					urls = [apiBase + page, apiBase + "Wikipedia:Articles for deletion/" + key["afd"]["afdtitle"]]
					query = query + page + "|" + "Wikipedia:Articles for deletion/" + key["afd"]["afdtitle"] + "|"
					# Add another argument for the article and also for its AfD.
					#Increment the pagecount so we can know what's going on.
					#print(query)
					if (querylength >= queryBatchSize) or (cursor >= len(dlData["pgs"])):
						query = query[:-1]
						# Trim that damn "|" from the end of the string.
						# query = query.replace("%", "%25")
						# # "Percent sign" needs to be encoded first, or it will mess up later ones, lol.
						# Commented out 2021-08-18, it is causing weird stuff to happen.
						query = query.replace("&", "%26")
						query = query.replace("?", "%3F")
						# Percent-encode stuff that will mess up the query/processing.
						#query = query.replace(",", "%2C")
						#query = query.replace('"', '%22')
						#query = query.replace("'", "%27")
						#query = query.replace("+", "%2B")
						# Stuff that might mess it up, but commented out to avoid chaos.
						query = apiBase + query
						# Prepend API base URL to send it out.
						if verbose:
							print("Requesting " + str(querylength) + " pages, query #" + str(totalQueriesMade + 1))
						#print(query)
						# Reset query and query length for next run.
						if forReal:
							# print("Doing it for real.")
							time.sleep(sleepTime)
							r = requests.get(query, allow_redirects=False)
							# Actually hit the URL in this line, and get a page, which will be of type "Response"
							totalQueriesMade = totalQueriesMade + 1
							# Increment "total queries made"
							r = r.text
							# Make it so that "r" is the text of the response, not a "Response" of the response
							r = json.loads(r)
							for rp in r['query']['pages']:
								ptitle = rp['title']
								#ptitle = ptitle.replace(",", "%2C")
								#Percent-encode commas, in hope of finding a bug.
								if (rp['title'].find('Wikipedia:Articles for deletion/') != -1):
									#print("AfD found: " + ptitle)
									ptitle = ptitle[32:]
									for ordinal in ["2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th"]:
										# Couldn't find any article with more than 17 nominations, so not including these.
										# , "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th"]:
										# print("Checking for " + ordinal + ": " + ordinal[0:len(ordinal) - 2])
										if (ptitle.find(" (" + ordinal + " nomination)") != -1):
											ptitle = ptitle[0:ptitle.find(" (" + ordinal + " nomination)")]
												# Trim the "(2nd nomination)" crap.
										# This whole block just trims out the nomination parts.
									ordsText = ["zeroth", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth"]
									# Yes, people actually did this sometimes.
									for ordinal in range(0,21):
										# There are 21 items in the list, so we want 0 to 20 as indices.
										# , "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th"]:
										# print("Checking for " + ordinal + ": " + ordinal[0:len(ordinal) - 2])
										if (ptitle.find(" (" + ordsText[ordinal] + " nomination)") != -1):
											# Trim the ordinal, i.e. "2nd" -> "2".
											#print("FOUND A WEIRD NOMINATION ORDINAL!!!!!!!!!!!!")
											#print(theSlice)
											#print(str(ordinal))
											ptitle = ptitle[0:ptitle.find(" (" + ordsText[ordinal] + " nomination)")]
									try:
										if "missing" in rp.keys():
											#print("AFD'S A LION GET IN THE CAR")
											dlData["pgs"][ptitle]['afdinfo'] = {
											"scrapetime": datetime.now(timezone.utc).isoformat(),
											"error": "missing"
											}
										else:
											#print(rp)
											ptext = rp['revisions'][0]['slots']['main']['content']
											ptextl = ptext.lower()
											isopen = 1
											if (ptext.find("<div class=\"") != -1) and (ptext.find("xfd-closed\"") != -1):
												isopen = 0
											delsorts = ptext.count("<small class=\"delsort-notice\">")
											sigs = ptext.count("[[User")
											lines = ptext.count("\n")
											vkp = ptextl.count("keep'''") + ptextl.count("oppose'''") + ptextl.count("keep all'''")
											vdl = ptextl.count("delete'''") + ptextl.count("delete all'''") 
											vsk = ptextl.count("speedy keep'''")
											vsd = ptextl.count("speedy delete'''")
											vkp = vkp - vsk
											vdl = vdl - vsd
											# Don't doublecount speedy keeps/deletes
											vmg = ptextl.count("merge'''") + ptextl.count("merge all'''")
											vrd = ptextl.count("redirect'''") + ptextl.count("redirect all'''")
											vtw = ptextl.count("transwiki'''")
											vus = ptextl.count("userfy'''")
											vdr = ptextl.count("draftify'''")
											vmv = ptextl.count("move'''") + ptextl.count("rename'''") 
											vall = vkp + vdl + vsk + vsd + vmg + vrd + vtw + vus + vdr
											#print("Delsorts: " + str(delsorts) + " Sigs: " + str(sigs)) 
											dlData["pgs"][ptitle]['afdinfo'] = {
											"scrapetime": datetime.now(timezone.utc).isoformat(),
											"error": "0",
											"size": len(ptext),
											"lines": lines,
											"delsorts": delsorts,
											"open": isopen,
											"vkp": vkp,
											"vdl": vdl,
											"vsk": vsk,
											"vsd": vsd,
											"vmg": vmg,
											"vrd": vrd,
											"vtw": vtw,
											"vus": vus,
											"vdr": vdr,
											"vmv": vmv,
											"all": vall
											}
											# print(dlData["pgs"][ptitle])
											# This whole block above handles AfDs in the response.
									except:
										aLog("!!!!!!!!!! Serious error in storing pageinfo for: " + ptitle)
								else:
									try:
										if "missing" in rp.keys():
											#print("IT'S A LION GET IN THE CAR")
											#if verbose:
											#	print(str(rp.keys()) + " / " + ptitle)
											dlData["pgs"][ptitle]['pageinfo'] = {
											"scrapetime": datetime.now(timezone.utc).isoformat(),
											"error": "missing"
											}
										else:
											ptext = rp['revisions'][0]['slots']['main']['content']
											ptextl = ptext.lower()
											lines = ptext.count("\n")
											redirect = ptextl.count("#redirect [[")
											refs = ptextl.count("</ref>")
											sections = ptextl.count("\n==")
											templates = ptextl.count("{{")
											files = ptextl.count("[[file:") + ptextl.count("[[image:")
											cats = ptextl.count("[[category:")
											links = ptextl.count("[[") - (files + cats)
											dlData["pgs"][ptitle]['pageinfo'] = {
											"scrapetime": datetime.now(timezone.utc).isoformat(),
											"error": "0",
											"redirect": redirect,
											"size": len(ptext),
											"lines": lines,
											"refs": refs,
											"sections": sections,
											"templates": templates,
											"files": files,
											"cats": cats,
											"links": links
											}
									except:
											#cursor = cursor + 1
											aLog("!!!!!!!!!! Serious error in storing pageinfo for: " + ptitle)
									#print("Article found: " + ptitle)

									# This whole block above handles articles in the response.

								#print("Title: " + ptitle + " / page title: " + rp['title'])
						query = ""
						querylength = 0
						# Reset the query and the counter variable for the next batch.
			except (KeyboardInterrupt):
				aLog("ABORTING EXECUTION: KeyboardInterrupt")
				quit()
			#except Exception as err:
				#aLog("!!!!!!!!!! FAILED TO PROCESS !!!!!!!!!!" + str(err))
		if verbose:
			aLog("Attempting to save parsed log to " + dayLogPath)
		try:
			dayLogFile = open(dayLogPath, 'w')
			dayLogFile.write(json.dumps(dlData, indent=2, ensure_ascii=	False))
			dayLogFile.close()
			aLog("Successfully saved: " + dayLogPath)
		except:
			aLog("!!! FAILED TO SAVE: " + dayLogPath)
		##########
		# End of codeblock that runs over every day's AfD log in the batch.
		##########
	except (KeyboardInterrupt):
		aLog("ABORTING EXECUTION: KeyboardInterrupt")
		quit()
closeOut()
# Log how long it took.
