# JPxG, 2021 August 31
# This isn't a very beautiful script. All it does is re-render and upload the months for a year.
# This causes twelve edits to be made: one for each month.
# You use it like this:
# bash render-year.sh 2014

year=$1
echo "Rendering and uploading AfDs for: $year"

echo "" > data/tmp/summary.txt
python3 render.py     -a -b 31 -l $year-12-31 -o temp-renderyear12.txt
python3 render.py     -a -b 30 -l $year-11-30 -o temp-renderyear11.txt
python3 render.py     -a -b 31 -l $year-10-31 -o temp-renderyear10.txt
python3 render.py     -a -b 30 -l $year-09-30 -o temp-renderyear09.txt
python3 render.py     -a -b 31 -l $year-08-31 -o temp-renderyear08.txt
python3 render.py     -a -b 31 -l $year-07-31 -o temp-renderyear07.txt
python3 render.py     -a -b 30 -l $year-06-30 -o temp-renderyear06.txt
python3 render.py     -a -b 31 -l $year-05-31 -o temp-renderyear05.txt
python3 render.py     -a -b 30 -l $year-04-30 -o temp-renderyear04.txt
python3 render.py     -a -b 31 -l $year-03-31 -o temp-renderyear03.txt

if [ "$year" = 2112 ] || [ "$year" = 2108 ] || [ "$year" = 2104 ] || [ "$year" = 2096 ] || [ "$year" = 2092 ] || [ "$year" = 2088 ] || [ "$year" = 2084 ] || [ "$year" = 2080 ] || [ "$year" = 2076 ] || [ "$year" = 2072 ] || [ "$year" = 2068 ] || [ "$year" = 2064 ] || [ "$year" = 2060 ] || [ "$year" = 2056 ] || [ "$year" = 2052 ] || [ "$year" = 2048 ] || [ "$year" = 2044 ] || [ "$year" = 2040 ] || [ "$year" = 2036 ] || [ "$year" = 2032 ] || [ "$year" = 2028 ] || [ "$year" = 2024 ] || [ "$year" = 2020 ] || [ "$year" = 2016 ] || [ "$year" = 2012 ] || [ "$year" = 2008 ] || [ "$year" = 2004 ] || [ "$year" = 2000 ]
	# Yeah, I'll be dead by the time anyone gets mad about this.
then
	python3 render.py -a -b 29 -l $year-02-29 -o temp-renderyear02.txt
else
	python3 render.py -a -b 28 -l $year-02-28 -o temp-renderyear02.txt
fi

python3 render.py     -a -b 31 -l $year-01-31 -o temp-renderyear01.txt

for month in {1..12}
do
    monthpad=$(printf "%02d" $month)
    python3 upload.py -o User:JPxG/Oracle/$year-$monthpad -i temp-renderyear$monthpad.txt -n "Re-rendering $year-$monthpad."
done

python3 upload.py -o User:JPxG/Oracle/$year -i summary-$year.txt -n "Updating $year."