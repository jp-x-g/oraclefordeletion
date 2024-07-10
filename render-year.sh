# JPxG, 2021 August 31
# This isn't a very beautiful script. All it does is concatenate the freakin' months into a year total.
# You use it like this:
# bash render-year.sh 2014

year=$1
echo "Rendering and uploading AfDs for: $year"

echo "" > data/tmp/summary.txt
python3 render.py              -a -b 31 -l $year-12-31 -o temp-renderyear.txt
python3 render.py              -a -b 30 -l $year-11-30 -o temp-renderyear.txt
python3 render.py              -a -b 31 -l $year-10-31 -o temp-renderyear.txt
python3 render.py              -a -b 30 -l $year-09-30 -o temp-renderyear.txt
python3 render.py              -a -b 31 -l $year-08-31 -o temp-renderyear.txt
python3 render.py              -a -b 31 -l $year-07-31 -o temp-renderyear.txt
python3 render.py              -a -b 30 -l $year-06-30 -o temp-renderyear.txt
python3 render.py              -a -b 31 -l $year-05-31 -o temp-renderyear.txt
python3 render.py              -a -b 30 -l $year-04-30 -o temp-renderyear.txt
python3 render.py              -a -b 31 -l $year-03-31 -o temp-renderyear.txt

if [ "$year" = 2112 ] || [ "$year" = 2108 ] || [ "$year" = 2104 ] || [ "$year" = 2096 ] || [ "$year" = 2092 ] || [ "$year" = 2088 ] || [ "$year" = 2084 ] || [ "$year" = 2080 ] || [ "$year" = 2076 ] || [ "$year" = 2072 ] || [ "$year" = 2068 ] || [ "$year" = 2064 ] || [ "$year" = 2060 ] || [ "$year" = 2056 ] || [ "$year" = 2052 ] || [ "$year" = 2048 ] || [ "$year" = 2044 ] || [ "$year" = 2040 ] || [ "$year" = 2036 ] || [ "$year" = 2032 ] || [ "$year" = 2028 ] || [ "$year" = 2024 ] || [ "$year" = 2020 ] || [ "$year" = 2016 ] || [ "$year" = 2012 ] || [ "$year" = 2008 ] || [ "$year" = 2004 ] || [ "$year" = 2000 ]
	# Yeah, I'll be dead by the time anyone gets mad about this.
then
	python3 render.py              -a -b 29 -l $year-02-29 -o temp-renderyear.txt
	# Leap year. February is a longboy.
else
	python3 render.py              -a -b 28 -l $year-02-28 -o temp-renderyear.txt
	# Not a leap year. Normal February.
fi

python3 render.py              -a -b 31 -l $year-01-31 -o temp-renderyear.txt

echo "<templatestyles src=\"User:JPxG/Oracle/styles.css\"/>" > data/tmp/summary-$year.txt
echo "This is a summary of all monthly deletion logpages for $year. This page only shows the total for each month; to see individual day logs, click the link to the month page." >> data/tmp/summarynow.txt
#echo "{{User:JPxG/Oracle/top}}" >> data/tmp/summary-$year.txt
echo "__NOTOC__" >> data/tmp/summary-$year.txt
echo '{|class="wikitable sortable collapsible"' >> data/tmp/summary-$year.txt
echo "|-" >> data/tmp/summary-$year.txt
echo "!'''[[User:JPxG/Oracle/$year|$year]]'''" >> data/tmp/summary-$year.txt
echo "!<sup><sub>Total</sub></sup>" >> data/tmp/summary-$year.txt
echo "!<sup><sub>Parsed</sub></sup>" >> data/tmp/summary-$year.txt
echo "!class=\"kp\"|<sup><sub>KP</sub></sup>" >> data/tmp/summary-$year.txt
echo "!class=\"dl\"|<sup><sub>DL</sub></sup>" >> data/tmp/summary-$year.txt
echo "!class=\"rd\"|<sup><sub>RD</sub></sup>" >> data/tmp/summary-$year.txt
echo "!class=\"mg\"|<sup><sub>MG</sub></sup>" >> data/tmp/summary-$year.txt
echo "!class=\"nc\"|<sup><sub>NC</sub></sup>" >> data/tmp/summary-$year.txt
echo "!class=\"sk\"|<sup><sub>SK</sub></sup>" >> data/tmp/summary-$year.txt
echo "!class=\"sd\"|<sup><sub>SD</sub></sup>" >> data/tmp/summary-$year.txt
echo "!class=\"tw\"|<sup><sub>TW</sub></sup>" >> data/tmp/summary-$year.txt
echo "!class=\"us\"|<sup><sub>US</sub></sup>" >> data/tmp/summary-$year.txt
echo "!class=\"wd\"|<sup><sub>WD</sub></sup>" >> data/tmp/summary-$year.txt
echo "!class=\"ud\"|<sup><sub>UD</sub></sup><onlyinclude>" >> data/tmp/summary-$year.txt
summ=`cat data/tmp/summary.txt`
echo "$summ" >> data/tmp/summary-$year.txt
################################################################################
# Here be dragons: code that actually totals up and averages the monthly totals.
################################################################################
#echo {$summ:46:20}

#touch data/tmp/summary.txt
#summ=`cat data/tmp/summary.txt`
##echo "$summ"
#end="\n"
#lng=${#summ}
## Length of summ.
#
##for i in {1..$lng}
## This won't work, for reasons.
#
#for ((i=1; i<=$lng;i++)); do
	#echo "What da $i"
	#echo `expr index "${summ:i}" "|"`
	#j=`expr index "${summ:i}" "|"`
	#i=$((i+j))
	##i=$((i-1))
#done

# Yeah, I'm not doing this.

################################################################################
# Dragons are over now.
################################################################################
echo "</onlyinclude>" >> data/tmp/summary-$year.txt
echo "|}" >> data/tmp/summary-$year.txt

MM=$(date +%m)
YYYY=$(date +%Y)

# If the year being processed is in the past, we include all of the months.
if [ $YYYY \> $year ]; then
	echo "== [[User:JPxG/Oracle/$year-12|$year-12]] == {{:User:JPxG/Oracle/$year-12}}" >> data/tmp/summary-$year.txt
	echo "== [[User:JPxG/Oracle/$year-11|$year-11]] == {{:User:JPxG/Oracle/$year-11}}" >> data/tmp/summary-$year.txt
	echo "== [[User:JPxG/Oracle/$year-10|$year-10]] == {{:User:JPxG/Oracle/$year-10}}" >> data/tmp/summary-$year.txt
	echo "== [[User:JPxG/Oracle/$year-09|$year-09]] == {{:User:JPxG/Oracle/$year-09}}" >> data/tmp/summary-$year.txt
	echo "== [[User:JPxG/Oracle/$year-08|$year-08]] == {{:User:JPxG/Oracle/$year-08}}" >> data/tmp/summary-$year.txt
	echo "== [[User:JPxG/Oracle/$year-07|$year-07]] == {{:User:JPxG/Oracle/$year-07}}" >> data/tmp/summary-$year.txt
	echo "== [[User:JPxG/Oracle/$year-06|$year-06]] == {{:User:JPxG/Oracle/$year-06}}" >> data/tmp/summary-$year.txt
	echo "== [[User:JPxG/Oracle/$year-05|$year-05]] == {{:User:JPxG/Oracle/$year-05}}" >> data/tmp/summary-$year.txt
	echo "== [[User:JPxG/Oracle/$year-04|$year-04]] == {{:User:JPxG/Oracle/$year-04}}" >> data/tmp/summary-$year.txt
	echo "== [[User:JPxG/Oracle/$year-03|$year-03]] == {{:User:JPxG/Oracle/$year-03}}" >> data/tmp/summary-$year.txt
	echo "== [[User:JPxG/Oracle/$year-02|$year-02]] == {{:User:JPxG/Oracle/$year-02}}" >> data/tmp/summary-$year.txt
	echo "== [[User:JPxG/Oracle/$year-01|$year-01]] == {{:User:JPxG/Oracle/$year-01}}" >> data/tmp/summary-$year.txt
fi

# If the year being processed is this year, we will only include months if they have existed yet.
if [ $YYYY = $year ]; then
	if [ "$MM" \> 11 ]; then
		echo "== [[User:JPxG/Oracle/$year-12|$year-12]] == {{:User:JPxG/Oracle/$year-12}}" >> data/tmp/summary-$year.txt
	fi
	if [ "$MM" \> 10 ]; then
		echo "== [[User:JPxG/Oracle/$year-11|$year-11]] == {{:User:JPxG/Oracle/$year-11}}" >> data/tmp/summary-$year.txt
	fi
	if [ "$MM" \> 09 ]; then
		echo "== [[User:JPxG/Oracle/$year-10|$year-10]] == {{:User:JPxG/Oracle/$year-10}}" >> data/tmp/summary-$year.txt
	fi
	if [ "$MM" \> 08 ]; then
		echo "== [[User:JPxG/Oracle/$year-09|$year-09]] == {{:User:JPxG/Oracle/$year-09}}" >> data/tmp/summary-$year.txt
	fi
	if [ "$MM" \> 07 ]; then
		echo "== [[User:JPxG/Oracle/$year-08|$year-08]] == {{:User:JPxG/Oracle/$year-08}}" >> data/tmp/summary-$year.txt
	fi
	if [ "$MM" \> 06 ]; then
		echo "== [[User:JPxG/Oracle/$year-07|$year-07]] == {{:User:JPxG/Oracle/$year-07}}" >> data/tmp/summary-$year.txt
	fi
	if [ "$MM" \> 05 ]; then
		echo "== [[User:JPxG/Oracle/$year-06|$year-06]] == {{:User:JPxG/Oracle/$year-06}}" >> data/tmp/summary-$year.txt
	fi
	if [ "$MM" \> 04 ]; then
		echo "== [[User:JPxG/Oracle/$year-05|$year-05]] == {{:User:JPxG/Oracle/$year-05}}" >> data/tmp/summary-$year.txt
	fi
	if [ "$MM" \> 03 ]; then
		echo "== [[User:JPxG/Oracle/$year-04|$year-04]] == {{:User:JPxG/Oracle/$year-04}}" >> data/tmp/summary-$year.txt
	fi
	if [ "$MM" \> 02 ]; then
		echo "== [[User:JPxG/Oracle/$year-03|$year-03]] == {{:User:JPxG/Oracle/$year-03}}" >> data/tmp/summary-$year.txt
	fi
	if [ "$MM" \> 01 ]; then
		echo "== [[User:JPxG/Oracle/$year-02|$year-02]] == {{:User:JPxG/Oracle/$year-02}}" >> data/tmp/summary-$year.txt
	fi
	echo "== [[User:JPxG/Oracle/$year-01|$year-01]] == {{:User:JPxG/Oracle/$year-01}}" >> data/tmp/summary-$year.txt
fi

mv data/tmp/summary-$year.txt data/output/summary-$year.txt

python3 upload.py -o User:JPxG/Oracle/$year -i summary-$year.txt -n "Updating $year."