![The Oracle contemplating the haze of general notability guidelines.](/logo.jpg)

This is a piece of software intended to provide a simple yet powerful utility to Wikipedia editors who participate in, monitor, and close discussions at [AfD](https://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion).

Specifically, this is what it does:

- Parse a range of dates
- Create a set of files containing a list of all Articles for Deletion discussions from those dates
- Populate the files with detailed information about the deletion discussions and the articles themselves
- Render a wikitext page in which this information is displayed in interactive, sortable tables
- Authenticate to a bot account and upload the wikitext to a page on the project

It contains five scripts, intended to be run in sequence, and a shell script that does so. Both the shell script and the individual components take numerous command-line arguments, which are explained thoroughly by running them with the -h flag.

**If you have no idea what to do with this software, do this and you will learn how to use it:**
> ``cd oraclefordeletion``

> ``bash run-batch.sh -h 1``

Basic and straightforward tasks (like scanning a range of days from the AfD logs, parsing the table and uploading it) should be done by running the shell script (run-batch.sh) with appropriate flags. Here's an example: gathering 14 days of AfD logs from November 2016, processing them verbosely with a cooldown of 0.75 seconds, and posting the result to ``User:Example/AfD_oracle``:
> ``run-batch.sh -b 100 -l 2016-11-14 -s 0.75 -v 1 -o User:Example/AfD_oracle``

Advanced or bizarre tasks (like scanning 100 days of nominations from the AfD logs, getting page stats for 28 of them, rendering a separate table for each week, and uploading them all to separate pages) should be done by running each component individually.
> ``python3 main.py -b 100 -l 2020-12-31``

> ``python3 detail.py -b 28 -l 2020-12-31``

> ``python3 detailpages.py -b 28 -l 2020-12-31``

> ``python3 render.py -b 7 -l 2020-12-31 -o render1.txt``

> ``python3 render.py -b 7 -l 2020-12-24 -o render2.txt``

> ``python3 render.py -b 7 -l 2020-12-17 -o render3.txt``

> ``python3 render.py -b 7 -l 2020-12-10 -o render4.txt``

> ``python3 upload.py -i render1.txt -o User:Example/AfD_end_of_December``

> ``python3 upload.py -i render2.txt -o User:Example/AfD_late_December``

> ``python3 upload.py -i render3.txt -o User:Example/AfD_mid-December``

> ``python3 upload.py -i render4.txt -o User:Example/AfD_beginning_of_December``