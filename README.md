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

Basic tasks (like scanning a range of days from the AfD logs, parsing the table and uploading it) should be done by running the shell script (run.sh) with appropriate flags.

Advanced tasks (like scanning 100 days of nominations from the AfD logs, getting page stats for 28 of them, rendering a separate table for each week, and uploading them all to separate pages) should be done by running each component individually.