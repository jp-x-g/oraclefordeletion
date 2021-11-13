![The Oracle contemplating the haze of general notability guidelines.](/logo.jpg)

This is a piece of software intended to provide a simple yet powerful utility to Wikipedia editors who participate in, monitor, and close discussions at [AfD](https://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion).

Specifically, this is what its components do:

- **main.py**: Parse a range of dates, and use the en.wikipedia API to create a set of files containing a list of all Articles for Deletion discussions from those dates
- **detail.py**: Populate the files with detailed information about the articles themselves and their deletion discussions using the Xtools API.
- **detailpages.py**: Populate the files with additional information about the pages, and statistics about deletion discussions, parsed from their respective wikitext using the en.wikipedia API.
- **render.py**: Render a wikitext page in which this information is displayed in interactive, sortable tables.
- **upload.py**: Authenticate to a bot account and upload the wikitext to a page on the project.

It contains five scripts, intended to be run in sequence (except for detail.py, which lenghtens runtime considerably and can be skipped). There are also shell scripts that run the programs automatically according to user-supplied parameters. Both the shell script and the individual components take numerous command-line arguments, which are explained thoroughly by running them with the -h flag. 

## Table of contents
**[Basic usage](#basic-usage)**

**[Programs (to run the software directly)](#all-scripts-and-their-usage)**
> [main.py (1 of 5)](#mainpy)

> [detail.py (2 of 5)](#detailpy)

> [detailpages.py (3 of 5)](#detailpagespy)

> [render.py (4 of 5)](#renderpy)

> [upload.py (5 of 5)](#uploadpy)

**[Batch scripts (to batch multiple programs together)](#batch-scripts)**
> [batch-year.sh](#batch-yearsh)

> [run-batch.sh](#run-batchsh)

> [render-year.sh](#render-yearsh)

## Basic usage
> [back to top](#table-of-contents)

If you have no idea what to do with this software, do this and you will learn how to use it:
> ``cd oraclefordeletion``

> ``bash run-batch.sh -h 1``

Basic and straightforward tasks (like scanning a range of days from the AfD logs, parsing the table and uploading it) should be done by running the shell script (run-batch.sh) with appropriate flags. Here's an example: gathering 14 days of AfD logs from November 2016, processing them verbosely with a cooldown of 0.75 seconds, and posting the result to ``User:Example/AfD_oracle``:
> ``bash run-batch.sh -b 14 -l 2016-11-14 -s 0.75 -v 1 -o User:Example/AfD_oracle``

Advanced or bizarre tasks (like scanning 100 days of nominations from the AfD logs, getting page stats for 28 of them, rendering a separate table for each week, and uploading them all to separate pages) should be done by running each component individually.
```
python3 main.py -b 100 -l 2020-12-31
python3 detail.py -b 28 -l 2020-12-31
python3 detailpages.py -b 28 -l 2020-12-31
python3 render.py -b 7 -l 2020-12-31 -o render1.txt
python3 render.py -b 7 -l 2020-12-24 -o render2.txt
python3 render.py -b 7 -l 2020-12-17 -o render3.txt
python3 render.py -b 7 -l 2020-12-10 -o render4.txt
python3 upload.py -i render1.txt -o User:Example/AfD_end_of_December
python3 upload.py -i render2.txt -o User:Example/AfD_late_December
python3 upload.py -i render3.txt -o User:Example/AfD_mid-December
python3 upload.py -i render4.txt -o User:Example/AfD_beginning_of_December
```

## Program scripts

### main.py
> [back to top](#table-of-contents)

Usage: ``main.py [-h] [-b DAYS] [-l YYYY-MM-DD] [-e YYYY-MM-DD] [-o] [-s S] [-d] [-v] [-c] [-x]``

Oracle for Deletion, AfD log parser (1 of 5). This will retrieve the wikitext of AfD log pages using the en.wikipedia API, and parse the entries from them into JSON files.

It also accompanies the entries with basic information from the log page: the title of the page, the title of the AfD page, relist status, and how many previous nominations the article has had.

The JSON skeletons will not have much information about the pages in question. After this script, the skeletons will be populated by the next one, which uses XTools to get page statistics, and the third one, which uses the en.wikipedia API to parse actual page content. Finally, the renderer uses all of this information to generate a page.

Note that all dates used by this program are in UTC, including timestamps in the runlog.

**Optional arguments:**
```
-h, --help                           Show this help message and exit.
-b DAYS, --back DAYS                 Number of days to parse. Default is 7. This will be overridden
                                       if you specify both "latest" and "earliest"!
-l YYYY-MM-DD, --latest YYYY-MM-DD   Date to parse back from. Default is today (UTC)
-e YYYY-MM-DD, --earliest YYYY-MM-DD Date to parse back to. Default is to determine it 
                                       automatically by subtracting "back" from "latest".
-o, --overwrite                      Overwrite existing data when saving skeletons. Only do this if
                                       you want to completely restart the reprocessing.
-s S, --sleep S                      Time, in seconds, to delay between receiving an API response
                                       and sending the next request. Default is 0.5.
-d, --dryrun                         Run the script without actually sending queries to the API.
                                       This may break stuff.
-v, --verbose                        Spam the terminal AND runlog with insanely detailed info.
-c, --configure                      Set up directories and runlog, then show config data and exit.
-x, --explain                        Display detailed info about what this program does, then exit.
```

This will run pretty quickly, even though it doesn't batch its API queries. Take care to specify reasonable dates; AfD was called VfD (and worked
differently) prior to 2005-08-28, and Wikipedia did not exist prior to January 2001.

### detail.py
> [back to top](#table-of-contents)

Usage: ``detail.py [-h] [-b DAYS] [-l YYYY-MM-DD] [-s S] [-m MAX] [-d] [-v] [-c] [-x]``

**Page stats detailer (2 of 5).** This will take JSON skeleton created by the previous script, and use XTools to populate them with statistics (like number of revisions, creation date, et cetera) for both the articles (pagestats) and and their deletion discussions (afdstats). Note that all dates used by this program are in UTC, including timestamps in the runlog. After this script, and the other one that handles the actual page content, the renderer can generate a page.

**Optional arguments:**
```
-h, --help                           Show this help message and exit.
-b DAYS, --back DAYS                 Days to go back. Default is 7.
-l YYYY-MM-DD, --latest YYYY-MM-DD   Date to parse back from. Default is today (UTC).
-s S, --sleep S                      Time, in seconds, to delay between receiving an API response
                                       and sending the next request. Default is 0.5.
-m MAX, --max MAX                    Maximum queries to make before stopping. Default is 0 (parse
                                       all entries in the specified interval). Setting this will
                                       probably cut off execution in the middle of a logpage, so 
                                       it's pretty stupid to do this unless you know what you're
                                       doing, or you're testing the script.                     
-d, --dryrun                         Run the script without actually sending queries to the API.
                                       This may break stuff.
-v, --verbose                        Spam the terminal AND runlog with insanely detailed info.
-c, --configure                      Set up directories and runlog, then show config data and exit.
-x, --explain                        Display detailed info about what this program does, then exit
                                       (incl. a full list of fields it gets from the API).
```
                        
Be aware that this one takes forever to run, as XTools doesn't allow batched requests: typical times on JPxG's computer have taken between 0.5 and 1.3 seconds per query. Since AfD log pages can have up to a hundred nominations, and each nomination is two queries, you're going to be here for a while.

These fields are retrieved for both the article at AfD and the AfD nomination page itself.

```
scrapetime           | timestamp | when the data is retrieved (i.e. in a few seconds)
error                |           | should be "0" unless the page is messed up
watchers             | number    | number of people with the page watchlisted
pageviews            | number    | number of pageviews in the last [offset] days
pageviews_offset     | number    | how many days pageviews are given for: should be 30
revisions            | number    | total number of revisions for the page
editors              | number    | total number of distinct editors
minor_edits          | number    | number of edits tagged "minor"
author               | string    | creator of page's username
author_editcount     | number    | creator's edit count
created_at           | timestamp | YYYY-MM-DD
created_rev_id       | number    | revision id for first revision
modified_at          | timestamp | YYYY-MM-DD HH:MM
secs_since_last_edit | number    | this should be pretty obvious, pal
last_edit_id         | number    | revision id for last edit
assessment           | string    | "C", "Stub", "???", et cetera.
```

### detailpages.py
> [back to top](#table-of-contents)

Usage: ``detailpages.py [-h] [-b DAYS] [-l YYYY-MM-DD] [-s S] [-q N] [-m MAX] [-d] [-v] [-u] [-c] [-x] [-z]``

**Page info detailer (3 of 5).** This will get wikitext from the en.wiki API, and use it to populate the JSON files of AfD log pages with information for both the articles (pageinfo) and and their deletion discussions (afdinfo). Feature counts (like refs, sections, and !votes) are approximate, and will miss some things. Note that all dates used by this program are in UTC, including timestamps in the runlog. After this script is run, the renderer can generate a page.

**Optional arguments:**
```
-h, --help                           Show this help message and exit.
-b DAYS, --back DAYS                 Days to go back. Default is 7.
-l YYYY-MM-DD, --latest YYYY-MM-DD   Date to parse back from. Default is today (UTC).
-s S, --sleep S                      Time, in seconds, to delay between receiving an API response
                                       and sending the next request. Default is 0.5.
-q N, --querysize N                  Number of pairs to batch in each query. Default (and maximum
                                       allowed by the API) is 25.
-m MAX, --max MAX                    Maximum queries to make before stopping. Default is 0 (parse
                                       all entries in the specified interval). Setting this will
                                       probably cut off execution in the middle of a logpage, so
                                       it's pretty stupid to do this unless you know what you're
                                       doing, or you're testing the script.
-d, --dryrun                         Run the script without actually sending queries to the API.
                                       This may break stuff.
-v, --verbose                        Spam the terminal AND runlog with insanely detailed info.
-u, --debug                          Spam the ever-loving hell out of the terminal.
-c, --configure                      Set up directories and runlog, then show config data & exit.
-x, --explain                        Display detailed info about what this program does & exit.
                                       (including a full list of the fields it gets from the API)
-z, --zero                           Put in fake placeholder values for AfD information, to run
                                       the parser on lists of normal pages.
```

This uses the "revisions" API endpoint, in its default mode, which supplies a single revision (the latest) of each page specified. The API's maximum batch size is 50; since each article is paired with an AfD page, the maximum batch size for this program is 25.

```
 Page info | NOTE: Feature counts (refs, templates, etc) will probably not be precise
-----------+-------------------------------------------------------------------------
scrapetime | string | ISO timestamp of when the data is received by this program
error      | string | should be "0" unless the page is messed up
redirect   | number | 1 if "#redirect [[" is found, 0 otherwise
size       | number | number of characters in page wikitext (ignores transclusions)
lines      | number | newline characters found
refs       | number | "</ref>"s found
sections   | number | "\n=="s found
templates  | number | "{{"s found
files      | number | "[[File:"s and "[[Image:"s found
cats       | number | "[[Category:"s found
links      | number | "[["s found (minus categories and files)
```
```
 AfD info  | NOTE: Detection is imperfect, and will fail to capture some !votes
-----------+-------------------------------------------------------------------------
scrapetime | string | ISO timestamp of when the data is received by this program
error      | string | should be "0" unless the page is messed up
size       | number | number of characters in page wikitext (ignores transclusions)
lines      | number | newline characters found
delsorts   | number | deletion sorting lines ("<small class="delsort-notice">") found
open       | number | 1, but 0 if "<div class="boilerplate afd vfd xfd-closed"" found
vkp        | number | number of parseable "keep"s
vdl        | number | number of parseable "delete"s
vsk        | number | number of parseable "speedy keep"s
vsd        | number | number of parseable "speedy delete"s
vmg        | number | number of parseable "merge"s
vrd        | number | number of parseable "redirect"s
vtw        | number | number of parseable "transwiki"s
vus        | number | number of parseable "userfy"s
vdr        | number | number of parseable "draftify"s
all        | number | sum of counts for all !vote types above
```


This one runs very quickly, since the en.wiki API allows batched queries.

### render.py
> [back to top](#table-of-contents)

Usage: ``render.py [-h] [-o blahblah.txt] [-b DAYS] [-l DATE] [-a,] [-v] [-c]``

Oracle for Deletion, output renderer (4 of 5). Note that all times and dates used by this program are in UTC, including in the runlog.

**Optional arguments:**
```
-h, --help                           Show this help message and exit.
-o blah.txt, --output blah.txt       Output file, which will be saved in data/output/.
                                       Default is "AfD-render-YYYY-MM-DD-to-YY-MM-DD.txt".)
-b DAYS, --back DAYS                 Days to go back. Default is 7.
-l DATE, --latest DATE               Date to parse back from (YYYY-MM-DD). Default is today (UTC).
-a, --aggregate                      Whether to eliminate the daily headings and just make one
                                       huge table for the whole interval.
-v, --verbose                        Spam the terminal AND runlog with detailed info. Wheee!
-c, --configure                      Set up directories and runlog, then show config data & exit.
```

This one runs almost instantaneously, since there are no API queries.

### upload.py
> [back to top](#table-of-contents)

Usage: ``upload.py [-h] [-n TEXT] [-i blahblah.txt] [-o User:JohnDoe/OfD] [-u JohnDoe@OfD_poster] [-p hunter2] [-d] [-v] [-c] [-x]``

Oracle for Deletion, uploader (5 of 5).

**Optional arguments:**
```
-h, --help                           Show this help message and exit.
-n TEXT, --note TEXT                 Comment to add to edit summary.
-i blah.txt, --input blah.txt        Input file to read, out of data/output/.
                                       Default is render.txt.
-o User:Foo/O, --output User:Foo/O   en.wp page to post the file to. Default is User:JPxG/Oracle.
                                       Be careful with this; it is easy to do something stupid.
-u Foo@OfD, --username Foo@OfD       Specify username to authenticate with.
                                       Default is to read from cfg/login.txt.
-p hunter2, --password hunter2       Specify password to authenticate with.
                                       Default is to read from cfg/login.txt.
-d, --dryrun                         Run the script without actually editing the page.
-v, --verbose                        Spam the terminal AND runlog with insanely detailed info.
-c, --configure                      Set up directories and runlog, then show config data & exit.
-x, --explain                        Display detailed info about what this program does & exit.
```

## Batch scripts

### batch-year.sh
> [back to top](#table-of-contents)

This is just a bunch of ``run-batch.sh`` invocations, with the proper date ranges and flags set, to automatically scrape, detail, render, and upload monthly summary pages for every year from 2037 back to 2001. Uncomment lines in this script if you want to run it.

### run-batch.sh
> [back to top](#table-of-contents)

This script runs all five components in order, and passes arguments to them automatically.
Usage looks like, for example, this:
> ``bash run-batch.sh -v 1 -s 0.1 -b 31 -l 2021-01-31 -o User:JPxG/sandbox99``

The flags work the same way here as they do in the individual components (and specifying no options will cause it to simply process the last 7 days):
```
-o                                   title of the output page on Wikipedia
-b                                   how many days to go back
-l                                   the latest day to parse (YYYY-MM-DD)
-s                                   sleep time between API queries in seconds (will take decimals)
-w 1                                 Overwrite existing files when scraping skeletons (this will
                                       clean damaged json, but may ruin lots of finished pages)
-f 1                                 skip XTools queries to make less detailed table.
                                       Cuts execution time by about 95% (a month will take
                                       about one minute instead of thirty)
-g 1                                 enable aggregate output (one big table, instead of new
                                       sections/tables for different days)
-v 1                                 enable verbose mode
-h 1                                 print this help message and exit
-a 1                                 print every individual component's help message and exit
-c 1                                 print every individual component's config details and exit
```

Note: ``-g``, ``-v``, ``-h``, ``-a``, and ``-c`` **cannot be supplied bare**. This means you must supply them as '``-v 1``', '``-v asdf``', et cetera, or the script will go berserk. If you don't want to run these flags, just don't specify them at all.

Also note that individual components have more flags, which provide finer control, and are not available from this shell script. If you want to specify a password from the command line, for example, running upload.py manually will allow you to do this with '-p'. See the component helps for more information (you can do so by invoking this script with '-a 1').


### render-year.sh
> [back to top](#table-of-contents)

This will render, and upload, a summary page for the year specified. It will not fetch anything from the API to get information, so you must have all the AfDs downloaded and detailed prior to running this. To use, just invoke the script with the year as its argument.
> ``bash render-year.sh 2014``