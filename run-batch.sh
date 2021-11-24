# JPxG, 2021 August 18

# This will run every OfD script, while passing parameters to the scripts.
# You MUST type something for -h, -v, and -c if you use them
# (i.e. "-v asdf" instead of just "-v")

# Standard shit (1 week, output to normal zone)
# python3 main.py        -v -b 14 -s 0.01
# python3 detail.py      -v -b 14 -s 0.01
# python3 detailpages.py -v -b 14 -s 0.01
# python3 render.py      -v -b 14 -o render.txt
# python3 upload.py      -v -b 14 -o User:JPxG/sandbox67

# Basic template for running them all in series:
#python3 main.py        -v -b 31 -l 2021-06-30 -s 0.01
#python3 detail.py      -v -b 31 -l 2021-06-30 -s 0.01
#python3 detailpages.py -v -b 31 -l 2021-06-30 -s 0.01
#python3 render.py      -v -b 31 -l 2021-06-30 -o render.txt
#python3 upload.py      -v -o User:JPxG/sandbox68 -n "Parsing June 2021"

while getopts v:h:c:a:g:f:s:b:l:o:w:q flag
do
	case "${flag}" in
		v) verbose=1;;
		h) help=1;;
		c) cfg=1;;
		a) all=1;;
		g) aggregate=1;;
		f) fast=1;;
		s) sleep=${OPTARG};;
		b) back=${OPTARG};;
		l) last=${OPTARG};;
		o) output=${OPTARG};;
		w) overwrite=${OPTARG};;
		q) sql=1;;
	esac
done

arst1=""
arst2=""
arst3=""
arst4=""
arst5=""
# Argument strings for each command (since some scripts don't take some flags)

if [ "$help" = 1 ]; then
	echo "This script runs all five components in order, and passes arguments to them."
	echo "Usage looks like, for example, this:"
	echo "  bash run-batch.sh -v 1 -s 0.1 -b 31 -l 2021-01-31 -o User:JPxG/sandbox99"
	echo "The flags work the same way here as they do in the individual components (and specifying no options will cause it to simply process the last 7 days):"
	echo "  -o    title of the output page on Wikipedia"
	echo "  -b    how many days to go back"
	echo "  -l    the latest day to parse (YYYY-MM-DD)"
	echo "  -s    sleep time between API queries (in seconds, will take decimals)"
	echo "  -w 1  overwrite existing files when scraping skeletons (this will clean damaged json, but may ruin lots of finished pages)"
	echo "  -f 1  skip XTools queries to make less detailed table, cuts execution time by about 95% (a month will take ~1 minute instead of ~30)"
	echo "  -q 1  detail table with SQL queries instead of XTools queries, also cuts execution time by a lot but can only be used if you are running this from a Toolforge account or Toolforge SSH tunnel"
	echo "  -g 1  enable aggregate output (one big table, instead of new sections/tables for different days)"
	echo "  -v 1  enable verbose mode"
	echo "  -h 1  print this help message and exit"
	echo "  -a 1  print every individual component's help message and exit"
	echo "  -c 1  print every individual component's configuration details and exit"
	echo ""
	echo "Note: -g, -v, -h, -a, -c cannot be supplied bare. This means you must supply them as '-v 1', '-v asdf', et cetera, or the script will go berserk. If you don't want to run these flags, just don't specify them at all."
	echo ""
	echo "Also note that individual components have more flags, which provide finer control, and are not available from this shell script. If you want to specify a password from the command line, for example, running upload.py manually will allow you to do this with '-p'. See the component helps for more information (you can do so by invoking this script with '-a 1')."
	exit 1
fi

if [ "$verbose" = 1 ]; then
	arst1="$arst1 -v"
	arst2="$arst2 -v"
	arst3="$arst3 -v"
	arst4="$arst4 -v"
	arst5="$arst5 -v"
fi
# If verbose is set, then add -v to the argument string.


if [ "$all" = 1 ]; then
	arst1="$arst1 -h"
	arst2="$arst2 -h"
	arst3="$arst3 -h"
	arst4="$arst4 -h"
	arst5="$arst5 -h"
fi
# If help is set, then add -h to the argument string.

if [ "$cfg" = 1 ]; then
	arst1="$arst1 -c"
	arst2="$arst2 -c"
	arst3="$arst3 -c"
	arst4="$arst4 -c"
	arst5="$arst5 -c"
fi
# If configure is set, then add -c to the argument string.

if [ "$aggregate" = 1 ]; then
	# main.py doesn't take -a
	# detail.py doesn't take -a
	# detailpages.py doesn't take -a
	arst4="$arst4 -a"
	# upload.py doesn't take -a
fi
# If last.

if [ "$sql" = 1 ]; then
	# main.py doesn't take this flag.
	arst2="$arst4 -q"
	# detailpages.py doesn't take this flag.
	# render.py doesn't take this flag.
	# upload.py doesn't take this flag.
fi
# If you want it to use the SQL queries.

if [ "$overwrite" = 1 ]; then
	arst1="$arst1 -o"
	# detail.py doesn't take this flag.
	# detailpages.py doesn't take this flag.
	# render.py doesn't take this flag.
	# upload.py doesn't take this flag.
fi
# If last.

if [ "$sleep" ]; then
	arst1="$arst1 -s $sleep"
	arst2="$arst2 -s $sleep"
	arst3="$arst3 -s $sleep"
	# render.py doesn't take -s as a flag
	# upload.py doesn't take -s as a flag
fi
# If sleep is set, pass sleep to the scripts.

if [ "$back" ]; then
	arst1="$arst1 -b $back"
	arst2="$arst2 -b $back"
	arst3="$arst3 -b $back"
	arst4="$arst4 -b $back"
	# upload.py doesn't take -b as a flag
fi
# If back is set.

if [ "$last" ]; then
	arst1="$arst1 -l $last"
	arst2="$arst2 -l $last"
	arst3="$arst3 -l $last"
	arst4="$arst4 -l $last"
	# upload.py doesn't take -l as a flag
fi
# If last.

arstupload=$arst

if [ "$output" ]; then
	# upload.py is the only one that takes -o for what we want
	arst5="$arst5 -o $output"
fi
# If last.

arst4="$arst4 -o render.txt"
#Specify render.txt as output for render.py if it's being run in the pipeline

python3 main.py        $arst1

if [ "$fast" ]; then
	arst2="$arst2"
else
	python3 detail.py      $arst2
fi
# Skip that nonsense if you're running it in fast mode.

python3 detailpages.py $arst3
python3 render.py      $arst4
python3 upload.py      $arst5