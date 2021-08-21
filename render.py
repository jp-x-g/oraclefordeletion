# Script to parse downloaded JSON logs of AfD pages, and use XTools to get revision/article information.
# JPxG, 2021 August 11
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
# Set default configuration variables.
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
logfilename = "run4.log"
outfilename = "output.html"
outprefix = "AfD-render-"
jsonprefix = "AfD-log-"
tmpfilename = "tmp.txt"

apiBase = "https://xtools.wmflabs.org/api/page/articleinfo/en.wikipedia.org/"
today = datetime.utcnow().date()
totalQueriesMade = 0


#clearScreen = 0
#if clearScreen:
#	for asdf in range(0,clearScreen):
#		print("\n")
#(All this does is put a bunch of blank lines in the terminal)

########################################
# Parse arguments from command line.
########################################

parser = argparse.ArgumentParser(description="Oracle for Deletion, output renderer (4 of 4). Note that all times and dates used by this program are in UTC, including in the runlog.", epilog="This one runs almost instantaneously, since there are no API queries.")
parser.add_argument("-o", "--output", metavar="blahblah.txt", help="Output file, which will be saved in " + os.getcwd() + dataname + "/" + outputname + "/. Default is \"AfD-render-YYYY-MM-DD-to-YY-MM-DD.txt\".)", default="insanely weird string that nobody would ever type in on purpose.txt")
parser.add_argument("-b", "--back", metavar="DAYS", help="Days to go back. Default is 7.", default=7)
parser.add_argument("-l", "--latest", metavar="DATE", help="Date to parse back from (YYYY-MM-DD). Default is today (UTC).", default=today)
parser.add_argument("-a,", "--aggregate", help="Whether to eliminate the daily headings and just make one huge table for the whole interval.",action="store_true")
#parser.add_argument("-m", "--max", help="Maximum queries to make before stopping. Default is 0 (parse all days in the specified interval).", default=0)
#parser.add_argument("-d", "--dryrun", help="Run the script without actually sending queries to the API.", action="store_true")
parser.add_argument("-v", "--verbose", help="Spam the terminal AND runlog with detailed information. Wheee!", action="store_true")
parser.add_argument("-c", "--configure", help="Set up directories and runlog, then show configuration data and exit.", action="store_true")
#parser.add_argument("-s", "--sleep", metavar="S", help="Time, in seconds, to delay before executing the script. Not very useful. Default is 0.5.", default=0.5)
#parser.add_argument("-s", "--sleep", metavar="SECS", help="Time in seconds to delay between receiving an API response and sending the next request. Default is 0.5.", default=0.5)
args = parser.parse_args()
today = datetime.fromisoformat(str(args.latest))

cooldown = 0

verbose = 0
if args.verbose:
	verbose = 1

forReal = 1
#if args.dryrun:
#	forReal = 0

limitMaxQueries = False
maxQueriesToMake = 69420
#if (args.max != 0):
#	limitMaxQueries = True
#	maxQueriesToMake = args.max

numberOfDays = int(args.back)
sleepTime = 0.01
#sleepTime = float(args.sleep)

daysDelta = timedelta(days=numberOfDays)

aggregate = 0
if args.aggregate:
	aggregate = 1

# Set configuration variables from args.
# This is awkward, but I wrote the script before I wrote the arg parser, lol.

########################################
# Here be file system stuff.
########################################

data = Path(os.getcwd() + "/" + dataname)
# This is the directory where all program-generated data should live.
pages = Path(os.getcwd() + "/" + dataname + "/" + pagesname)
# This is the directory that JSON encodings of AfD log pages will be parsed to.
config = Path(os.getcwd() + "/" + configname)
# Config files live here.
tmp = Path(os.getcwd() + "/" + dataname + "/" + tempname)
tmpfile = Path(os.getcwd() + "/" + dataname + "/" + tempname + "/" + tmpfilename)
# Temporary file directory (doesn't need to persist between runs of the stack)
pagePath = Path(os.getcwd() + "/" + dataname + "/" + tempname + "/page.html")
# Stupid kludge.
configFilePath = Path(os.getcwd() + "/" + configname + "/" + configfilename)
logFilePath = Path(os.getcwd() + "/" + dataname + "/" + logfilename)
out = Path(os.getcwd() + "/" + dataname + "/" + outputname)
outputPath = Path(os.getcwd() + "/" + dataname + "/" + outputname + "/" + outfilename)

########################################
# Make sure those paths exist.
########################################

data.mkdir(mode=0o777, exist_ok = True)
pages.mkdir(mode=0o777, exist_ok = True)
config.mkdir(mode=0o777, exist_ok = True)
tmp.mkdir(mode=0o777, exist_ok = True)
out.mkdir(mode=0o777, exist_ok = True)

########################################
# Function to log to the logfile.
########################################

def aLog(argument):
	try:
		dalogPath = open(str(logFilePath), 'rb')
		dalogContents = dalogPath.read().decode()
		dalogPath.close()
		dalog = open(str(logFilePath), 'w')
		dalog.write(dalogContents + argument)
		dalog.close()
		print(argument)
	except (FileNotFoundError):
		daLog = open(str(logFilePath), 'w')
		daLog.write("\nSetting up runtime log at " + str(datetime.now(timezone.utc)) + "\n" + argument)
		daLog.close()
		print(argument)

########################################
# Function to create a gradient.
########################################

def createGradient(start, end, step):
	# There's probably a library for this, but whatever.
	# - JPxG, 2021 August 17
	st = [int(("0x" + start[1:3]), 16), int(("0x" + start[3:5]), 16), int(("0x" + start[5:7]), 16)]
	ed = [int(("0x" + end[1:3]), 16), int(("0x" + end[3:5]), 16), int(("0x" + end[5:7]), 16)]
	# Convert from hex string to numbers.
	st = [float(st[0]), float(st[1]), float(st[2])]
	ed = [float(ed[0]), float(ed[1]), float(ed[2])]
	# Convert from ints to floats.
	output = []
	#print(st)
	#print(ed)
	diff = [(ed[0] - st[0]), (ed[1] - st[1]), (ed[2] - st[2])]
	#print(diff)
	for stp in range(0, step):
	# Loop that runs over every step in the whole.
	# "stp" is the step we're at in the gradient.
		#print(stp)
		s = "#"
		for v in range(0,3):
		# This will only execute for 0, 1, and 2.
			amountToGoUp = diff[v] / (step - 1)
			# The total difference between the start and end values,
			# divided by how many steps we're putting in the gradient.
			# It's "step - 1" because we want to end at the end value,
			# not one increment before the end value.
			val = int(st[v] + (stp * (diff[v] / (step - 1))))
			# The starting value, plus (current gradient step) many of the increment.
			# It's an int, because you can't do partial hex values.
			if (len(str(hex(val))[2:5]) == 1):
				s = s + "0" + str(hex(val))[2:5]
				# Add a ZERO-PADDED hex number if it's one digit.
			else:
				s = s + str(hex(val))[2:5]
				# Add the hex number if it's normal.
			# Convert the computed value to a hex, then to a string, then append it to
			# the string for that step's hex value.
			s = s.upper()
			# Convert to uppercase. Not a big deal, but whatever.
		output.append(s)
		# Store all three computed hex values as the color for that step.
	return(output)

########################################
# Function to be done with the program.
########################################

def closeOut():
	execTime = (datetime.now(timezone.utc) - startTime).total_seconds()
	aLog("FINISHED AT  : " + str(datetime.now(timezone.utc)))
	aLog("TIME: " + str(round(execTime,3)) + "s")
	try:
		tmphandlePath = open(str(tmpfile), 'rb')
		tmphandleContents = tmphandlePath.read().decode()
		tmphandlePath.close()
		tmphandle = open(str(tmpfile), 'w')
		tmphandle.write(tmphandleContents + str(execTime))
		# For some reason, it writes two line breaks instead of one. No idea what's up with that. The other scripts don't freaking do that.
		tmphandle.close()
	except (FileNotFoundError):
		print("Couldn't log execution time.")
	quit()

########################################
# Set colors.
########################################
""
########## Normal colors.
keepest = "#CCFFDD"
# Color for the highest "keep" ratios. Conventionally pale green.
dellest = "#FFCCDD"
# Color for the highest "delete" ratios. Conventionally pale red.
middest = "#EFEFDD"
# Color for the midpoint of keepest and dellest (the natural midpoint is too murky, and yellow is too yellow).
errorst = "#EAECF0"
# Color for ratios that couldn't be determined (or no !votes have been cast)
defaultcl = "#EAECF0"
# Color for closes that couldn't be determined, or AfDs which are still open.
keepcl = "#CEF2CE"
# Convention is pale green.
delecl = "#F2CECE"
# Convention is pale red.
elsecl = "#F2F2CE"
# Convention is straw.
afdheaderbg = "#F2F2CE"
# Background for AfD column headers.
afdbg = "#FFFFE6"
# Background for AfD columns.
afdnocomments = "#FFFF73"
# Background for AfD comment cells with no comments on them yet.
indGrayed = "#EAECF0"
# Background for table-of-contents cells that are irrelevant.
# Default is the default Wikitable header color, EAECF0.
""

########## Solarize that shizz.
# These are Solarized colors, mixed with #f8f9fa (Wikitable default cell background)
"""
keepest = "#BEC97D"
# Color for the highest "keep" ratios. Conventionally pale green.
dellest = "#EA9594"
# Color for the highest "delete" ratios. Conventionally pale red.
middest = "#D6C17D"
# Color for the midpoint of keepest and dellest (the natural midpoint is too murky, and yellow is too yellow).
midder = createGradient(middest, dellest, 8)[2]
# Color for one step past the midpoint.
errorst = "#B2B5DF"
# Color for ratios that couldn't be determined.
defaultcl = "#D5D7EC"
# Color for closes that couldn't be determined.
keepcl = "#DBE1BB"
# Convention is pale green.
delecl = "#F1C7C7"
# Convention is pale red.
elsecl = "#E7DDBB"
# Convention is straw.
afdheaderbg = "#E597BE"
# Background for AfD column headers.
afdbg = "#EEC8DC"
# Background for AfD columns.
afdnocomments = "#E597BE"
# Background for AfD comment cells with no comments on them yet.
"""

########################################
# Get everybody and their stuff together.
########################################

curTime = datetime.now(timezone.utc)
startTime = curTime
lastTime = curTime
delta = (curTime - lastTime).total_seconds()
# Might use these later, but probably won't.

aLog("Running Oracle for Deletion (renderer), version " + version + ", at " + datetime.now(timezone.utc).isoformat() + " UTC, local time " + datetime.now().isoformat())
aLog("Arguments: " + str(args))

if verbose or args.configure == True:
	aLog("File name  : " + __file__)
	aLog("Base path  : " + os.getcwd() + "/" + __file__)
	aLog("Data path  : " + str(data))
	aLog("Pages path : " + str(pages))
	aLog("Temp path  : " + str(tmp))
	aLog("Config file: " + str(configFilePath))
	aLog("Output dir : " + str(out))
	aLog("Log file   : " + str(logFilePath))
	aLog("Running as : " + os.getlogin())
	aLog("Cooldown   : " + str(sleepTime))
aLog("Running script for " + userRunning + ". Processing " + str(numberOfDays) + " days: " + today.strftime("%Y %B %d") + " back to " + (today - timedelta(days=numberOfDays)).strftime("%Y %B %d") + ".") 

########################################
# Okay -- three, two, one...
########################################

if args.configure == True:
	quit()
	# If we're just showing the config data, we're done with the script. Let's scram.

if numberOfDays > 30:
	word = "boat"
	time.sleep(1)
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
	print("!!!!!  WARNING: This is a " + word + "load of pages.  !!!!!"
		+ "!!!!!     Your output is going to be HUGE     !!!!!")
	time.sleep(5)

########################################
# Let's jam.
########################################

m = "<small><small>"
n = "</small></small>"
# These are used for formatting table headers.


dayLogPath = str(out) + "/" + str(outprefix) + today.strftime("%Y-%m-%d") + "-to-" + (today - timedelta(days=numberOfDays)).strftime("%Y-%m-%d") + ".txt"
# out/outprefix/YYYY-MM-DD-to-YYYY-MM-DD.txt
if (args.output != "insanely weird string that nobody would ever type in on purpose.txt"):
	dayLogPath = str(out) + "/" + args.output
# This will set the path for the output file, either to the default thing, or to whatever input was given.

outputstring = "\nLast updated: " + str(datetime.now(timezone.utc).strftime("%Y-%m-%d, %H:%M (UTC)")) + "\n"
top = ""
# Create blank template for output text of top index.
top = top + "{|class=\"wikitable sortable\""
top = top + "\n|-"
top = top + "\n!'''Contents'''"
top = top + "\n!"+m+"Total"+n
top = top + "\n!"+m+"Open"+n
top = top + "\n!"+m+"Uncom-<br/>mented"+n
top = top + "\n!"+m+"Closed"+n
top = top + "\n!"+m+"(%k)"+n
top = top + "\n!"+m+"(%d)"+n
top = top + "\n!"+m+"(%m)"+n
#print(top)

totind = ["<span style=\"display:none\">!!!999</span>'''TOTAL'''",  0,  0,  0,  0,  0,  0,  0]
# Initialize empty array for total of all days.

o = ""
# Create blank template for output text of main tables.

# grad = createGradient("#CCFFDD", "#FFCCDD", 16)
# 16-step gradient between pale green and pale red.
midder = createGradient(middest, dellest, 52)[2]
grad = createGradient(keepest, middest, 50) + createGradient(midder, dellest, 51)
# 101-step gradient between pale green, pale yellow, and pale red.
# The natural midpoint of the gradient is E6E6DD, which I changed to EFEFDD to be a slight bit yellower.
# I started out with FFFFDD, but this was so yellow it made the midrange of results hard to read.
# The next one is 56% (a sixteenth) along the second gradient, not 50, to avoid double-counting it and making two steps the same color.


for incr in range(0,numberOfDays):
# This will go from 0 (today) to numberOfDays (the furthest we want to go back)
	try:
		theDay = (today - timedelta(days=incr))
		# The day we're going to be dealing with is today minus the increment
		dayDate = theDay.strftime("%Y-%m-%d")
		# The day that the day is, formatted like a normal human being would choose
		dayText = theDay.strftime("%Y_%B_%-d")
		# The url for that day is, formatted like Wikipedia would choose
		# Note that it's %-d and not %d, because the AfD urls don't have zero-padded days
		processingPath = str(pages) + "/" + str(jsonprefix) + dayDate + ".json"
		# Determine which json to open for the day being processed.
		if verbose:
			aLog("Attempting to open logfile at " + processingPath)
		try:
			dayLogFile = open(processingPath, 'r')
			dlData = json.load(dayLogFile)
			dayLogFile.close()
			aLog("Processing " + str(dlData["count"]) + " AfDs from " + processingPath)
		except:
			aLog("!!! FAILED TO OPEN: " + processingPath)
		# Take the existing string, and add a new section header for each new day being processed.
		m = "<small><small>"
		n = "</small></small>"
		# These are used for formatting table headers.
		op = ""
		cl = ""
		if (aggregate == 0):
			o=o+"\n===" + dayDate + "===" 
			op = "\n{| class=\"wikitable sortable collapsible\" style=\"width:100%\"" 
			op = op + "\n|-" 
			op = op + "\n!'''Open AfDs (relists bolded)'''" 
			op = op + "\n!" 
			op = op + "\n!"+m+"Keep<br/>%"+n
			op = op + "\n!"+m+"Page<br/>revs"+n
			op = op + "\n!"+m+"Page<br/>eds."+n
			op = op + "\n!"+m+"Page<br/>size"+n
			op = op + "\n!"+m+"Page<br/>made"+n
			op = op + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>!v #"+n
			op = op + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>eds."+n
			op = op + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>size"+n
			op = op + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>made"+n
			op = op + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>last"+n
			# Initialize string that will be a table of all open AfDs for that day.
			cl = "\n{| class=\"wikitable sortable collapsible collapsed\" style=\"width:100%\"" 
			cl = cl + "\n|-" 
			cl = cl + "\n!'''Closed AfDs (relists bolded)'''" 
			cl = cl + "\n!" 
			cl = cl + "\n!"+m+"Keep<br/>%"+n
			cl = cl + "\n!"+m+"Page<br/>revs"+n
			cl = cl + "\n!"+m+"Page<br/>eds."+n
			cl = cl + "\n!"+m+"Page<br/>size"+n
			cl = cl + "\n!"+m+"Page<br/>made"+n
			cl = cl + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>!v #"+n
			cl = cl + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>eds."+n
			cl = cl + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>size"+n
			cl = cl + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>made"+n
			cl = cl + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>last"+n
			# Initialize string that will be a table of all closed AfDs for that day.
			anchorSetYet = 1
			# We don't want to set anchors at all.
		else:
			anchorSetYet = 0
		#Set this to zero, which means that the renderer will put an anchor in the first entry for the day.
		opCount = 0
		# Initialize count for open AfDs
		clCount = 0
		# Initialize count for closed AfDs
		ind = [dayDate,  0,  0,  0,  0,  0,  0,  0]
		#         0      1   2   3   4   5   6   7
		#               /   /   /     \   \   \   \
		#	      total open uncom closed  %k  %d  %m
		#print(ind)
		#print(dlData["pgs"])
		for page in dlData["pgs"]:
			try:
				# This iterates over every page in that day's AfD.
				#print(page)
				d = dlData["pgs"][page]
				#print(d)
				b = "style=\"background:" + afdbg + "\"|"
				bnocomments = "style=\"background:" + afdnocomments + "\"|"
				# Beginning for AfD data cells
				cellcolor = defaultcl
				sortkey = "!111"
				if (d['afdinfo']['open'] != 1):
					if (d['pageinfo']['error'] != "0"):
						ind[6] = ind[6] + 1
						# Increment the "delete" counter in the day's index row.
						cellcolor = delecl
						sortkey = "!444"
						# Dark red for closed AfDs where the article doesn't exist.
					elif (d['pageinfo']['redirect'] != 0):
						ind[7] = ind[7] + 1
						# Increment the "merge" counter in the day's index row.
						cellcolor = elsecl
						sortkey = "!333"
						# Dark yellow for closed AfDs where the article is a redirect.
					else:
						ind[5] = ind[5] + 1
						# Increment the "keep" counter in the day's index row.
						cellcolor = keepcl
						sortkey = "!222"
						# Dark green (i.e. keep) for closed AfDs.
				try:
					#print("D: " + str(d['afdinfo']['vdl'] + d['afdinfo']['vsd'] + d['afdinfo']['vmg'] + d['afdinfo']['vrd'] + d['afdinfo']['vdr'] + d['afdinfo']['vus']) + " / K: " + str(d['afdinfo']['vkp'] + d['afdinfo']['vsk']) + " / T: " + str(d['afdinfo']['all']))
					if (d['afdinfo']['all'] == 0):
						ratio = "N/A"
						ratiocolor = errorst
					else:
						ratio = (d['afdinfo']['vdl'] + d['afdinfo']['vsd'] + d['afdinfo']['vmg'] + d['afdinfo']['vrd'] + d['afdinfo']['vdr'] + d['afdinfo']['vus']) / d['afdinfo']['all']
						# Delete, speedy delete, merge, redirect, draftify, and userfy !votes, out of all !votes.
						ratio = ratio * 100.0
						# Creates number (from 0 to 100) expressing ratio of how many !votes are delete-like.
						# There's 101 gradient steps, so 0 to 100 will cover them all.
						#print(str(ratio)[0:5])
						ratiocolor = str(grad[int(ratio)])
						ratio = str(100 - ratio)[0:5]
						# Calculate ratio to display (as keep %, truncated decimals)
				except:
					aLog("Couldn't calculate ratio for " + page)
					ratio = "?"
					ratiocolor = errorst
				s = ""
				# Initialize blank string for this row. Rows for open and closed AfDs are the same,
				# which means we can use the same code for both, THEN decide which table to put it in.
				n = "\n|"
				# Newline string (this just makes the code less ugly)
				s=s+ "\n|-"
				s=s+"\n|style=\"background:" + cellcolor + "\" |<span style=\"display:none\">" + sortkey + "</span>"
				if d['afd']['relist'] > 0:
					s=s+"'''"
					# Bold it if it's a relist
				s=s+"[[Wikipedia:Articles for deletion/" + d['afd']['afdtitle'] + "|" + page + "]]"
				if d['afd']['relist'] > 0:
					s=s+"'''"
					# Bold it if it's a relist
				if (anchorSetYet == 0):
					s=s+"{{anchor|" + dayDate + "}}"
					anchorSetYet = 1
					# Add an anchor and disable the sentry variable.
				linkscolumn="\n|<span class=\"plainlinks\">[[" + page + "|a]]·[[Talk:" + page + "|t]]·[{{fullurl:" + page + "|action=history}} h]</span>"
				########################################
				# Fix namespace errors in link string.
				########################################
				# Article links column
				linkscolumn = linkscolumn.replace("·[[Talk:Talk:","·[[Talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Draft:","·[[Draft talk:")
				# Sometimes people nominate weird namespaces at AfD.
				linkscolumn = linkscolumn.replace("·[[Talk:User:","·[[User talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Wikipedia:","·[[Wikipedia talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Template:","·[[Template talk:")
				# Sometimes people nominate REALLY weird namespaces.
				linkscolumn = linkscolumn.replace("·[[Talk:Wikipedia talk:","·[[Wikipedia talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Template talk:","·[[Template talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:File:","·[[File talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:File talk:","·[[File talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:MediaWiki:","·[[MediaWiki talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:MediaWiki talk:","·[[MediaWiki talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Help:","·[[Help talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Help talk:","·[[Help talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Category:","·[[Category talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Category talk:","·[[Category talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Portal:","·[[Portal talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Portal talk:","·[[Portal talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:TimedText:","·[[TimedText talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:TimedText talk:","·[[TimedText talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Module:","·[[Module talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Module talk:","·[[Module talk:")
				# Sometimes it's April Fools' Day.
				linkscolumn = linkscolumn.replace("·[[Talk:Gadget:","·[[Gadget talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Gadget talk:","·[[Gadget talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Gadget definition:","·[[Gadget definition talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Gadget definition talk:","·[[Gadget definition talk:")
				# Some editors just want to watch the world burn.
				linkscolumn = linkscolumn.replace("·[[Talk:Special:","·[[Special talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Special talk:","·[[Special talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Media:","·[[Media talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Media talk:","·[[Media talk:")
				# Virtual namespaces.
				linkscolumn = linkscolumn.replace("·[[Talk:Image:","·[[Image talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Image talk:","·[[Image talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:WP:","·[[Wikipedia talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:WPT:","·[[Wikipedia talk:")
				# Aliases.
				linkscolumn = linkscolumn.replace("·[[Talk:Book:","·[[Book talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Book talk:","·[[Book talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Flow:","·[[Flow talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Flow talk:","·[[Flow talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Education Program:","·[[Education Program talk:")
				linkscolumn = linkscolumn.replace("·[[Talk:Education Program talk:","·[[Education Program talk:")
				# I don't even think this is possible, but why not.
				s=s+linkscolumn
				s=s+"\n|style=\"background:" + ratiocolor + "\"|" + ratio
				# Ratio column
				try: 
					sd = n + str(d['pagestats']['revisions'])
					sd = sd + n + str(d['pagestats']['editors'])
					sd = sd + n + str(d['pageinfo']['size'])
					sd = sd + n + str(d['pagestats']['created_at'])[0:7]
					s = s + sd
					# Add them all to a string and then add that string to s all at once.
					# This may seem pointless, but it prevents table-breaking.
					# If it just adds them to s sequentially, and it fails on column 4,
					# cause it to add a full five dummy columns IN ADDITION to those four.
					# That is to say, the row will be more than five, and the table will break.
				except:
					try:
						sd = n + "−"
						sd = sd + n + "−"
						sd = sd + n + str(d['pageinfo']['size'])
						sd = sd + n + "−"
						s = s + sd
						# Render light version (without XTools queries).
						# This is what will render if detail.py wasn't run.
					except:
						s=s+n+n+n+n
						# If rendering the light version also failed, dummy out the row.
						# This will happen if the page was deleted.
				try:
					if (d['afdinfo']['all'] == 0):
						sd = n + bnocomments + str(d['afdinfo']['all'])
						# Add the background color for an uncommented AfD to the line.
						ind[3] = ind[3] + 1
						# Increment the "uncommented" counter.
					else:
						sd = n + b + str(d['afdinfo']['all'])
						# Add normal background color for commented AfD to the line.
					sd = sd + n + b + str(d['afdstats']['editors'])
					sd = sd + n + b + str(d['afdinfo']['size'])
					sd = sd + n + b + str(d['afdstats']['created_at'])[5:]
					sd = sd + n + b + str(d['afdstats']['modified_at'])[5:]
					s = s + sd
					# See above comment for why this is necessary.
				except:
					try:
						if (d['afdinfo']['all'] == 0):
							sd = n + bnocomments + str(d['afdinfo']['all'])
							# Add the background color for an uncommented AfD to the line.
							ind[3] = ind[3]
							# Don't increment the "uncommented" counter, because we just did it.
						else:
							sd = n + b + str(d['afdinfo']['all'])
							# Add normal background color for commented AfD to the line.
						sd = sd + n + b + "−"
						sd = sd + n + b + str(d['afdinfo']['size'])
						sd = sd + n + b + "−"
						sd = sd + n + b + "−"
						s = s + sd
						# Render the light version of the AfD row (omitting XTools info).
						# This is what will render if detail.py wasn't run.
					except:
						aLog("Failed to render AfD for" + d['afd']['afdtitle'])
						s=s+n+b+n+b+n+b+n+b+n+b
						# 
				if (d['afdinfo']['open'] != 1):
					clCount = clCount + 1
					cl = cl + s 
					#If the AfD is closed, increment the count and add it to the closed-AfD table string.
				else:
					opCount = opCount + 1
					op = op + s
					#If the AfD is open, increment the count and add it to the open-AfD table string.
			except:
				# If there is some bizarre mystery bug that makes no sense.
				try:
					aLog("Couldn't process " + page)
					o = o + "<!-- Couldn't process a page: " + page + "-->"
					#o = o + "<!-- Couldn't process a page: " + str(dlData["pgs"][page])
				except:
					aLog("Couldn't process a page, and couldn't even figure out what it was.")
					o = o + "<!-- Couldn't process a page, and trying to tell what page it was failed. -->"

		totind[1] = totind[1] + int(opCount + clCount) 
		totind[2] = totind[2] + int(opCount)
		totind[3] = totind[3] + int(ind[3])
		totind[4] = totind[4] + int(clCount)
		totind[5] = totind[5] + int(ind[5])
		totind[6] = totind[6] + int(ind[6])
		totind[7] = totind[7] + int(ind[7])
		# Add all quantities to the "total" row in the index table

		#    ind[  0      1   2   3   4   5   6   7 ]
		#        date    /   /   /     \   \   \   \
		#	        total open uncom closed  %k  %d %m

		ind[0] = dayDate
		ind[1] = int(opCount + clCount)
		ind[2] = int(opCount)
		ind[3] = int(ind[3])
		ind[4] = int(clCount)
		if(clCount != 0):
			# If there are any freaking closes at all.
			ind[5] = str(float(100*(ind[5] / clCount)))[0:5]
			ind[6] = str(float(100*(ind[6] / clCount)))[0:5]
			ind[7] = str(float(100*(ind[7] / clCount)))[0:5]
		else:
			# Avoid the classic meme "I JUST DIVIDED BY ZERO OH SHI-"
			ind[5] = "style=\"background: " + indGrayed + "\" | 0"
			ind[6] = "style=\"background: " + indGrayed + "\" | 0"
			ind[7] = "style=\"background: " + indGrayed + "\" | 0"
		# Calculate stuff for the index. Many things stay the same. 
		top = top + "\n|-"
		top = top + "\n| " + "[[#" + str(ind[0]) + "|" + str(ind[0]) + "]]"
		if (ind[1] == 0):
			top = top + "\n| style=\"background:" + indGrayed + "\" | 0"
		else:
			top = top + "\n| " + str(ind[1])
		top = top + "\n| " + str(ind[2])
		top = top + "\n| " + str(ind[3])
		if (ind[4] == 0):
			top = top + "\n| style=\"background:" + indGrayed + "\" | 0"
		else:
			top = top + "\n| " + str(ind[4])
		top = top + "\n| " + str(ind[5])
		top = top + "\n| " + str(ind[6])
		top = top + "\n| " + str(ind[7])
		# Add all the stuff to the index table for the top.
		if (aggregate == 0):
			o = o + "\n====Open AfDs, " + dayDate +  " (" + str(opCount) + ")====" + op + "\n|}\n====Closed AfDs, " + dayDate + " (" + str(clCount) + ")====\n" + cl + "\n|}"
		else:
			o = o + op + cl
		#print(o)
		##########
		# End of codeblock that runs over every day's AfD log in the batch.
		##########
	except (KeyboardInterrupt):
		aLog("ABORTING EXECUTION: KeyboardInterrupt")
		quit()
##### All days have now been processed, time to start compositing the output page.

sort = "<span style=\"display:none\">!!!999</span>"
top = top + "\n|-"
top = top + "\n| " + sort + str(totind[0])
top = top + "\n| " + sort + str(totind[1])
top = top + "\n| " + sort + str(totind[2])
top = top + "\n| " + sort + str(totind[3])
top = top + "\n| " + sort + str(totind[4])
if (totind[4] != 0):
	# If there are any freaking closes at all.
	top = top + "\n| " + sort + str(float(100*(totind[5] / totind[4])))[0:5]
	top = top + "\n| " + sort + str(float(100*(totind[6] / totind[4])))[0:5]
	top = top + "\n| " + sort + str(float(100*(totind[7] / totind[4])))[0:5]
else:
	# Avoid the classic meme "I JUST DIVIDED BY ZERO OH SHI-"
	top = top + "\n| " + sort + "0"
	top = top + "\n| " + sort + "0"
	top = top + "\n| " + sort + "0"
top = top + "\n|}\n"
# Composite table-of-contents index table with "total" row.
if (aggregate == 1):
	top = "<onlyinclude>" + top + "\n</onlyinclude>"
	top = top + "\n{| class=\"wikitable sortable collapsible\" style=\"width:100%\"" 
	top = top + "\n|-" 
	top = top + "\n!'''AfDs (relists bolded)'''" 
	top = top + "\n!" 
	top = top + "\n!"+m+"Keep<br/>%"
	top = top + "\n!"+m+"Page<br/>revs"
	top = top + "\n!"+m+"Page<br/>eds."
	top = top + "\n!"+m+"Page<br/>size"
	top = top + "\n!"+m+"Page<br/>made"
	top = top + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>!v #"
	top = top + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>eds."
	top = top + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>size"
	top = top + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>made"
	top = top + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>last"
	# Create start, and headers, for big aggregate column.
	o = o + "\n|}"
	# Terminate output string for AfD table.
outputstring = outputstring + "__NOTOC__\n" + top + o
# Composite output string from beginning section, top index table, and day tables.
try:
	dayLogFile = open(dayLogPath, 'w')
	dayLogFile.write(outputstring)
	dayLogFile.close()
	aLog("Successfully saved: " + dayLogPath)
	aLog("Total length: " + str(len(outputstring)))
except:
	aLog("!!! FAILED TO SAVE: " + dayLogPath)
closeOut()
# Log how long it took.