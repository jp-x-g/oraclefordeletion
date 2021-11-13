# Script to parse downloaded JSON logs of AfD pages, and use XTools to get revision/article information.
# JPxG, 2021 August 10
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
outputname = "output"
configfilename = "config.txt"
logfilename = "run2.log"
outfilename = "output.html"
outprefix = "AfD-render-"
jsonprefix = "AfD-log-"
tmpfilename = "tmp.txt"

apiBase = "https://xtools.wmflabs.org/api/page/articleinfo/en.wikipedia.org/"
today = datetime.utcnow().date()
totalQueriesMade = 0

########################################
# Parse arguments from command line.
########################################

parser = argparse.ArgumentParser(description="Oracle for Deletion, page stats detailer (2 of 4). This will take the JSON files of AfD log pages and use XTools to populate it with statistics (like number of revisions, creation date, et cetera) for both the articles (pagestats) and and their deletion discussions (afdstats). Note that all dates used by this program are in UTC, including timestamps in the runlog.", epilog="Be aware that this one takes forever to run, as XTools doesn't allow batched requests: typical times on JPxG's computer have taken between 0.5 and 1.3 seconds per query. Since AfD log pages can have up to a hundred nominations, and each nomination is two queries, you're going to be here for a while.")
parser.add_argument("-b", "--back", metavar="DAYS", help="Days to go back. Default is 7.", default=7)
parser.add_argument("-l", "--latest", metavar="YYYY-MM-DD", help="Date to parse back from. Default is today (UTC).", default=today)
parser.add_argument("-s", "--sleep", metavar="S", help="Time, in seconds, to delay between receiving an API response and sending the next request. Default is 0.5.", default=0.5)
parser.add_argument("-m", "--max", help="Maximum queries to make before stopping. Default is 0 (parse all entries in the specified interval). Setting this will probably cut off execution in the middle of a logpage, so it's pretty stupid to do this unless you know what you're doing, or you're testing the script.", default=0)
parser.add_argument("-d", "--dryrun", help="Run the script without actually sending queries to the API. This may break stuff.", action="store_true")
parser.add_argument("-v", "--verbose", help="Spam the terminal AND runlog with insanely detailed information. Wheee!", action="store_true")
parser.add_argument("-c", "--configure", help="Set up directories and runlog, then show configuration data and exit.", action="store_true")
parser.add_argument("-x", "--explain", help="Display specific, detailed information about what this program does (including a full list of the fields it gets from the API), then exit.", action="store_true")

args = parser.parse_args()
today = datetime.fromisoformat(str(args.latest))

if args.explain:
	print("This is the second in a series of scripts.")
	print(" For happiness to bloom,")
	print("  all must work together.")
	print("   Without this one,")
	print("    the others cannot work,")
	print("     and without the others,")
	print("      this one cannot work.")
	print("       Such is life.")
	print("The specific task of this script is to populate the JSON skeletons of the previous script with actual information about the pages in question, obtained with XTools. After this script, and the other one that handles the actual page content, the renderer can generate a page.")
	print("These fields are retrieved for both the article at AfD and the AfD nomination page itself.")
	print("scrapetime           | timestamp | when the data is retrieved (i.e. in a few seconds)")
	print("error                |           | should be \"0\" unless the page is messed up")
	print("watchers             | number    | number of people with the page watchlisted")
	print("pageviews            | number    | number of pageviews in the last [offset] days")
	print("pageviews_offset     | number    | how many days pageviews are given for: should be 30")
	print("revisions            | number    | total number of revisions for the page")
	print("editors              | number    | total number of distinct editors")
	print("minor_edits          | number    | number of edits tagged \"minor\"")
	print("author               | string    | creator of page's username")
	print("author_editcount     | number    | creator's edit count")
	print("created_at           | timestamp | YYYY-MM-DD")
	print("created_rev_id       | number    | revision id for first revision")
	print("modified_at          | timestamp | YYYY-MM-DD HH:MM")
	print("secs_since_last_edit | number    | this should be pretty obvious, pal")
	print("last_edit_id         | number    | revision id for last edit")
	print("assessment           | string    | \"C\", \"Stub\", \"???\", et cetera.")
	quit()

verbose = 0
if args.verbose:
	verbose = 1

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
	aLog("DAYS: " + str(numberOfDays) + " / ENTRIES: " + str(totalQueriesMade / 2.0) + " / QUERIES: " + str(totalQueriesMade))
	aLog("TIME: " + str(round(execTime,3)) + "s / " + str(round((execTime / totalQueriesMade),3)) + "s per query")
	try:
		tmphandlePath = open(str(tmpfile), 'r')
		profile = json.load(tmphandlePath)
		tmphandlePath.close()
		# Try to read from temp file.
		for param in ['main1', 'main2']:
			try:
				profile[param]
			except:
				profile[param] = 0.01
			# Zero out previous parameters, if not already set.
		profile['detail1'] = execTime
		profile['detail2'] = totalQueriesMade
		# Set params for this script.
		tmphandle = open(str(tmpfile), 'w')
		tmphandle.write(json.dumps(profile, indent=2, ensure_ascii=False))
		tmphandle.close()
		# Close file.
	except (FileNotFoundError):
		print("Couldn't log execution time.")
		try:	
			profile = {
			'main1'    : 0.01,
			'main2'    : 0.01,
			'detail1'  : execTime,
			'detail2'  : totalQueriesMade
			}
			# Set zeroed params.
			tmphandle = open(str(tmpfile), 'w')
			tmphandle.write(json.dumps(profile, indent=2, ensure_ascii=False))
			tmphandle.close()
			# Write out file.
		except:
			print("Couldn't save a fresh log either.")
	quit()

########################################
# Get everybody and their stuff together.
########################################

curTime = datetime.now(timezone.utc)
startTime = curTime
lastTime = curTime
delta = (curTime - lastTime).total_seconds()
# Might use these later, but probably won't.

aLog("Running Oracle for Deletion (mass analyzer), version " + version + ", at " + datetime.now(timezone.utc).isoformat() + " UTC, local time " + datetime.now().isoformat())
aLog("Arguments: " + str(args))

if verbose:
	aLog("File name  : " + __file__)
	aLog("Base path  : " + os.getcwd() + "/" + __file__)
	aLog("Data path  : " + str(data))
	aLog("Pages path : " + str(pages))
	aLog("Temp path  : " + str(tmp))
	aLog("Config file: " + str(configFilePath))
	aLog("Log file   : " + str(logFilePath))
	aLog("Running as : " + os.getlogin())
	aLog("Cooldown   : " + str(sleepTime))
aLog("Running script for " + userRunning + ".\nProcessing " + str(numberOfDays) + " days: " + today.strftime("%Y %B %d") + " back to " + (today - timedelta(days=numberOfDays)).strftime("%Y %B %d") + ".")

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
			aLog("Processing " + str(dlData["count"]) + " AfDs from " + dayLogPath)
		except:
			aLog("!!! FAILED TO OPEN: " + dayLogPath)
		# Generic XTools API URL:
		# https://xtools.wmflabs.org/api/page/articleinfo/en.wikipedia.org/Albert_Einstein
		# Tested this on "Slavoj Žižek" and it seems like it Just Works(R) with Unicode and spaces.
		#print(dlData["pgs"])
		pageQueriesMade = 0
		for page in dlData["pgs"]:
			try:
				#Increment the pagecount so we can know what's going on.
				# This iterates over every page in that day's AfD.
				#print(page)
				key = dlData["pgs"][page]
				#print(key)
				if ((forReal) and (page != "")):
					# This will actually hit the XTools API.
					if verbose:
						aLog("Attempting to contact API for " + page)
					urls = [apiBase + page.replace("&","%26").replace("?","%3F"), apiBase + "Wikipedia:Articles for deletion/" + key["afd"]["afdtitle"].replace("&","%26").replace("?","%3F")]
					# This makes an array for the two API URLs we're gonna 	hit.
					# We need to percent-encode the ampersand and question mark so it doesn't make XTools sad :(
					for incre in [0, 1]:
						if ((limitMaxQueries == True) and (totalQueriesMade > maxQueriesToMake)):
							print("!!! Test is over, go home.")
							closeOut()
						# We want to get page info and AfD info.
						# These are mostly the same thing.
						# So can just run the same code twice with small changes.
						storeIn = ["pagestats", "afdstats"][incre]
						time.sleep(sleepTime)
						# Okay, now we are ready to hit the API.
						r = requests.get(urls[incre])
						# Actually hit the URL in this line, and get a page, which will be of type "Response"
						r = r.text
						# Make it so that "r" is the text of the response, not a "Response" of the response
						r = json.loads(r)
						# Make it so that "r" is the parsed JSON of "r", not text
						if "error" in r.keys():
							pageQueriesMade = pageQueriesMade + 1
							totalQueriesMade = totalQueriesMade + 1
							toStore = {
							"scrapetime": datetime.now(timezone.utc).isoformat(),
							"error": r["error"]}
							dlData["pgs"][page][storeIn] = toStore
						else:
							#print(r)
							pageQueriesMade = pageQueriesMade + 1
							totalQueriesMade = totalQueriesMade + 1
							toStore = {
							"scrapetime": datetime.now(timezone.utc).isoformat(),
							"error": "0",
							"watchers": r["watchers"], 
							"pageviews": r["pageviews"], 
							"pageviews_offset": r["pageviews_offset"], 
							"revisions": r["revisions"], 
							"editors": r["editors"], 
							"minor_edits": r["minor_edits"], 
							"author": r["author"], 
							"author_editcount": r["author_editcount"], 
							"created_at": r["created_at"], 
							"created_rev_id": r["created_rev_id"], 
							"modified_at": r["modified_at"], 
							"secs_since_last_edit": r["secs_since_last_edit"], 
							"last_edit_id": r["last_edit_id"], 
							"assessment": r["assessment"]["value"]}
							dlData["pgs"][page][storeIn] = toStore
							if verbose:
								print(storeIn + " retrieved (" + str(totalQueriesMade) + ")")
						#print(page)
						##########
						# End of codeblock that runs twice for each page (page 	and Afd)
						##########
				aLog(str(totalQueriesMade) + " (entry " + str(int(pageQueriesMade / 2)) + " of " + str(dlData["count"]) + ", on page " + str(incr+1) + " of " + str(numberOfDays) + "): " + page + " completed")
				##########
				# End of codeblock that runs over every page in the day's AfD log.
				##########
			except (KeyboardInterrupt):
				aLog("ABORTING EXECUTION: KeyboardInterrupt")
				quit()
			except:
				aLog("!!!!!!!!!! FAILED TO PROCESS !!!!!!!!!!")
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