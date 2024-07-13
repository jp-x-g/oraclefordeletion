# JPxG, 2021 August 09
# Haven't written any software in a long time. This will be extremely painful. For me.

# Required to parse json. Parse parse!
import argparse

# Required to use time. Tick tock!
import json
import os
import time

# For scraping webpages. Scrape scrape!
from datetime import datetime, timedelta, timezone

# This is used so that happy programs can sleep warmly. Snooze snooze!
from pathlib import Path

# For filesystem interactions. Read read! Write write!
import requests

# Required to parse arguments. Parse parse...!!

########################################
# Set all configuration variables.
########################################
version        = "2.5"
userRunning    = "JPxG"

# File system stuff
dataname       = "data"
pagesname      = "pages"
configname     = "cfg"
tempname       = "tmp"
configfilename = "config.txt"
logfilename    = "run1.log"
outfilename    = "output.html"
jsonprefix     = "AfD-log-"
tmpfilename    = "tmp.txt"

stupidKludge   = 0
# Set this to 1 if you want to do the dumbest, most lazy hack nonsense in history.

today          = datetime.utcnow().date()
# This SHOULD be fine in 3.5. May have to change later.

########################################
# Parse arguments from command line.
########################################

parser = argparse.ArgumentParser(
    description="Oracle for Deletion, AfD log parser (1 of 5). This will retrieve the wikitext of AfD log pages, and parse the entries from them into JSON files. It also accompanies the entries with basic information from the log page: the title of the page, the title of the AfD page, relist status, and how many previous nominations the article has had. Note that all dates used by this program are in UTC, including timestamps in the runlog.",
    epilog="This will run pretty quickly, even though it doesn't batch its API queries. Take care to specify reasonable dates; AfD was called VfD (and worked differently) prior to 2005-08-28, and Wikipedia did not exist prior to January 2001.",
)
parser.add_argument(
    "-b",
    "--back",
    metavar="DAYS",
    help='Number of days to parse. Default is 7. This will be overridden if you specify both "latest" and "earliest"!',
    default=69420,
)
parser.add_argument(
    "-l",
    "--latest",
    metavar="YYYY-MM-DD",
    help="Date to parse back from. Default is today (UTC)",
    default=today,
)
parser.add_argument(
    "-e",
    "--earliest",
    metavar="YYYY-MM-DD",
    help='Date to parse back to. Default is to determine it automatically by subtracting "back" from "latest".',
    default="1420-06-09",
)
parser.add_argument(
    "-o",
    "--overwrite",
    help="Overwrite existing data when saving skeletons. Only do this if you want to completely restart the reprocessing.",
    action="store_true",
)
parser.add_argument(
    "-s",
    "--sleep",
    metavar="S",
    help="Time, in seconds, to delay between receiving an API response and sending the next request. Default is 0.5.",
    default=0.5,
)
parser.add_argument(
    "-d",
    "--dryrun",
    help="Run the script without actually sending queries to the API. This may break stuff.",
    action="store_true",
)
parser.add_argument(
    "-v",
    "--verbose",
    help="Spam the terminal AND runlog with insanely detailed information. Wheee!",
    action="store_true",
)
parser.add_argument(
    "-c",
    "--configure",
    help="Set up directories and runlog, then show configuration data and exit.",
    action="store_true",
)
parser.add_argument(
    "-x",
    "--explain",
    help="Display specific, detailed information about what this program does, then exit.",
    action="store_true",
)
parser.add_argument(
    "-i",
    "--input",
    help="Use alternate input file for list of articles/AfDs (will disregard other options)",
    default="Don't use one, doofus.",
)

# , or determined automatically if you specify \"back\" and \"earliest\".
# Too hard to implement now, may do later.

args = parser.parse_args()
# today = datetime.fromisoformat(str(args.latest))
# earliest = datetime.fromisoformat(str(args.earliest))
# Commenting these out to replace with strptime, for Python 3.5 compatibility

today = datetime.strptime(str(args.latest), "%Y-%m-%d")
earliest = datetime.strptime(str(args.earliest), "%Y-%m-%d")

if args.explain:
    print("This is the first in a series of scripts.")
    print(" For happiness to bloom,")
    print("  all must work together.")
    print("   Without this one,")
    print("    the others cannot work,")
    print("     and without the others,")
    print("      this one cannot work.")
    print("       Such is life.")
    print(
        "The specific task of this script is to set up JSON skeletons of AfD log pages, without much information about the pages in question. After this script, the .JSONs will be populated by the next one, which uses XTools to get page statistics, and the third one, which uses the en.wikipedia API to parse actual page content. Finally, the renderer uses all of this information to generate a page."
    )
    quit()

print(args)

verbose = 0
if args.verbose:
    verbose = 1

overwrite = 0
if args.overwrite:
    overwrite = 1

forReal = 1
if args.dryrun:
    forReal = 0

sleepTime = float(args.sleep)

if args.back == 69420:
    numberOfDays = 7
else:
    numberOfDays = int(args.back)
# This may look stupid, but I'm using it to determine if it's 7 days as given by the user or 7 days as given by the default value for the argument.

if args.earliest == "1420-06-09":
    useAltStartDate = False
    earliestDay = today - timedelta(days=(numberOfDays - 1))
    # If it's still the default value, and hasn't been specified.
else:
    if args.back != 69420:
        print("!!!   WARNING: Too many date parameters have been supplied   !!!")
        print("!!! Ignoring supplied interval, going by earliest and latest !!!")
        print("!!!  Double-check and make sure this is what you want to do  !!!")
    # 	earliestDay = datetime.fromisoformat(str(args.earliest))
    earliestDay = datetime.strptime(str(args.earliest), "%Y-%m-%d")
    numberOfDays = (today - earliestDay).days + 1
    # If we've specified an earliest and latest day, we'll compute numberOfDays from them.

daysDelta = timedelta(days=numberOfDays)

useInputFile = 0
if args.input != "Don't use one, doofus.":
    inputFileName = args.input
    useInputFile = 1
    numberOfDays = 1
    # earliestDay  = datetime.fromisoformat("2001-01-01")
    # today        = datetime.fromisoformat("2001-01-01")
    # earliest     = datetime.fromisoformat("2001-01-01")
    # Comment these out for 3.5 compatibility. Replacing with lines below.
    earliestDay = datetime.strptime("2001-01-01", "%Y-%m-%d")
    today = datetime.strptime("2001-01-01", "%Y-%m-%d")
    earliest = datetime.strptime("2001-01-01", "%Y-%m-%d")
    # If we're using an input file, then just like, whatever, man.


# Set configuration variables from args.
# This is awkward, but I wrote the script before I wrote the arg parser, lol.

########################################
# Here be file system stuff.
########################################

# This is the directory where all program-generated data should live.
data           = Path(os.getcwd() + "/" + dataname)
# This is the directory that JSON encodings of AfD log pages will be parsed to.
pages          = Path(os.getcwd() + "/" + dataname   + "/" + pagesname)
# Config files live here.
config         = Path(os.getcwd() + "/" + configname)
# Temporary file directory (doesn't need to persist between sessions)
tmp            = Path(os.getcwd() + "/" + dataname   + "/" + tempname)
tmpfile        = Path(os.getcwd() + "/" + dataname   + "/" + tempname + "/" + tmpfilename)
# Stupid kludge.
pagePath       = Path(os.getcwd() + "/" + dataname   + "/" + tempname + "/page.html")
configFilePath = Path(os.getcwd() + "/" + configname + "/" + configfilename)
logFilePath    = Path(os.getcwd() + "/" + dataname   + "/" + logfilename)
outputPath     = Path(os.getcwd() + "/" + dataname   + "/" + outfilename)

########################################
# Make sure those paths exist.
########################################

data.mkdir(  mode=0o777, exist_ok=True)
pages.mkdir( mode=0o777, exist_ok=True)
config.mkdir(mode=0o777, exist_ok=True)
tmp.mkdir(   mode=0o777, exist_ok=True)

########################################
# Function to read from the input file (if we're doing that)
########################################
def openInputFile(name):
    inputPath = open(str(name), "rb")
    inputContents = inputPath.read().decode()
    inputPath.close()
    inputContents = inputContents.split("\n")

    stringystrangy = "\n\n"
    for i in range(0, len(inputContents)):
        stringystrangy += "\n{{Wikipedia:Articles for deletion/" + str(inputContents[i]) + "}}"
    return stringystrangy


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
        daLog.write("\nSetting up runtime log for  " +
                    str(datetime.now(timezone.utc)) + "\n" + argument
        )
        daLog.close()
        print(argument)


########################################
# Get everybody and their stuff together.
########################################

curTime = datetime.now(timezone.utc)
startTime = curTime
lastTime = curTime
delta = (curTime - lastTime).total_seconds()
# Might use these later, but probably won't.

aLog(
    "Running Oracle for Deletion (AfD parser), version "
    + version
    + ", at "
    + datetime.now(timezone.utc).isoformat()
    + " UTC, local time "
    + datetime.now().isoformat()
)
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
    + (today - timedelta(days=(numberOfDays - 1))).strftime("%Y %B %d")
    + "."
)

if args.back != 69420:
    time.sleep(4)

if args.configure == True:
    quit()
    # If we're just showing the config data, we're done with the script. Let's scram.'

########################################
# Okay -- three, two, one...
########################################

if numberOfDays > 60:
    word = "boat"
    time.sleep(1)
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
        + "load of pages.  !!!!!\n"
        + "!!!!! I sure hope you know what you're doing. !!!!!"
    )
    # if numberOfDays > 60:
    # time.sleep(5)

########################################
# Let's jam.
########################################

# initialize afdDay, which we'll be using to store all the day for the data.
afdDay = {}
# this will go from 0 (today) to numberOfDays (the furthest we want to go back)
for incr in range(0, numberOfDays):
    try:
        # the day we're going to be dealing with is today minus the increment:
        theDay = today - timedelta(days=incr)
        # the day that the day is, formatted like a normal human being would choose
        dayDate = theDay.strftime("%Y-%m-%d")
        # the url for that day is, formatted like Wikipedia would choose:
        # note that it's %-d and not %d, because the AfD urls don't have zero-padded days
        dayText = theDay.strftime("%Y_%B_%-d")
        theDayUrl = (
            "http://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion/Log/"
            + dayText
        )
        theWikitextUrl = (
            "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Wikipedia%3AArticles_for_deletion%2FLog%2F"
            + dayText
            + "&rvslots=*&rvprop=content&formatversion=2&format=json"
        )
        # initialize afdDay with the date it's being scraped at, as well as some other stuff.
        afdDay = {
            "scrapedate": today.isoformat(),
            "afddate": dayDate,
            "afddatetext": dayText,
            "count": 0,
        }
        if verbose:
            aLog(
                "Fetching page "
                + str(incr + 1)
                + " of "
                + str(numberOfDays)
                + ": "
                + theWikitextUrl
            )
        # if forReal:
        # print("Doing it for real.")
        # time.sleep(sleepTime)
        # r = requests.get(theWikitextUrl, allow_redirects=False)
        # paegfile = open(pagePath, 'wb')
        # paegfile.write(r.content)
        # paegfile.close()
        # paeg = open(pagePath, 'rb')
        # Okay, if forReal is set, this will actually hit the server for a page.
        if forReal:
            # print("Doing it for real.")
            time.sleep(sleepTime)
            if useInputFile == 0:
                r = requests.get(theWikitextUrl, allow_redirects=False)
                ## Actually hit the URL in this line, and get a page, which will be of type "Response"
                r = r.text
                ## Make it so that "r" is the text of the response, not a "Response" of the response
                r = json.loads(r)
                # Make it so that "r" is the parsed JSON of "r", not text
                ###################################################
                # Now we're going to store the stuff into an array.
                ###################################################
                # Do this for each page in the response (not currently necessary, but why not).
            if useInputFile == 1:
                r = {
                    "query": {
                        "pages": {
                            "Dummy information (will be overwritten in a few lines)"
                        }
                    }
                }
            for eachPage in r["query"]["pages"]:
                afdDay["title"] = "Wikipedia:Articles_for_deletion/Log/" + dayText
                try:
                    pageContent = eachPage["revisions"][0]["slots"]["main"]["content"]
                except:
                    aLog("!!! Failed to retrieve page content for that day.")
                    pageContent = "Failed to retrieve content."
                # Get a string of the content we want to store.
                ##########
                # Stupid disgusting hack. Do this to process raw text of an AfD series, if you're a weirdo.
                if useInputFile == 1:
                    pageContent = openInputFile(inputFileName)
                ##########
                pageContent = pageContent.replace("_", " ")
                afdDay["content"] = pageContent
                # Store the content of the page as 'content' for that day's entry.
                # Also, replace underscores with spaces.
                afdDay["pgs"] = {}
                # Create empty array for the list of pages that day.
                searchStr = "\n{{Wikipedia:Articles for deletion/"
                # The search string for each entry.
                afdCount = afdDay["content"].count(searchStr)
                # Count number of AfDs.
                # if verbose:
                # 	print("Found " + str(afdCount) + " AfDs.")
                location = 0
                # Start our cursor at the beginning of the string.
                afdCounter = 1
                # How many have been done (this starts at 1 to be correct)
                # print(pageContent)
                while location < len(pageContent):
                    # Make the last place of the cursor the beginning of what we want to slice out.
                    lastLocation = location
                    # Find the search string in the string.
                    location = pageContent.find(searchStr, lastLocation + 1)
                    # If there's no more, get outta here.
                    if location == -1:
                        location = len(pageContent)
                    theSlice = pageContent[lastLocation:location]
                    # if verbose:
                    # 	print("Slice " + str(afdCounter) + ", from " + str(lastLocation) + " to " + str(location) + ": " + theSlice)
                    nom = 1
                    relist = 0
                    article = ""
                    ########################################
                    # Store entries in json with attributes.
                    # This is a big, ugly, nasty thing.
                    # Essentially, it parses each entry.
                    # If it's relisted, it notes that.
                    # If it's a renom, it notes that.
                    # The data will be stored under the key of
                    # the actual article title, with entries:
                    #    "relist" (int, whether is relisted)
                    #    "nom" (int, which nomination it is)
                    #    "afd" (str, title of AfD page)
                    ########################################
                    # Check and see if it's a relist.
                    if theSlice.find("<!--Relisted-->") != -1:
                        relist = 1

                    # Chop off the beginning and end of the string, getting the actual link to the AfD page.
                    theSlice = theSlice[len(searchStr) : theSlice.find("}}")]
                    # Initialize article title to the same as the AfD title (will be true unless it's a renom)
                    # print(article)
                    # if verbose:
                    # print(theSlice + " (relist = " + str(relist) + ")")

                    ########################################
                    # Remove naughty characters et cetera.
                    ########################################

                    theSlice = theSlice.replace("‎", "")
                    # This looks like it doesn't do anything, but it does!!
                    # It is removing U+200E LEFT-TO-RIGHT MARK.
                    if theSlice.count("  ") != 0:
                        while theSlice.count("  ") != 0:
                            print("Trimming")
                            theSlice = theSlice.replace("  ", " ")
                            # Eliminate double, multiple spaces in the title string. These don't exist to MediaWiki:
                            # that is to say, {{Wikipedia:Articles for deletion/Dog  (2nd nomination)}} in the source
                            # will just load  [[Wikipedia:Articles for deletion/Dog (2nd nomination)]] as the page.
                            # There can't be a page with consecutive spaces! So the transclusion is just an error.
                    if theSlice.count("{{{pg|") != 0:
                        theSlice = theSlice.replace("{{{pg|", "")
                        theSlice = theSlice.replace("}}}", "")
                        # These start showing up once you go back far enough (first instance was in 2008)
                    if theSlice.count("|") != 0:
                        theSlice = theSlice[0 : theSlice.find("|")]
                        # If there is a pipe in the title of the AfD page (this really did happen, in the log for 2010 May 27)
                    ########################################
                    # The following block of code is a massive meme.
                    # Basically, it checks for if the page is a renomination.
                    # If so, it slices the string down to the actual page's title,
                    # and notes which nomination it is.
                    ########################################

                    article = theSlice
                    for ordinal in [
                        "2nd",
                        "3rd",
                        "4th",
                        "5th",
                        "6th",
                        "7th",
                        "8th",
                        "9th",
                        "10th",
                        "11th",
                        "12th",
                        "13th",
                        "14th",
                        "15th",
                        "16th",
                        "17th",
                        "18th",
                        "19th",
                        "20th",
                    ]:
                        # Couldn't find any article with more than 17 nominations, so not including these.
                        # , "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th"]:
                        # print("Checking for " + ordinal + ": " + ordinal[0:len(ordinal) - 2])
                        if theSlice.find(" (" + ordinal + " nomination)") != -1:
                            # Trim the ordinal, i.e. "2nd" -> "2".
                            nom = int(ordinal[0 : len(ordinal) - 2])
                            article = theSlice[
                                0 : theSlice.find(" (" + ordinal + " nomination)")
                            ]
                            # print("Nomination: " + str(nom))
                    ordsText = [
                        "zeroth",
                        "first",
                        "second",
                        "third",
                        "fourth",
                        "fifth",
                        "sixth",
                        "seventh",
                        "eighth",
                        "ninth",
                        "tenth",
                        "eleventh",
                        "twelfth",
                        "thirteenth",
                        "fourteenth",
                        "fifteenth",
                        "sixteenth",
                        "seventeenth",
                        "eighteenth",
                        "nineteenth",
                        "twentieth",
                    ]
                    # Yes, people actually did this sometimes.
                    for ordinal in range(0, 21):
                        # There are 21 items in the list, so we want 0 to 20 as indices.
                        # print("Checking for " + ordinal + ": " + ordinal[0:len(ordinal) - 2])
                        if theSlice.find(" (" + ordsText[ordinal] + " nomination)") != -1:
                            # Trim the ordinal, i.e. "2nd" -> "2".
                            # print("FOUND A WEIRD NOMINATION ORDINAL!!!!!!!!!!!!")
                            # print(theSlice)
                            # print(str(ordinal))
                            nom = int(ordinal)
                            article = theSlice[
                                0 : theSlice.find(
                                    " (" + ordsText[ordinal] + " nomination)"
                                )
                            ]
                            # print(str(article))
                            # print("Nomination: " + str(nom))
                    # articleJson = {article: {"afd": {"relist": relist, "nom": nom, "afdtitle": theSlice}}
                    # articleJson = {"afd": {"relist": relist, "nom": nom, "afdtitle": theSlice}}
                    # print(json.dumps(articleJson))
                    if (
                        (article != "")
                        and (article.find("boilerplate metadata vfd") == -1)
                        and (article.find("{{Imbox") == -1)
                        and (article.find("\n") == -1)
                        and (theSlice.find("{{about|") == -1)
                    ):
                        # Eliminate bug where large chunks of text at the beginning of the page would be stored as an AfD
                        article = article.strip()
                        # article = article.replace("  ", " ")
                        # Spent a while tracking this one down... it was "Chinese Language Institute  (2nd nomination)."
                        # Note the two spaces! So it was being put into the json as "Chinese Language Institute ". Trail my neko spaces...
                        # afdDay['pgs'].append(articleJson)
                        # print("Adding to list")
                        if article.find("[[Wikipedia:Articles for deletion/Log/") == -1:
                            afdDay["pgs"][article] = {
                                "afd": {
                                    "relist": relist,
                                    "nom": nom,
                                    "afdtitle": theSlice,
                                }
                            }
                            afdCounter = afdCounter + 1
                        else:
                            print("Poopity scoop")
                    # else:
                    # 	if verbose:
                    # 	afdDays[eachPage['title']]['pages'].append(theSlice[len(searchStr):theSlice.find("}}")])
                    ##########
                    # End of block that iterates over each AfD entry.
                    ##########
                afdDay["count"] = afdCounter - 1
                if verbose:
                    aLog(
                        "Loaded AfDs for "
                        + dayDate
                        + ". Count: "
                        + str(afdCounter)
                        + ". Attempting to save..."
                    )
                dayLogPath = str(pages) + "/" + str(jsonprefix) + dayDate + ".json"
                # if verbose:
                # 	aLog("Attempting to save parsed log to " + dayLogPath)
                if overwrite == 1:
                    try:
                        dayLogFile = open(dayLogPath, "w")
                        dayLogFile.write(
                            json.dumps(afdDay, indent=2, ensure_ascii=False)
                        )
                        dayLogFile.close()
                        aLog(
                            "Successfully created: "
                            + dayLogPath
                            + " ("
                            + str(afdCounter)
                            + ")"
                        )
                    except:
                        aLog("!!! FAILED TO SAVE: " + dayLogPath)
                else:
                    aLog("Refusing to overwrite existing file.")
                ##########
                # End of block that iterates over each page in the query's response (will be 1 for now).
                ##########
            ##########
            # End of block that runs if forReal is set.
            ##########
        ##########
        # End of "try" block that iterates over each page in the set of days to scrape.
        ##########

    except (KeyboardInterrupt):
        aLog("ABORTING EXECUTION: KeyboardInterrupt")
        quit()

execTime = (datetime.now(timezone.utc) - startTime).total_seconds()
aLog(
    "FINISHED AT "
    + str(datetime.now(timezone.utc))
    + " ("
    + str(round(execTime, 3))
    + "s total / "
    + str(round((execTime / numberOfDays), 3))
    + "s per entry)"
)
# Log how long it took.
try:
    tmphandle = open(str(tmpfile), "w")
    profile = {}
    profile["main1"] = execTime
    profile["main2"] = numberOfDays
    tmphandle.write(json.dumps(profile, indent=2, ensure_ascii=False))
    tmphandle.close()
except (FileNotFoundError):
    print("Couldn't log execution time.")
# Store to temp file.
