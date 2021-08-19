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
version = "0.1"
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
apiBase = "https://xtools.wmflabs.org/api/page/articleinfo/en.wikipedia.org/"
today = datetime.utcnow().date()
totalQueriesMade = 0
dividerStart = "<!-- Everything below"
# This is what the bot will interpret as the last line of header text on the page.

divider = "<!-- Everything below here will be replaced by the bot when the page is next updated. Do not edit or remove this HTML note. -->"
# This is what the bot will use to prefix the content it puts into the page.


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
# Temporary file directory (doesn't need to persist between sessions)
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
# Color for ratios that couldn't be determined.
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

#FFFFDD
#E0E0CE
dayLogPath = str(out) + "/" + str(outprefix) + today.strftime("%Y-%m-%d") + "-to-" + (today - timedelta(days=numberOfDays)).strftime("%Y-%m-%d") + ".txt"
# out/outprefix/YYYY-MM-DD-to-YYYY-MM-DD.txt
if (args.output != "insanely weird string that nobody would ever type in on purpose.txt"):
	dayLogPath = str(out) + "/" + args.output
# This will set the path for the output file, either to the default thing, or to whatever input was given.


outputstring = divider + "\n Last updated: " + str(datetime.now(timezone.utc).strftime("%Y-%m-%d")) + "\n"
top = ""
o = ""
# Create blank template for output text.

# grad = createGradient("#CCFFDD", "#FFCCDD", 16)
# 16-step gradient between pale green and pale red.
midder = createGradient(middest, dellest, 8)[2]
grad = createGradient(keepest, middest, 8) + createGradient(midder, dellest, 8)
# 32-step gradient between pale green, pale yellow, and pale red.
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
		o=o+"\n===" + dayDate + "===" 
		# Take the existing string, and add a new section header for each new day being processed.

		op = "\n{| class=\"wikitable sortable\n" + "|-\n" + "! '''Open AfDs'''\n" + "! \n" + "! Page<br/>revs\n" + "! Page<br/>eds.\n" + "! Page<br/>size\n" + "! Page<br/>made\n" + "!! style=\"background:" + afdheaderbg + "\" | AfD<br/>cmts.\n" + "!! style=\"background:" + afdheaderbg + "\" | AfD<br/>eds.\n" + "!! style=\"background:" + afdheaderbg + "\" | AfD<br/>size\n" + "!! style=\"background:" + afdheaderbg + "\" | AfD<br/>made\n" + "!! style=\"background:" + afdheaderbg + "\" | AfD<br/>last\n"
		# Initialize string that will be a table of all open AfDs for that day.
		cl = "\n{| class=\"wikitable sortable\n" + "|-\n" + "! '''Closed AfDs'''\n" + "! \n" + "! Page<br/>revs\n" + "! Page<br/>eds.\n" + "! Page<br/>size\n" + "! Page<br/>made\n" + "!! style=\"background:" + afdheaderbg + "\" | AfD<br/>cmts.\n" + "!! style=\"background:" + afdheaderbg + "\" | AfD<br/>eds.\n" + "!! style=\"background:" + afdheaderbg + "\" | AfD<br/>size\n" + "!! style=\"background:" + afdheaderbg + "\" | AfD<br/>made\n" + "!! style=\"background:" + afdheaderbg + "\" | AfD<br/>last\n"
		# Initialize string that will be a table of all closed AfDs for that day.
		opCount = 0
		# Initialize count for open AfDs
		clCount = 0
		# Initialize count for closed AfDs

		#print(dlData["pgs"])
		for page in dlData["pgs"]:
			try:
				# This iterates over every page in that day's AfD.
				#print(page)
				d = dlData["pgs"][page]
				#print(d)
				b = "style=\"background:" + afdbg + "\" | "
				bnocomments = "style=\"background:" + afdnocomments + "\" | "
				# Beginning for AfD data cells
				cellcolor = defaultcl
				sortkey = "111"
				if (d['afdinfo']['open'] != 1):
					cellcolor = keepcl
					sortkey = "222"
					# Default to dark green (i.e. keep) for closed AfDs.
					if (d['pageinfo']['error'] != "0"):
						cellcolor = delecl
						sortkey = "444"
						# Dark red for closed AfDs where the article doesn't exist.
					elif (d['pageinfo']['redirect'] != 0):
						cellcolor = elsecl
						sortkey = "333"
						# Dark yellow for closed AfDs where the article is a redirect.
				try:
					#print("D: " + str(d['afdinfo']['vdl'] + d['afdinfo']['vsd'] + d['afdinfo']['vmg'] + d['afdinfo']['vrd'] + d['afdinfo']['vdr'] + d['afdinfo']['vus']) + " / K: " + str(d['afdinfo']['vkp'] + d['afdinfo']['vsk']) + " / T: " + str(d['afdinfo']['all']))
					ratio = (d['afdinfo']['vdl'] + d['afdinfo']['vsd'] + d['afdinfo']['vmg'] + d['afdinfo']['vrd'] + d['afdinfo']['vdr'] + d['afdinfo']['vus']) / d['afdinfo']['all']
					# Delete, speedy delete, merge, redirect, draftify, and userfy !votes, out of all !votes.
					ratio = ratio * 15.0
					#There's 16 steps, so 0 to 15 will cover them all.
					#print(str(ratio)[0:5])
					ratiocolor = str(grad[int(ratio)])
					# Creates number (from 0 to 16) expressing ratio of how many !votes are delete-like.
				except:
					aLog("Couldn't calculate ratio for " + page)
					ratiocolor = errorst
				s = ""
				# Initialize blank string for this row. Rows for open and closed AfDs are the same,
				# which means we can use the same code for both, THEN decide which table to put it in.
				n = "\n| "
				s=s+ "\n|-"
				s=s+"\n| style=\"background:" + cellcolor + "\" | <span style=\"display:none\">" + sortkey + "</span>"
				if d['afd']['relist'] > 0:
					s=s+"'''"
				s=s+"[[Wikipedia:Articles for deletion/" + d['afd']['afdtitle'] + "|" + page + "]]"
				if d['afd']['relist'] > 0:
					s=s+"'''"
				s=s+"\n| style=\"background:" + grad[int(ratio)] + "\" | <span style=\"display:none\">" + str(ratio)[0:5] + "</span><span class=\"plainlinks nourlexpansion lx\">[[" + page + "|a]]·[[Talk:" + page + "|t]]·[{{fullurl:" + page + "|action=history}} h]</span>"
				try: 
					sd = n + str(d['pagestats']['revisions'])
					sd = sd + n + str(d['pagestats']['editors'])
					sd = sd + n + str(d['pageinfo']['size'])
					sd = sd + n + str(d['pagestats']['created_at'])[0:7]
					s = s + sd
					# Add them all to a string and then add that string to s all at once.
					# This may seem pointless, but it prevents table-breaking.
					# If it just adds them to s sequentially, this "try" failing will
					# cause it to add a full five dummy columns, even if it's already written some.
					# That is to say, it will add more than five, and the table will break.
				except:
					s=s+n+n+n+n
				try:
					if (d['afdinfo']['all'] == 0):
						sd = n + bnocomments + str(d['afdinfo']['all'])
					else:
						sd = n + b + str(d['afdinfo']['all'])
					sd = sd + n + b + str(d['afdstats']['editors'])
					sd = sd + n + b + str(d['afdinfo']['size'])
					sd = sd + n + b + str(d['afdstats']['created_at'])[5:]
					sd = sd + n + b + str(d['afdstats']['modified_at'])[5:]
					s = s + sd
					# See above comment for why this is necessary.
				except:
					print("Oopsie woopsie! Failed to render for " + d['afd']['afdtitle'])
					s=s+n+b+n+b+n+b+n+b+n+b
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
					aLog("Couldn't process " + str(dlData["pgs"][page]))
					o = o + "<!-- Couldn't process a page -->"
					#o = o + "<!-- Couldn't process a page: " + str(dlData["pgs"][page])
				except:
					aLog("Couldn't process a page, and couldn't even figure out what it was.")
					o = o + "<!-- Couldn't process a page, and trying to tell what page it was failed. -->"

		o = o + "\n====Open AfDs, " + dayDate +  " (" + str(opCount) + ")====" + op + "\n|}" + "\n{{collapse top|Closed AfDs for " + dayDate + " (" + str(clCount) + ")}}\n====Closed AfDs, " + dayDate + " (" + str(clCount) + ")====\n" + cl + "\n|}\n{{collapse bottom}}"
		#print(o)
		##########
		# End of codeblock that runs over every day's AfD log in the batch.
		##########
	except (KeyboardInterrupt):
		aLog("ABORTING EXECUTION: KeyboardInterrupt")
		quit()
outputstring = outputstring + top + o
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