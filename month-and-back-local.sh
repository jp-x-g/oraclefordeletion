# Fetches the whole current month, and also goes 31 days back.
# Renders and uploads the resultant month page, and master dashboard.
# JPxG, 2021 November 26

backby=$1

#DAYS=$(cal $(date +"%m %Y") | awk 'NF {DAYS = $NF}; END {print DAYS}')
# Days of the current month. Props to sleeplessbeastie.eu who came up with this
# Commented out, since this messes up on the last day of the month.

DD=$(date +%d)
MM=$(date +%m)
YYYY=$(date +%Y)

DD=$((10#$DD))
#Convert, e.g., "09" to "9"

if [ "$MM" = "01" ]; then
	DAYS="31"
fi

if [ "$MM" = "02" ]; then
	if [ "$year" = 2112 ] || [ "$year" = 2108 ] || [ "$year" = 2104 ] || [ "$year" = 2096 ] || [ "$year" = 2092 ] || [ "$year" = 2088 ] || [ "$year" = 2084 ] || [ "$year" = 2080 ] || [ "$year" = 2076 ] || [ "$year" = 2072 ] || [ "$year" = 2068 ] || [ "$year" = 2064 ] || [ "$year" = 2060 ] || [ "$year" = 2056 ] || [ "$year" = 2052 ] || [ "$year" = 2048 ] || [ "$year" = 2044 ] || [ "$year" = 2040 ] || [ "$year" = 2036 ] || [ "$year" = 2032 ] || [ "$year" = 2028 ] || [ "$year" = 2024 ] || [ "$year" = 2020 ] || [ "$year" = 2016 ] || [ "$year" = 2012 ] || [ "$year" = 2008 ] || [ "$year" = 2004 ] || [ "$year" = 2000 ]
	# Yeah, I'll be dead by the time anyone gets mad about this.
	then
		DAYS="29"
	else
		DAYS="28"
	fi
fi

if [ "$MM" = "03" ]; then
	DAYS="31"
fi

if [ "$MM" = "04" ]; then
	DAYS="30"
fi

if [ "$MM" = "05" ]; then
	DAYS="31"
fi

if [ "$MM" = "06" ]; then
	DAYS="30"
fi

if [ "$MM" = "07" ]; then
	DAYS="31"
fi

if [ "$MM" = "08" ]; then
	DAYS="31"
fi

if [ "$MM" = "09" ]; then
	DAYS="30"
fi

if [ "$MM" = "10" ]; then
	DAYS="31"
fi

if [ "$MM" = "11" ]; then
	DAYS="30"
fi

if [ "$MM" = "12" ]; then
	DAYS="31"
fi


daysback=$(($backby-$DD))
# How many days to go back into the previous month
# (0 if it's 31, 2 if it's 29, etc)

goback=$(($DAYS+$daysback))
# How many days to go back past the end of this month
# (0 if it's 31, 33 if it's 29, etc)

echo "$goback"
five="5"
echo "$topday"
#echo "$topday"
#echo "$topday"

python3 main.py                 -o -v -b $goback -l $YYYY-$MM-$DAYS -s 0.01
python3 detail.py               -q -v -b $goback -l $YYYY-$MM-$DAYS -s 0.01
python3 detailpages.py             -v -b $goback -l $YYYY-$MM-$DAYS -s 0.01
cp data/tmp/tmp.txt data/tmp/tmp2.txt

python3 render.py               -a -v -b $DAYS   -l $YYYY-$MM-$DAYS -o render.txt
python3 upload.py     			   -v -o User:JPxG/Oracle/$YYYY-$MM -n "Updating from local instance."
# Render and upload the monthly page.

mv data/tmp/tmp2.txt data/tmp/tmp.txt
python3 render.py                  -v -b $DAYS   -l $YYYY-$MM-$DD   -o render.txt
python3 upload.py     			   -v -o User:JPxG/Oracle -n "Updating from local instance."
# Render and upload the dashboard


#python3 detail.py                  -v -b 1 -l 2014-10-05 -s 0.01
#python3 detailpages.py             -v -b 1 -l 2014-10-05 -s 0.01
#python3 render.py              -a -v -b 31 -l 2014-10-31 -o render.txt
#python3 upload.py      -v -o User:JPxG/Oracle/2014-10 -i render.txt -n "Attempt to fix two errors (redlinks) on 2014-10-11, and 1 unicode error on 2014-10-05."

#[x@localhost afd]$ bash run-batch.sh -w 1 -b 31 -s 0.01 -o User:JPxG/Oracle -q 1
#[x@localhost afd]$ bash run-batch.sh -w 1 -g 1 -b 30 -l 2021-11-30 -v 1 -s 0.01 -o User:JPxG/Oracle/2021-11 -q 1
