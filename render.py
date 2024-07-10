# Script to parse downloaded JSON logs of AfD pages, and use XTools to get revision/article information.
# JPxG, 2021 August 11
# Haven't written any software in a long time. This will be extremely painful. For me.

# Required to parse json. Parse parse!
import argparse

# Required to use time. Tick tock!
import json
import os

# For scraping webpages. Scrape scrape!from datetime import datetime
from datetime import datetime, timedelta, timezone

# This is used so that happy programs can sleep warmly. Snooze snooze!
from pathlib import Path

# For filesystem interactions. Read read! Write write!


# Required to parse arguments. Parse parse...!!

########################################
# Set default configuration variables.
########################################
version = "2.0"
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
summaryfilename = "summary.txt"

apiBase = "https://xtools.wmflabs.org/api/page/articleinfo/en.wikipedia.org/"
today = datetime.utcnow().date()
totalQueriesMade = 0


# clearScreen = 0
# if clearScreen:
# 	for asdf in range(0,clearScreen):
# 		print("\n")
# (All this does is put a bunch of blank lines in the terminal)

########################################
# Parse arguments from command line.
########################################

parser = argparse.ArgumentParser(
    description="Oracle for Deletion, output renderer (4 of 5). Note that all times and dates used by this program are in UTC, including in the runlog.",
    epilog="This one runs almost instantaneously, since there are no API queries.",
)
parser.add_argument(
    "-o",
    "--output",
    metavar="blahblah.txt",
    help="Output file, which will be saved in "
    + os.getcwd()
    + dataname
    + "/"
    + outputname
    + '/. Default is "AfD-render-YYYY-MM-DD-to-YY-MM-DD.txt".)',
    default="insanely weird string that nobody would ever type in on purpose.txt",
)
parser.add_argument(
    "-b", "--back", metavar="DAYS", help="Days to go back. Default is 7.", default=7
)
parser.add_argument(
    "-l",
    "--latest",
    metavar="DATE",
    help="Date to parse back from (YYYY-MM-DD). Default is today (UTC).",
    default=today,
)
parser.add_argument(
    "-a,",
    "--aggregate",
    help="Whether to eliminate the daily headings and just make one huge table for the whole interval.",
    action="store_true",
)
# parser.add_argument("-m", "--max", help="Maximum queries to make before stopping. Default is 0 (parse all days in the specified interval).", default=0)
# parser.add_argument("-d", "--dryrun", help="Run the script without actually sending queries to the API.", action="store_true")
parser.add_argument(
    "-v",
    "--verbose",
    help="Spam the terminal AND runlog with detailed information. Wheee!",
    action="store_true",
)
parser.add_argument(
    "-c",
    "--configure",
    help="Set up directories and runlog, then show configuration data and exit.",
    action="store_true",
)
# parser.add_argument("-s", "--sleep", metavar="S", help="Time, in seconds, to delay before executing the script. Not very useful. Default is 0.5.", default=0.5)
# parser.add_argument("-s", "--sleep", metavar="SECS", help="Time in seconds to delay between receiving an API response and sending the next request. Default is 0.5.", default=0.5)
args = parser.parse_args()
# today = datetime.fromisoformat(str(args.latest))
# Commenting out in lieu of Python 3.5 compatible line below.
today = datetime.strptime(str(args.latest), "%Y-%m-%d")


cooldown = 0

verbose = 0
if args.verbose:
    verbose = 1

forReal = 1
# if args.dryrun:
# 	forReal = 0

limitMaxQueries = False
maxQueriesToMake = 69420
# if (args.max != 0):
# 	limitMaxQueries = True
# 	maxQueriesToMake = args.max

numberOfDays = int(args.back)
sleepTime = 0.01
# sleepTime = float(args.sleep)

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
jsonPath = Path(os.getcwd() + "/" + configname + "/delsort.json")
emojisPath = Path(os.getcwd() + "/" + configname + "/emojis.json")
summaryPath = Path(
    os.getcwd() + "/" + dataname + "/" + tempname + "/" + summaryfilename
)

########################################
# Make sure those paths exist.
########################################

data.mkdir(mode=0o777, exist_ok=True)
pages.mkdir(mode=0o777, exist_ok=True)
config.mkdir(mode=0o777, exist_ok=True)
tmp.mkdir(mode=0o777, exist_ok=True)
out.mkdir(mode=0o777, exist_ok=True)

########################################
# Function to log to the logfile.
########################################


def aLog(argument):
    try:
        dalogPath = open(str(logFilePath), "rb")
        dalogContents = dalogPath.read().decode()
        dalogPath.close()
        dalog = open(str(logFilePath), "w")
        dalog.write("\n" + dalogContents + argument)
        dalog.close()
        print(argument)
    except (FileNotFoundError):
        daLog = open(str(logFilePath), "w")
        daLog.write(
            "\nSetting up runtime log at "
            + str(datetime.now(timezone.utc))
            + "\n"
            + argument
        )
        daLog.close()
        print(argument)


########################################
# Function to create a gradient.
########################################

# This can just all be done in CSS.
# JPxG, 2024 July 9

# def createGradient(start, end, step):
#     # There's probably a library for this, but whatever.
#     # - JPxG, 2021 August 17
#     st = [
#         int(("0x" + start[1:3]), 16),
#         int(("0x" + start[3:5]), 16),
#         int(("0x" + start[5:7]), 16),
#     ]
#     ed = [
#         int(("0x" + end[1:3]), 16),
#         int(("0x" + end[3:5]), 16),
#         int(("0x" + end[5:7]), 16),
#     ]
#     # Convert from hex string to numbers.
#     st = [float(st[0]), float(st[1]), float(st[2])]
#     ed = [float(ed[0]), float(ed[1]), float(ed[2])]
#     # Convert from ints to floats.
#     output = []
#     # print(st)
#     # print(ed)
#     diff = [(ed[0] - st[0]), (ed[1] - st[1]), (ed[2] - st[2])]
#     # print(diff)
#     for stp in range(0, step):
#         # Loop that runs over every step in the whole.
#         # "stp" is the step we're at in the gradient.
#         # print(stp)
#         s = "#"
#         for v in range(0, 3):
#             # This will only execute for 0, 1, and 2.
#             amountToGoUp = diff[v] / (step - 1)
#             # The total difference between the start and end values,
#             # divided by how many steps we're putting in the gradient.
#             # It's "step - 1" because we want to end at the end value,
#             # not one increment before the end value.
#             val = int(st[v] + (stp * (diff[v] / (step - 1))))
#             # The starting value, plus (current gradient step) many of the increment.
#             # It's an int, because you can't do partial hex values.
#             if len(str(hex(val))[2:5]) == 1:
#                 s = s + "0" + str(hex(val))[2:5]
#                 # Add a ZERO-PADDED hex number if it's one digit.
#             else:
#                 s = s + str(hex(val))[2:5]
#                 # Add the hex number if it's normal.
#             # Convert the computed value to a hex, then to a string, then append it to
#             # the string for that step's hex value.
#             s = s.upper()
#             # Convert to uppercase. Not a big deal, but whatever.
#         output.append(s)
#         # Store all three computed hex values as the color for that step.
#     return output


########################################
# Function to be done with the program.
########################################


def closeOut():
    execTime = (datetime.now(timezone.utc) - startTime).total_seconds()
    aLog("FINISHED AT  : " + str(datetime.now(timezone.utc)))
    aLog("TIME: " + str(round(execTime, 3)) + "s")
    try:
        tmphandlePath = open(str(tmpfile))
        profile = json.load(tmphandlePath)
        tmphandlePath.close()
        # Try to read from temp file.
        for param in ["main1", "main2", "detail1", "detail2", "detailp1", "detailp2"]:
            try:
                profile[param]
            except:
                profile[param] = 0.01
            # Zero out previous parameters, if not already set.
        profile["render"] = execTime
        # Set params for this script.
        tmphandle = open(str(tmpfile), "w")
        tmphandle.write(json.dumps(profile, indent=2, ensure_ascii=False))
        tmphandle.close()
        # Write out file.
    except:
        print("Couldn't log execution time.")
        try:
            profile = {
                "main1": 0.01,
                "main2": 0.01,
                "detail1": 0.01,
                "detail2": 0.01,
                "detailp1": 0.01,
                "detailp2": 0.01,
                "render": execTime,
            }
            # Set zeroed params.
            tmphandle = open(str(tmpfile), "w")
            tmphandle.write(json.dumps(profile, indent=2, ensure_ascii=False))
            tmphandle.close()
            # Write file.
        except:
            print("Couldn't save a fresh log either.")
            # Well, to hell with it.
    quit()


########################################
# Function to save the month's summary line to a file.
########################################
# def summarize(arg):
# 	try:
# 		summPath = open(str(summaryPath), 'a')
# 		summPath.write(arg)
# 		summPath.close()
# 		aLog("Summary written to: " + summaryPath)
# 	except:
# 		aLog("Did not write summary line")
def summarize(arg):
    try:
        summPath = open(str(summaryPath), "a")
        summPath.write(arg)
        summPath.close()
        aLog("Summary written to: " + str(summaryPath))
    except:
        aLog("!!! Could not write summary file.")


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


dots = ["·", "⋅"]

# This looks stupid, but it's actually smart.
# #0 is · U+00B7 MIDDLE DOT
# #1 is ⋅ U+22C5 DOT OPERATOR
# #0 will alphabetically sort above #1.

full = {
    "op": "open",
    "kp": "keep",
    "dl": "delete",
    "rd": "redirect",
    "mg": "merge",
    "nc": "no consensus",
    "sk": "speedy keep",
    "sd": "speedy delete",
    "tw": "transwiki",
    "us": "userfy",
    "wd": "withdrawn",
    "ud": "undefined",
}


# full = {
# 	"op": "open",
# 	"sk": "speedy keep",
# 	"kp": "keep",
# 	"nc": "no consensus",
# 	"mg": "merge",
# 	"rd": "redirect",
# 	"dl": "delete",
# 	"sd": "speedy delete",
# 	"tw": "transwiki",
# 	"us": "userfy",
# 	"wd": "withdrawn",
# 	"ud": "undefined"
# }
# Default ordering (makes the table look goofy)

clcol = {
    "op": "#EAECF0",
    "sk": "#A9F2A9",
    "kp": "#CEF2CE",
    "nc": "#F2F2A9",
    "mg": "#F2F2CE",
    "rd": "#F2E0CE",
    "dl": "#F2CECE",
    "sd": "#F2A9A9",
    "tw": "#CEF2F2",
    "us": "#CECEF2",
    "wd": "#D1D3D7",
    "ud": "#F3AAF3",
}
# Sets close colors.

sortkey = {
    "op": [dots[0], dots[0], dots[0], dots[1]],
    "sk": [dots[0], dots[0], dots[1], dots[0]],
    "kp": [dots[0], dots[0], dots[1], dots[1]],
    "nc": [dots[0], dots[1], dots[0], dots[0]],
    "mg": [dots[0], dots[1], dots[0], dots[1]],
    "rd": [dots[0], dots[1], dots[1], dots[0]],
    "dl": [dots[0], dots[1], dots[1], dots[1]],
    "sd": [dots[1], dots[0], dots[0], dots[0]],
    "tw": [dots[1], dots[0], dots[0], dots[1]],
    "us": [dots[1], dots[0], dots[1], dots[0]],
    "wd": [dots[1], dots[0], dots[1], dots[1]],
    "ud": [dots[1], dots[1], dots[0], dots[0]],
}
#               ^       ^       ^       ^
#               8       4       2       1
# Counting up with binary numbers to give a sort key, lol.


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
# This is very, very, very, very stupid.
# Gives a lookup table for 1-deep jsons.
########################################


def reverseUpAJson(json):
    rev = {}
    for asdf in json:
        for qwer in json[asdf]:
            rev[qwer] = asdf
    return rev


########################################
# Try to load a delsort json.
# If it doesn't work, we don't NEED it.
########################################

dsJsonLoaded = 0

try:
    dsJsonFile = open(str(jsonPath))
    dsJson = json.load(dsJsonFile)
    dsJsonFile.close()
    aLog("Successfully loaded delsort json.")
    dsJsonRev = reverseUpAJson(dsJson)
    dsJsonLoaded = 1
except:
    aLog("!!! Couldn't load delsort category json file.")

emojisLoaded = 0
try:
    emojisJsonFile = open(str(emojisPath))
    emojis = json.load(emojisJsonFile)
    emojisJsonFile.close()
    aLog("Successfully loaded delsort emojis.")
    emojisLoaded = 1
except:
    aLog("!!! Couldn't load emojis json file.")

########################################
# Get everybody and their stuff together.
########################################

curTime = datetime.now(timezone.utc)
startTime = curTime
lastTime = curTime
delta = (curTime - lastTime).total_seconds()
# Might use these later, but probably won't.

aLog(
    "Running Oracle for Deletion (renderer), version "
    + version
    + ", at "
    + datetime.now(timezone.utc).isoformat()
    + " UTC, local time "
    + datetime.now().isoformat()
)
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
    try:
        aLog("Running as : " + os.getlogin())
    except:
        aLog("Running as : [couldn't retrieve login]")
    aLog("Cooldown   : " + str(sleepTime))
aLog(
    "Running script for "
    + userRunning
    + ". Processing "
    + str(numberOfDays)
    + " days: "
    + today.strftime("%Y %B %d")
    + " back to "
    + (today - timedelta(days=numberOfDays)).strftime("%Y %B %d")
    + "."
)

########################################
# Okay -- three, two, one...
########################################

if args.configure == True:
    quit()
    # If we're just showing the config data, we're done with the script. Let's scram.

if numberOfDays > 60:
    word = "boat"
    # time.sleep(1)
    if numberOfDays > 120:
        word = "crap"
    if numberOfDays > 360:
        word = "shit"
    if numberOfDays > 720:
        word = "giant shit"
    if ((today - timedelta(days=numberOfDays)).year) < 2001:
        print("DANGER: Wikipedia doesn't go back that far, buddy!")
        aLog(
            "ABORTING EXECUTION: invalid start date ("
            + (today - timedelta(days=numberOfDays)).isoformat()
            + ")"
        )
        quit()
    if ((today - timedelta(days=numberOfDays)).year) < 2006:
        print("CAUTION: AfDs back then were formatted differently.")
        print("This probably isn't going to work the way you want.")
    print(
        "!!!!!  WARNING: This is a "
        + word
        + "load of pages.  !!!!!"
        + "!!!!!     Your output is going to be HUGE     !!!!!"
    )
    # if numberOfDays > 60:
    # time.sleep(5)

########################################
# Let's jam.
########################################

m = "<sup><sub>"
n = "</sub></sup>"
# These are used for formatting table headers.


dayLogPath = (
    str(out)
    + "/"
    + str(outprefix)
    + today.strftime("%Y-%m-%d")
    + "-to-"
    + (today - timedelta(days=numberOfDays)).strftime("%Y-%m-%d")
    + ".txt"
)
# out/outprefix/YYYY-MM-DD-to-YYYY-MM-DD.txt
if args.output != "insanely weird string that nobody would ever type in on purpose.txt":
    dayLogPath = str(out) + "/" + args.output
# This will set the path for the output file, either to the default thing, or to whatever input was given.

outputstring = (
    "\nLast updated: "
    + str(datetime.now(timezone.utc).strftime("%Y-%m-%d, %H:%M (UTC)"))
    + "\n"
)
top = ""
# Create blank template for output text of top index.
top = top + '{|class="wikitable sortable collapsible"'
top = top + "\n|-"
top = top + "\n!'''Contents'''"
top = top + "\n!" + m + "Total" + n
top = top + "\n!" + m + "Open" + n
top = top + "\n!" + m + "Uncom-<br/>mented" + n
top = top + "\n!" + m + "Closed" + n
for asdf in full:
    ## The iterations of this loop will have asdf as "op", "sk", "kp", etc.
    if asdf != "op":
        # print(asdf)
        # For every type of close in the index except "op", put the total of how many there were.
        top = top + '\n!class="' + asdf + '"|' + m + asdf.upper() + n
# print(top)

# totind = ["<span style=\"display:none\">!!!9999</span>'''TOTAL'''",  0,  0,  0,  0,  0,  0,  0]
totind = {
    "date": "<span style=\"display:none\">!!!9999</span>'''TOTAL'''",
    "total": 0,
    "uncom": 0,
    "op": 0,
    "sk": 0,
    "kp": 0,
    "nc": 0,
    "mg": 0,
    "rd": 0,
    "dl": 0,
    "sd": 0,
    "tw": 0,
    "us": 0,
    "wd": 0,
    "ud": 0,
}
# Initialize empty array for total of all days.

o = ""
# Create blank template for output text of main tables.

# grad = createGradient("#CCFFDD", "#FFCCDD", 16)
# 16-step gradient between pale green and pale red.
##midder = createGradient(middest, dellest, 52)[2]
##grad = createGradient(keepest, middest, 50) + createGradient(midder, dellest, 51)
# 101-step gradient between pale green, pale yellow, and pale red.
# The natural midpoint of the gradient is E6E6DD, which I changed to EFEFDD to be a slight bit yellower.
# I started out with FFFFDD, but this was so yellow it made the midrange of results hard to read.
# The next one is 56% (a sixteenth) along the second gradient, not 50, to avoid double-counting it and making two steps the same color.

errorList = []
redLinkList = []
redLinkAfds = {}
allErrorCount = 0
allRedLinkCount = 0
# No error pages for the day yet.
for incr in range(0, numberOfDays):
    # This will go from 0 (today) to numberOfDays (the furthest we want to go back)
    try:
        theDay = today - timedelta(days=incr)
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
            dayLogFile = open(processingPath)
            dlData = json.load(dayLogFile)
            dayLogFile.close()
            if verbose:
                aLog(
                    "Processing "
                    + str(dlData["count"])
                    + " AfDs from "
                    + processingPath
                )
        except:
            aLog("!!! FAILED TO OPEN: " + processingPath)
        # Take the existing string, and add a new section header for each new day being processed.
        m = "<sup><sub>"
        n = "</sub></sup>"
        # These are used for formatting table headers.
        op = ""
        cl = ""
        if aggregate == 0:
            o = o + "\n===" + dayDate + "==="
            op = '\n{| class="wikitable sortable collapsible" style="width:100%"'
            op = op + "\n|-"
            op = op + "\n!'''Open AfDs (relists bolded)'''"
            op = op + "\n!"
            op = op + "\n!" + m + "Keep<br/>%" + n
            op = op + "\n!" + m + "Page<br/>revs" + n
            op = op + "\n!" + m + "Page<br/>eds." + n
            op = op + "\n!" + m + "Page<br/>size" + n
            op = op + "\n!" + m + "Page<br/>made" + n
            op = op + '\n!class="afdheaderbg"|' + m + "AfD<br/>!v #" + n
            # op = op + "\n!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>eds."+n
            op = op + '\n!class="afdheaderbg"|' + m + "AfD<br/>size" + n
            op = op + '\n!class="afdheaderbg"|' + m + "AfD<br/>made" + n
            op = op + '\n!class="afdheaderbg"|' + m + "AfD<br/>last" + n
            op = op + '\n!class="afdheaderbg"|' + m + "Sorts" + n
            # Initialize string that will be a table of all open AfDs for that day.
            cl = '\n{| class="wikitable sortable collapsible collapsed" style="width:100%"'
            cl = cl + "\n|-"
            cl = cl + "\n!'''Closed AfDs (relists bolded)'''"
            cl = cl + "\n!"
            cl = cl + "\n!" + m + "Keep<br/>%" + n
            cl = cl + "\n!" + m + "Page<br/>revs" + n
            cl = cl + "\n!" + m + "Page<br/>eds." + n
            cl = cl + "\n!" + m + "Page<br/>size" + n
            cl = cl + "\n!" + m + "Page<br/>made" + n
            cl = cl + '\n!class="afdheaderbg"|' + m + "AfD<br/>!v #" + n
            # cl = cl + "\n!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>eds."+n
            cl = cl + '\n!class="afdheaderbg"|' + m + "AfD<br/>size" + n
            cl = cl + '\n!class="afdheaderbg"|' + m + "AfD<br/>made" + n
            cl = cl + '\n!class="afdheaderbg"|' + m + "AfD<br/>last" + n
            cl = cl + '\n!class="afdheaderbg"|' + m + "Sorts" + n
            # Initialize string that will be a table of all closed AfDs for that day.
            anchorSetYet = 1
            # We don't want to set anchors at all.
        else:
            anchorSetYet = 0
        # Set this to zero, which means that the renderer will put an anchor in the first entry for the day.
        errorCount = 0
        redLinkCount = 0
        # We haven't messed up rendering any AfDs... yet.
        # Initialize count for open AfDs
        # Initialize count for closed AfDs
        # ind = [dayDate,  0,  0,  0,  0,  0,  0,  0]
        #         0      1   2   3   4   5   6   7
        #               /   /   /     \   \   \   \
        # 	      total open uncom closed  %k  %d  %m
        ind = {
            "date": dayDate,
            "total": 0,
            "uncom": 0,
            "op": 0,
            "sk": 0,
            "kp": 0,
            "nc": 0,
            "mg": 0,
            "rd": 0,
            "dl": 0,
            "sd": 0,
            "tw": 0,
            "us": 0,
            "wd": 0,
            "ud": 0,
        }
        # print(ind)
        # print(dlData["pgs"])
        for page in dlData["pgs"]:
            try:
                # This iterates over every page in that day's AfD.
                # print(page)
                d = dlData["pgs"][page]
                # print(d)
                b = 'class="afdbg"|'
                bnocomments = 'class="afdnocomments"|'
                # Beginning for AfD data cells
                if verbose:
                    print(page)
                # Effective, but unbelievably spammy, debug line that prints every page title as it's processed.
                cellcolor = d["afdinfo"]["close"]
                # Set cell color by taking the "clcol" entry with the index of the AfD close.
                dts = sortkey[d["afdinfo"]["close"]]
                # Do the same for the sortkey.
                ind[d["afdinfo"]["close"]] = ind[d["afdinfo"]["close"]] + 1
                totind[d["afdinfo"]["close"]] = totind[d["afdinfo"]["close"]] + 1
                ind["total"] = ind["total"] + 1
                totind["total"] = totind["total"] + 1
                # if (d['afdinfo']['open'] != 1):
                # if (d['pageinfo']['error'] != "0"):
                # ind[6] = ind[6] + 1
                ## Increment the "delete" counter in the day's index row.
                # cellcolor = delecl
                ## Dark red for closed AfDs where the article doesn't exist.
                # dts = [dots[1], dots[0]]
                ## Sort key: low, high
                # elif (d['pageinfo']['redirect'] != 0):
                # ind[7] = ind[7] + 1
                ## Increment the "merge" counter in the day's index row.
                # cellcolor = elsecl
                ## Dark yellow for closed AfDs where the article is a redirect.
                # dts = [dots[0], dots[1]]
                ## Sort key: high, low
                # else:
                # ind[5] = ind[5] + 1
                ## Increment the "keep" counter in the day's index row.
                # cellcolor = keepcl
                ## Dark green (i.e. keep) for closed AfDs.
                # dts = [dots[0], dots[0]]
                ## Sort key: high, high (will sort highest)
                try:
                    # print("D: " + str(d['afdinfo']['vdl'] + d['afdinfo']['vsd'] + d['afdinfo']['vmg'] + d['afdinfo']['vrd'] + d['afdinfo']['vdr'] + d['afdinfo']['vus']) + " / K: " + str(d['afdinfo']['vkp'] + d['afdinfo']['vsk']) + " / T: " + str(d['afdinfo']['all']))
                    if d["afdinfo"]["all"] == 0:
                        ratio = "N/A"
                        ratioclass = "pn-a"
                    else:
                        ratio = (
                            d["afdinfo"]["vdl"]
                            + d["afdinfo"]["vsd"]
                            + d["afdinfo"]["vmg"]
                            + d["afdinfo"]["vrd"]
                            + d["afdinfo"]["vdr"]
                            + d["afdinfo"]["vus"]
                        ) / d["afdinfo"]["all"]
                        # Delete, speedy delete, merge, redirect, draftify, and userfy !votes, out of all !votes.
                        ratio = 100 - (ratio * 100.0)
                        # Creates number (from 0 to 100) expressing ratio of how many !votes are delete-like.
                        ratioclass = "000" + str(int(ratio))
                        ratioclass = "p" + ratioclass[-3:] # Last three chars
                        # ratiocolor = str(grad[int(ratio)])
                        # Calculate the actual numbers to display for the ratio (i.e. formulate as keep %, and truncate decimals)
                        ratio = str(ratio)[0:5]
                except:
                    aLog("Couldn't calculate ratio for " + page)
                    ratio = "?"
                    ratioclass = "?"
                s = ""
                # Initialize blank string for this row. Rows for open and closed AfDs are the same,
                # which means we can use the same code for both, THEN decide which table to put it in.
                new = "\n|"
                # Newline string (this just makes the code less ugly)
                s = s + "\n|-"
                s = s + '\n|class="' + cellcolor + '" |'
                for asdf in ["st nom", "nd nom", "rd nom", "th nom"]:
                    if d["afd"]["afdtitle"].lower().count(asdf) != 0:
                        s = s + "∗"
                        # add a U+2217 ASTERISK OPERATOR if it's an nth nom
                if d["afd"]["relist"] > 0:
                    s = s + "'''"
                    # Bold it and if it's a relist
                s = s + "[[Wikipedia:Articles for deletion/" + d["afd"]["afdtitle"] + "|" + page + "]]"
                if d["afd"]["relist"] > 0:
                    s = s + "'''"
                    # Close the bolding if it's a relist
                if anchorSetYet == 0:
                    s = s + "{{anchor|" + dayDate + "}}"
                    anchorSetYet = 1
                    # Add an anchor and disable the sentry variable.
                linkscolumn = (
                    '\n|'
                    + dts[0]
                    + "[["
                    + page
                    + "|a]]"
                    + dts[1]
                    + "[[Talk:"
                    + page
                    + "|t]]"
                    + dts[2]
                    + "[[Special:History/"
                    + page
                    + "|h]]"
                    + dts[3]
                )
                for asdf in ["File", "Image", "Category"]:
                    ln = len(asdf)+2
                    if linkscolumn[0:ln].lower() == ("[[" + asdf.lower()):
                        linkscolumn.replace("[[", "[[:")
                        # Add a colon to the page link if warranted,
                        # because on January 2, 2008, someone nominated
                        # the freaking Xbox logo at AfD, and it'll just embed the whole thing otherwise.

                # The dts[0] and dts[1] are the sort keys.
                # Since these colums are the same thing no matter what,
                # we can use two different Unicode dots to make them sort
                # without throwing things off.
                # To understand this, go way up and look at where dots was assigned.
                ########################################
                # Fix namespace errors in link string.
                ########################################

                # Beware of corner cases: below are actual article titles.
                # Tic Talk: Living with Tourette Syndrome
                # If a Lion Could Talk: Animal Intelligence and the Evolution of Consciousness
                # Shop Talk: A Writer and His Colleagues and Their Work
                # Gadget:Invention, Travel, & Adventure
                # Gadget: Invention, Travel, and Adventure
                # Book:A Novel
                # Book: A Novel
                # Course: Oblivion (Star Trek: Voyager)
                # Topic:The Washington & Jefferson College Review

                linkscolumn = linkscolumn.replace("[[Talk:Talk:", "[[Talk:")
                # Special case for mainspace which doesn't actually have a special name
                nses = ["User",
                        "Wikipedia",
                        "File",
                        "MediaWiki",
                        "Template",
                        "Help",
                        "Category",
                        "Portal",
                        "Draft",
                        "TimedText",
                        "Module"
                        ]
                # There are additional namespaces that no longer exist.
                # But, since they don't exist, their talk pages don't either.
                # That is to say, the talk page for "Book:A Novel" really IS "Talk:Book:A Novel".
                # So these ones do not actually need to be fixed.
                        #"Book",
                        #"Course",
                        #"Institution",
                        #"Education Program",
                        #"Flow",
                        #"Gadget",
                        #"Gadget definition",
                        #"Topic",
                        #"Special",
                        #"Media"

                for ns in nses:
                    # Note: We have to do the [[ at the beginning because sometimes articles are...
                    # well... 
                    linkscolumn = linkscolumn.replace(("[[Talk:" + ns + " talk:"), ("[[" + ns + " talk:"))
                    # "Talk:TimedText talk:" -> "TimedText talk:"
                    linkscolumn = linkscolumn.replace(("[[Talk:" + ns + ":"), ("[[" + ns + " talk:"))
                    # "Talk:TimedText" -> "TimedText talk:"

                s = s + linkscolumn
                s = s + '\n|class="pct ' + ratioclass + '"|' + ratio
                # Ratio column
                try:
                    sd = new + str(d["pagestats"]["revisions"])
                    sd = sd + new + str(d["pagestats"]["editors"])
                    sd = sd + new + str(d["pageinfo"]["size"])
                    sd = sd + new + str(d["pagestats"]["created_at"])[0:7]
                    s = s + sd
                    # Add them all to a string and then add that string to s all at once.
                    # This may seem pointless, but it prevents table-breaking.
                    # If it just adds them to s sequentially, and it fails on column 4,
                    # this makes it add a full five dummy columns IN ADDITION to those four.
                    # That is to say, the row will be more than five, and the table will break.
                except:
                    try:
                        sd = new + "−"
                        sd = sd + new + "−"
                        sd = sd + new + str(d["pageinfo"]["size"])
                        sd = sd + new + "−"
                        s = s + sd
                        # Render light version (without XTools queries).
                        # This is what will render if detail.py wasn't run.
                    except:
                        s = s + new + new + new + new
                        #       1     2     3     4
                        # If rendering the light version also failed, dummy out the row.
                        # This will happen if the page was deleted.
                try:
                    if int(d["afdinfo"]["all"]) > 100:
                        countstring = "100"
                    else:
                        countstring = "000" + str(int(d["afdinfo"]["all"]))
                        countstring = countstring[-3:]
                    sd = new + 'class="vct p' + countstring + '"|' + str(d["afdinfo"]["all"])
                        # Add normal background color for commented AfD to the line.
                    # sd = sd + new + str(d['afdstats']['editors'])
                    # Commented out line for AfD editor count.
                    sd = sd + new + str(d["afdinfo"]["size"])
                    sd = sd + new + str(d["afdstats"]["created_at"])[5:]
                    sd = sd + new + str(d["afdstats"]["modified_at"])[5:]
                    s = s + sd
                    # See above comment for why this is necessary.
                except:
                    try:
                        if int(d["afdinfo"]["all"]) > 100:
                            countstring = "100"
                        else:
                            countstring = "000" + str(int(d["afdinfo"]["all"]))
                            countstring = countstring[-3:]
                        sd = new + 'class="vct p' + countstring + '|' + str(d["afdinfo"]["all"])
                        if d["afdinfo"]["all"] == 0:
                            sd = new + bnocomments + str(d["afdinfo"]["all"])
                        # sd = sd + new + "−"
                        # Commented out line for AfD editor count.
                        sd = sd + new + str(d["afdinfo"]["size"])
                        sd = sd + new + "−"
                        sd = sd + new + "−"
                        s = s + sd
                        # Render the light version of the AfD row (omitting XTools info).
                        # This is what will render if detail.py wasn't run.
                    except:
                        aLog("Failed to render AfD for" + d["afd"]["afdtitle"])
                        # s=s+n+b+n+b+n+b+n+b+n+b+n+b
                        #   1   2   3   4   5   6
                        s = s + new + new + new + new + new
                        #   1   2   3   4   5
                ################################################################################
                # This next thing will try to parse some emojis for the delsort.
                ################################################################################
                try:
                    s = s + new
                    if d["afdinfo"]["delsorts"] != 0:
                        already = []
                        # We don't want to print the same emoji eight times in a row,
                        # even if there are redundant delsorts that would cause us to do this.
                        for asdf in range(len(d["afdinfo"]["delsorts"]["sub"])):
                            try:
                                if (
                                    emojis[d["afdinfo"]["delsorts"]["top"][asdf]]
                                    not in already
                                ):
                                    if len(already) < 6:
                                        s = s+ emojis[d["afdinfo"]["delsorts"]["top"][asdf]]
                                already.append(
                                    emojis[d["afdinfo"]["delsorts"]["top"][asdf]]
                                )
                                # Add emoji for the top-level cat, if there's an emoji for it.
                            except:
                                s = s
                            try:
                                if (
                                    emojis[d["afdinfo"]["delsorts"]["sub"][asdf]]
                                    not in already
                                ):
                                    if len(already) < 6:
                                        s = s+ emojis[d["afdinfo"]["delsorts"]["sub"][asdf]]
                                already.append(
                                    emojis[d["afdinfo"]["delsorts"]["sub"][asdf]]
                                )
                                # Add emoji for the sub cat, if there's an emoji for it.
                            except:
                                s = s
                            s = s + " "
                            # print(d['afdinfo']['delsorts']['top'][asdf])
                            # print(d['afdinfo']['delsorts']['sub'][asdf])
                except:
                    print("Couldn't parse delsorts")
                ################################################################################
                # End delsort emoji parsing.
                ################################################################################
                if d["afdinfo"]["close"] == "op":
                    op = op + s
                    # If the AfD is open, add it to the open-AfD table string.
                else:
                    cl = cl + s
                    # If the AfD is closed, add it to the closed-AfD table string.
            except KeyboardInterrupt:
                raise(Exception)
                exit()
            except Exception as err:
                print("Error: ", err)
                # If there is some bizarre mystery bug that makes no sense.
                try:
                    try:
                        # If it can pull the afdinfo and afdstats, but they're empty (means the AfD was deleted)
                        print("!! AfD info says: " + str(d["afdinfo"]["error"]))
                        print("!! AfD stats say: " + str(d["afdstats"]["error"]))
                        # If these stats can't be pulled, it'll throw an error into the except block.
                        # Otherwise, we know that it was a redlink!
                        redLinkList.append(page)
                        aLog("!!Deleted AfD(?): " + page)
                        o = o + "<!-- Probably a deleted AfD: " + page + "-->"
                        redLinkAfds[page] = d["afd"]["afdtitle"]
                        # print(redLinkAfds)
                        redLinkCount = redLinkCount + 1
                    except Exception as err:
                        print("Error: ", err)
                        # If it can't pull the stats for the page (likely means the propertizers messed up)
                        errorList.append(page)
                        aLog("Couldn't process " + page)
                        o = o + "<!-- Couldn't process a page: " + page + "-->"
                        # o = o + "<!-- Couldn't process a page: " + str(dlData["pgs"][page])
                        errorCount = errorCount + 1
                except Exception as err:
                    print("Error: ", err)
                    errorCount = errorCount + 1
                    errorList.append("UNKNOWN")
                    aLog(
                        "Couldn't process a page, and couldn't even figure out what it was."
                    )
                    o = (
                        o
                        + "<!-- Couldn't process a page, and trying to tell what page it was failed. -->"
                    )
        ################################################################################
        # Add that day's redlink and error counts to the totals.
        ################################################################################
        allRedLinkCount = allRedLinkCount + redLinkCount
        allErrorCount = allErrorCount + errorCount
        ################################################################################
        # Render a row for that day, in the index summary at the top of the page.
        ################################################################################
        top = top + "\n|-"
        top = top + "\n| " + "[[#" + str(dayDate) + "|" + str(dayDate) + "]]"
        if errorCount != 0:
            top = top + " (" + str(errorCount) + ")"
            # If there's errors, put them in parentheses next to the date.
        if redLinkCount != 0:
            top = top + " ."
        # print(ind)
        closed = ind["total"] - ind["op"]
        top = top + "\n| " + str(ind["total"])
        if ind["op"] == 0:
            top = top + '\n|class="indGrayed"| 0'
        else:
            top = top + "\n| " + str(ind["op"])
        if ind["uncom"] == 0:
            top = top + "\n| 0"
        else:
            top = top + '\n|class="afdnocomments"|' + str(ind["uncom"])
        top = top + "\n| " + str(closed)
        for asdf in full:
            ## The iterations of this loop will have asdf as "op", "sk", "kp", etc.
            if asdf != "op":
                # For every type of close in the index except "op", put the total of how many there were.
                if ind[asdf] == 0:
                    top = top + "\n| "
                else:
                    top = top + "\n| " + str(ind[asdf])
        ################################################################################
        # Add all the stuff to the index table for the top.
        ################################################################################
        if aggregate == 0:
            o = (
                o
                + "\n====Open AfDs, "
                + dayDate
                + " ("
                + str(ind["op"])
                + ")===="
                + op
                + "\n|}\n====Closed AfDs, "
                + dayDate
                + " ("
                + str(ind["total"] - ind["op"])
                + ")====\n"
                + cl
                + "\n|}"
            )
        else:
            o = o + op + cl
        # print(o)
        ##########
        # End of codeblock that runs over every day's AfD log in the batch.
        ##########
    except (KeyboardInterrupt):
        aLog("ABORTING EXECUTION: KeyboardInterrupt")
        quit()
##### All days have now been processed, time to start compositing the output page.

################################################################################
# Render a row for the month's totals.
################################################################################
sumup = ""
sumup = sumup + "\n|-"
sort = '<span style="display:none">' + dots[0] + "</span>"
sumup = sumup + "\n| " + sort + "'''Total'''"
# Col 1: period of time
closed = totind["total"] - totind["op"]
sumup = sumup + "\n| " + sort + str(totind["total"])
# Col 2: total AfDs
summed = sumup
# What we store in the summary file should be the same as the page output, up to this point.
if ind["op"] == 0:
    sumup = sumup + '\n|class="indGrayed"|' + sort + "0"
    # Col 3: Number of open AfDs (zero, grayed out)
else:
    sumup = sumup + "\n|" + sort + str(totind["op"])
    # Col 3: Number of open AfDs (normal background)
if ind["uncom"] == 0:
    sumup = sumup + "\n|" + sort + "0"
    # Col 4: Number of uncommented AfDs (zero)
else:
    sumup = sumup + '\n|class="afdnocomments"|' + sort + str(totind["uncom"])
    # Col 4: Number of uncommented AfDs (nonzero, special background)
sumup  = sumup  + "\n|" + sort + str(closed)
summed = summed + "\n|" + sort + str(closed)
# Col 5: number of closed AfDs
for asdf in full:
    ## The iterations of this loop will have asdf as "op", "sk", "kp", etc.
    if asdf != "op":
        # For every type of close in the index aside from "op", put the total of how many there were.
        sumup  = sumup  + "\n|" + sort + str(totind[asdf])
        summed = summed + "\n|" + sort + str(totind[asdf])
        # Cols 6 - 16: totals for each close type.
pageLink = "[[User:JPxG/Oracle/" + str(dayDate)[0:7] + "|" + str(dayDate)[0:7] + "]]"
summarize(summed.replace("'''Total'''", pageLink).replace(sort, ""))
# Log the slightly-altered line (no "open" or "uncommented" counts) to the summary file.
top = top + sumup
# Add all the stuff to the index table for the sumup.
################################################################################
# Render a row for the month's averages.
################################################################################
m = "<sup><sub>"
n = "</sub></sup>"
top = top + "\n|-"
sort = '<span style="display:none">' + dots[1] + "</span>"
top = top + "\n| " + sort + "'''Average'''"
closed = totind["total"] - totind["op"]
top = top + "\n| " + sort + str(totind["total"] / numberOfDays)[0:5]
if ind["op"] == 0:
    top = top + '\n|class="indGrayed"|' + sort + "0"
else:
    top = top + "\n|" + sort + str(totind["op"] / numberOfDays)[0:5]
if ind["uncom"] == 0:
    top = top + "\n|" + sort + "0"
else:
    top = top + '\n|class="afdnocomments"|' + sort + str(totind["uncom"] / numberOfDays)[0:5]
top = top + "\n|" + sort + str(closed / numberOfDays)[0:5]
for asdf in full:
    ## The iterations of this loop will have asdf as "op", "sk", "kp", etc.
    if asdf != "op":
        if closed == 0:
            closed = 0.1
        # For every type of close in the index aside from "op", put the total of how many there were.
        top = (
            top
            + "\n|"
            + sort
            + m
            + str(float(100.0 * (totind[asdf] / closed)))[0:4]
            + "%"
            + n
        )
# Add all the stuff to the index table for the top.
################################################################################
top = top + "\n|}\n"
# Close the table for the index at the top.


# top = top + "\n|-"
# top = top + "\n| " + sort + "'''AVERAGE'''"
# top = top + "\n| " + sort + str(totind[1])
# top = top + "\n| " + sort + str(totind[2])
# top = top + "\n| " + sort + str(totind[3])
# top = top + "\n| " + sort + str(totind[4])
# if (totind[4] != 0):
# 	# If there are any freaking closes at all.
# 	top = top + "\n| " + sort + str(float(100*(totind[5] / totind[4])))[0:5]
# 	top = top + "\n| " + sort + str(float(100*(totind[6] / totind[4])))[0:5]
# 	top = top + "\n| " + sort + str(float(100*(totind[7] / totind[4])))[0:5]
# else:
# 	# Avoid the classic meme "I JUST DIVIDED BY ZERO OH SHI-"
# 	top = top + "\n| " + sort + "0"
# 	top = top + "\n| " + sort + "0"
# 	top = top + "\n| " + sort + "0"
# Composite table-of-contents index table with "total" row.
if aggregate == 1:
    top = "<onlyinclude>" + top
    if redLinkList:
        top = top + "\n:''Unretrievable AfDs (" + str(allRedLinkCount) + "): "
        for err in redLinkList:
            top = (
                top
                + "[[Wikipedia:Articles for deletion/"
                + redLinkAfds[err]
                + "|"
                + err
                + "]]<sup>[[Special:WhatLinksHere/Wikipedia:Articles for deletion/"
                + redLinkAfds[err]
                +"|@]]</sup>, "
            )
            # print("[[Wikipedia:Articles for deletion/" + redLinkAfds[err] + "|" + err + "]], ")
        top = top[:-2] + "''"
    if errorList:
        top = top + "\n:''Unknown errors (" + str(allErrorCount) + "): "
        for err in errorList:
            top = top + "[[Wikipedia:Articles for deletion/" + err + "|" + err + "]]"
            top = top + "<sup>[[Special:WhatLinksHere/Wikipedia:Articles for deletion/" + err + "|@]]</sup>, "
        top = top[:-2] + "''"
        # Trim that last freakin' comma.
    # Record all the errors in a HTML note.
    top = top + "\n</onlyinclude>"
    top = top + '\n{| class="wikitable sortable collapsible" style="width:100%"'
    top = top + "\n|-"
    top = top + "\n!'''AfDs (relists bolded)'''"
    top = top + "\n!"
    top = top + "\n!" + m + "Keep<br/>%"
    top = top + "\n!" + m + "Page<br/>revs"
    top = top + "\n!" + m + "Page<br/>eds."
    top = top + "\n!" + m + "Page<br/>size"
    top = top + "\n!" + m + "Page<br/>made"
    top = top + '\n!!class="afdheaderbg"|' + m + "AfD<br/>!v #"
    # top = top + "\n!!style=\"background:" + afdheaderbg + "\"|"+m+"AfD<br/>eds."
    top = top + '\n!!class="afdheaderbg"|' + m + "AfD<br/>size"
    top = top + '\n!!class="afdheaderbg"|' + m + "AfD<br/>made"
    top = top + '\n!!class="afdheaderbg"|' + m + "AfD<br/>last"
    top = top + '\n!!class="afdheaderbg"|' + m + "Sorts" + n
    # Create start, and headers, for big aggregate column.
    o = o + "\n|}"
    # Terminate output string for AfD table.
outputstring = outputstring + "__NOTOC__\n" + top + o
# Composite output string from beginning section, top index table, and day tables.
try:
    dayLogFile = open(dayLogPath, "w")
    dayLogFile.write(outputstring)
    dayLogFile.close()
    aLog("Successfully saved: " + dayLogPath)
    aLog("Total length: " + str(len(outputstring)))
except:
    aLog("!!! FAILED TO SAVE: " + dayLogPath)
closeOut()
# Log how long it took.
