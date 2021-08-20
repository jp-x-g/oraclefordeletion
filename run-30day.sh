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

#python3 main.py        -v -b 31 -l 2021-06-30 -s 0.01
#python3 detail.py      -v -b 31 -l 2021-06-30 -s 0.01
#python3 detailpages.py -v -b 31 -l 2021-06-30 -s 0.01
#python3 render.py      -v -b 31 -l 2021-06-30 -o render.txt
#python3 upload.py      -v -o User:JPxG/sandbox68 -n "Parsing June 2021"

while getopts v:h:c:a:s:b:l:o: flag
do
	case "${flag}" in
		v) verbose=1;;
		h) help=1;;
		c) cfg=1;;
		a) all=1;;
		s) sleep=${OPTARG};;
		b) back=${OPTARG};;
		l) last=${OPTARG};;
		o) output=${OPTARG};;
	esac
done

arst1=""
arst2=""
arst3=""
arst4=""
arst5=""
# Argument strings for each command (since some scripts don't take some flags)

if [ "$verbose" = 1 ]; then
	arst1="$arst1 -v"
	arst2="$arst2 -v"
	arst3="$arst3 -v"
	arst4="$arst4 -v"
	arst5="$arst5 -v"
fi
# If verbose is set, then add -v to the argument string.

if [ "$help" = 1 ]; then
	echo "This script will render and post a page for a full 30-day interval, regardless of how many pages are being newly scraped."
	echo "If you want to render a different number of pages, use run-batch.sh instead!"
	echo ""
	echo "This script runs all five components in order, and passes arguments to them."
	echo "Usage looks like, for example, this:"
	echo "  bash run-batch.sh -v 1 -s 0.1 -b 31 -l 2021-01-31 -o User:JPxG/sandbox99"
	echo "The flags work the same way here as they do in the individual components (and specifying no options will cause it to simply process the last 7 days):"
	echo "  -o    title of the output page on Wikipedia"
	echo "  -b    how many days to go back (render will be last 30 pages no matter what)"
	echo "  -l    the latest day to parse (YYYY-MM-DD)"
	echo "  -s    sleep time between API queries (in seconds, will take decimals)"
	echo "  -v    enable verbose mode"
	echo "  -h    print this help message and exit"
	echo "  -a    print every individual component's help message and exit"
	echo "  -c    print every individual component's configuration details and exit"
	echo ""
	echo "Note: -v, -h, -a and -c cannot be supplied bare. This means you must supply them as '-v 1', '-v asdf', et cetera."
	echo ""
	echo "Also note that individual components have more flags, which provide finer control, and are not available from this shell script. If you want to specify a password from the command line, for example, running upload.py manually will allow you to do this with '-p'. See the component helps for more information (you can do so by invoking this script with '-a 1')."
	exit 1
fi

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
	arst4="$arst4 -b 30"
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
python3 detail.py      $arst2
python3 detailpages.py $arst3
python3 render.py      $arst4
python3 upload.py      $arst5