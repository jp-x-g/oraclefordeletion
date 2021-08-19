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
version = "0.1"
userRunning = "JPxG"

apiBase = "https://xtools.wmflabs.org/api/page/articleinfo/en.wikipedia.org/"
today = datetime.utcnow().date()
totalQueriesMade = 0

# File system stuff below.
dataname = "data"
pagesname = "pages"
configname = "cfg"
tempname = "tmp"
outputname = "output"
configfilename = "config.txt"
logfilename = "run5.log"
outfilename = "output.html"
outprefix = "AfD-render-"
jsonprefix = "AfD-log-"
logindeets = "login.txt"
tmpfilename = "tmp.txt"

# Page names below.
inputPage = "render.txt"
pagename = "User:JPxG/sandbox66"
apiBase = "https://en.wikipedia.org/w/api.php"

dividerStart = "<!-- Everything below"
# This is what the bot will interpret as the last line of header text on the page.

divider = "<!-- Everything below here will be replaced by the bot when the page is next updated. Do not edit or remove this HTML note. -->"
# All this does is put a bunch of blank lines in the terminal.
#clearScreen = 0
#if clearScreen:
#	for asdf in range(0,clearScreen):
#		print("\n")

########################################
# Parse arguments from command line.
########################################

parser = argparse.ArgumentParser(description="Oracle for Deletion, uploader.", epilog="Wow!")
#parser.add_argument("-b", "--back", metavar="DAYS", help="Days to go back. Default is 7.", default=7)
#parser.add_argument("-l", "--latest", metavar="YYYY-MM-DD", help="Date to parse back from. Default is today (UTC).", default=today)
parser.add_argument("-n", "--note", metavar="TEXT", help="Comment to add to edit summary.", default="Updating with")
parser.add_argument("-i", "--input", metavar="blahblah.txt", help="Input file to read, out of " + os.getcwd() + "/" + dataname + "/" + outputname + "/. Default is " + inputPage + ".", default=inputPage)
parser.add_argument("-o", "--output", metavar="User:JohnDoe/OfD", help="Wikipedia page to post the file to. Default is " + pagename + ". Be careful with this one, because it is easy to do something stupid.", default=pagename)
parser.add_argument("-u", "--username", metavar="JohnDoe@OfD_poster", help="Specify username to authenticate with. Default is to read from " + os.getcwd() + "/" + configname + "/" + logindeets + ".", default = "Didn't specify one.")
parser.add_argument("-p", "--password", metavar="hunter2", help="Specify password to authenticate with. Default is to read from " + os.getcwd() + "/" + configname + "/" + logindeets + ".", default = "Didn't specify one.")
#parser.add_argument("-s", "--sleep", metavar="S", help="Time, in seconds, to delay before executing the script. Not very useful. Default is 0.5.", default=0.5)
#parser.add_argument("-m", "--max", help="Maximum queries to make before stopping. Default is 0 (parse all entries in the specified interval). Setting this will probably cut off execution in the middle of a logpage, so it's pretty stupid to do this unless you know what you're doing, or you're testing the script.", default=0)
parser.add_argument("-d", "--dryrun", help="Run the script without actually editing the page.", action="store_true")
parser.add_argument("-v", "--verbose", help="Spam the terminal AND runlog with insanely detailed information. Wheee!", action="store_true")
parser.add_argument("-c", "--configure", help="Set up directories and runlog, then show configuration data and exit.", action="store_true")
parser.add_argument("-x", "--explain", help="Display specific, detailed information about what this program does (including a full list of the fields it gets from the API), then exit.", action="store_true")

args = parser.parse_args()
#today = datetime.fromisoformat(str(args.latest))

if args.explain:
	print("This is the fifth in a series of scripts.")
	print(" For happiness to bloom,")
	print("  all must work together.")
	print("   Without this one,")
	print("    the others cannot work,")
	print("     and without the others,")
	print("      this one cannot work.")
	print("       Such is life.")
	quit()

verbose = 0
if args.verbose:
	verbose = 1

forReal = 1
if args.dryrun:
	forReal = 0

#limitMaxQueries = False
#maxQueriesToMake = 69420
#if (args.max != 0):
#	limitMaxQueries = True
#	maxQueriesToMake = args.max

#numberOfDays = int(args.back)
sleepTime = 0.01
#sleepTime = float(args.sleep)

if args.output:
	pagename = args.output

if args.input:
	inputPage = args.input

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
loginPath = Path(os.getcwd() + "/" + configname + "/" + logindeets)
inputPath = Path(os.getcwd() + "/" + dataname + "/" + outputname + "/" + inputPage)

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
	aLog("FINISHED AT  : " + str(datetime.now(timezone.utc)) + " / TIME: " + str(round(execTime,3)))
	quit()

########################################
# Get everybody and their stuff together.
########################################

curTime = datetime.now(timezone.utc)
startTime = curTime
lastTime = curTime
delta = (curTime - lastTime).total_seconds()
# Might use these later, but probably won't.

aLog("Running Oracle for Deletion (uploader), version " + version + ", at " + datetime.now(timezone.utc).isoformat() + " UTC, local time " + datetime.now().isoformat())
aLog("Arguments: " + str(args))

if verbose:
	aLog("File name  : " + __file__)
	aLog("Base path  : " + os.getcwd() + "/" + __file__)
	aLog("Data path  : " + str(data))
	aLog("Pages path : " + str(pages))
	aLog("Temp path  : " + str(tmp))
	aLog("Config file: " + str(configFilePath))
	aLog("Auth file  : " + str(loginPath))
	aLog("Input file : " + str(inputPath))
	aLog("Log file   : " + str(logFilePath))
	aLog("Running as : " + os.getlogin())
	aLog("Cooldown   : " + str(sleepTime))
aLog("Running script for " + userRunning)
#".\nProcessing " + str(numberOfDays) + " days: " + today.strftime("%Y %B %d") + " back to " + (today - timedelta(days=numberOfDays)).strftime("%Y %B %d") + ".")

if args.configure == True:
	quit()
	# If we're just showing the config data, we're done with the script. Let's scram.

########################################
# Let's jam.
########################################

if (args.username == "Didn't specify one." or args.password == "Didn't specify one."):
	try:
		openLogin = open(str(loginPath), 'rb')
		loginContents = openLogin.read().decode()
		openLogin.close()
		# Open the auth file, read it into memory, and close it.	
	except:
		print("!!! FATAL ERROR: Could not read login details. !!!")
		quit()
	authName = loginContents[0:loginContents.find("\n")]
	authPass = loginContents[loginContents.find("\n") + 1:]
else:
	authName = args.username
	authPass = args.password

# Set the auth name and auth password from the auth file, if they weren't specified by the user.

inputFile = open(str(inputPath), 'rb')
payload = inputFile.read().decode()
inputFile.close()
# Get the payload out of the input file.


if verbose:
	aLog("Auth details retrieved (username: " + authName + "). Retrieving token.")
tokenUrl = apiBase + "?action=query&meta=tokens&format=json&type=login"
editTokenUrl = apiBase + "?action=query&meta=tokens&format=json"
s = requests.Session()
# The token and login attempt must be part of the same session, or else it'll time out.

t = s.get(tokenUrl)
########## This line actually hits the API.
token = json.loads(t.text)['query']['tokens']['logintoken']
# Stores the result as "token"
if verbose:
	aLog("Token retrieved. Attempting login.")
l = s.post(apiBase, data={
	"action": "login",
	"lgname": authName,
	"lgpassword": authPass,
	"lgtoken": token,
	"format": "json"})
########## This line actually hits the API.
l = l.text
l = json.loads(l)
if ((l['login']['result']) != "Success"):
	aLog("!!! Login failed: " + l)
	quit()
aLog("Login successful. Authenticated as " + l['login']['lgusername'])




#############################################
#	Grabbing the previous rev of the page
#	and slicing it at the divider so that
#   we can retain some sort of header.
#############################################
"""r = requests.get(apiBase, data={
	"action": "query",
	"prop": "revisions",
	"rvslots": "*",
	"rvprop": "content",
	"formatversion": "2",
	"format": "json",
	"titles": pagename
	})"""
	# Don't know why the heck this doesn't work.
try:
	r = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvslots=*&rvprop=content&formatversion=2&format=json&titles=" + pagename)
	# Actually hit the URL in this line, and get a page, which will be of type "Response"
	r = r.text
	#print(r)
	# Make it so that "r" is the text of the response, not a "Response" of the response
	r = json.loads(r)
	# Make it so that "r" is the parsed JSON of "r", not text
	r = r['query']['pages'][0]['revisions'][0]['slots']['main']['content']
	# The MediaWiki API is so freakin' normal and cool. I love json!!!!!!!
	startZone = 0
	if (r.find(dividerStart) != -1):
		startZone = r.find(dividerStart)
	r = r[0:startZone]
	#print(r)
except:
	r = divider

t = s.get(editTokenUrl)
########## This line actually hits the API for an edit token.
token = json.loads(t.text)['query']['tokens']['csrftoken']

########## This stuff below is going to parse the profiling data from the temp file.
try:
	tmphandlePath = open(str(tmpfile), 'rb')
	tmptxt = tmphandlePath.read().decode()
	tmphandlePath.close()
	execTime = (datetime.now(timezone.utc) - startTime).total_seconds()
	tmplist = tmptxt.split("\n")
	#print(tmplist)
	totalTime =	float(tmplist[0]) + float(tmplist[2]) + float(tmplist[4]) + float(tmplist[6]) + execTime 
	totalQueries = float(tmplist[1]) + float(tmplist[3]) + float(tmplist[5]) + float(4)
	profile = "\n----\n<center>''Completed in " + str(round(totalTime,3)) + "s (" + str(int(totalQueries)) + " queries, " + str(round((totalTime / totalQueries),5)) + "s per query) · Oracle for Deletion v" + version + " · [[User:JPxG|JPxG]] 2021''</center>"
	profile = profile + "\n<!-- Detailed profiling information:"
	profile = profile + "\n main       : " + str(tmplist[0])
	profile = profile + "\n  > queries : " + str(tmplist[1])
	profile = profile + "\n  > per     : " + str(float(tmplist[0])/float(tmplist[1]))
	profile = profile + "\n detail     : " + str(tmplist[2])
	profile = profile + "\n  > queries : " + str(tmplist[3])
	profile = profile + "\n  > per     : " + str(float(tmplist[2])/float(tmplist[3]))
	profile = profile + "\n detailpages: " + str(tmplist[4])
	profile = profile + "\n  > queries : " + str(tmplist[5])
	profile = profile + "\n  > per     : " + str(float(tmplist[4])/float(tmplist[5]))
	profile = profile + "\n render     : " + str(tmplist[6])
	profile = profile + "\n upload     : " + str(execTime)
	profile = profile + "\n-->"
	tmphandle = open(str(tmpfile), 'w')
	tmphandle.write("")
	tmphandle.close()
except:
	print("Couldn't retrieve execution time.")
	profile = "\n----\n<center>''Completed in some amount of time · Oracle for Deletion v" + version + " · [[User:JPxG|JPxG]] 2021''</center>"
#print(profile)

if forReal == 1:
	edit = s.post(apiBase, data={
		"action": "edit",
		"token": token,
		"title": pagename,
		"text": r + "\n" + payload + profile,
		"summary": args.note + " [Oracle for Deletion, version " + version + " :^)]",
		"format": "json"
		})
	edit = edit.text
	#print(edit)
	edit = json.loads(edit)
	print(edit)
else:
	print("Here's what I was going to send:")
	data = {
		"action": "edit",
		"token": token,
		"title": pagename,
		"text": r + "\n" + payload + profile,
		"summary": args.note + " [Oracle for Deletion, version " + version + " :^)]",
		"format": "json"
		}
	print(data)

closeOut()