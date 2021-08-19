![The Oracle contemplating the haze of general notability guidelines.](/logo.jpg)

This is a piece of software intended to provide a simple yet powerful utility to Wikipedia editors who participate in, monitor, and close discussions at [AfD](https://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion).

Specifically, this is what it does:

- Parse a range of dates
- Create a set of files containing a list of all Articles for Deletion discussions from those dates
- Populate the files with detailed information about the deletion discussions and the articles themselves
- Render a wikitext page in which this information is displayed in interactive, sortable tables
- Authenticate to a bot account and upload the wikitext to a page on the project

It contains five scripts, intended to be run in sequence. 
