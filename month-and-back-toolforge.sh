# Fetches the whole current month, and also goes 31 days back.
# Renders and uploads the resultant month page, and master dashboard.
# JPxG, 2021 November 26

backby=$1


DAYS=$(cal $(date +"%m %Y") | awk 'NF {DAYS = $NF}; END {print DAYS}')
# Days of the current month. Props to sleeplessbeastie.eu who came up with this

DD=$(date +%d)
MM=$(date +%m)
YYYY=$(date +%Y)


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
python3 detail.py               -q -v -b $goback -l $YYYY-$MM-$DAYS -s 0.01 -o enwiki.analytics.db.svc.wikimedia.cloud
python3 detailpages.py             -v -b $goback -l $YYYY-$MM-$DAYS -s 0.01
cp tmp/tmp.txt tmp/tmp2.txt

python3 render.py               -a -v -b $DAYS   -l $YYYY-$MM-$DAYS -o render.txt
python3 upload.py     			   -v -o User:JPxG/Oracle/$YYYY-$MM -n "Updating from Toolforge."
# Render and upload the monthly page.

mv tmp/tmp2.txt tmp/tmp.txt
python3 render.py                  -v -b $DAYS   -l $YYYY-$MM-$DD   -o render.txt
python3 upload.py     			   -v -o User:JPxG/Oracle -n "Updating with Toolforge."
# Render and upload the dashboard


#python3 detail.py                  -v -b 1 -l 2014-10-05 -s 0.01
#python3 detailpages.py             -v -b 1 -l 2014-10-05 -s 0.01
#python3 render.py              -a -v -b 31 -l 2014-10-31 -o render.txt
#python3 upload.py      -v -o User:JPxG/Oracle/2014-10 -i render.txt -n "Attempt to fix two errors (redlinks) on 2014-10-11, and 1 unicode error on 2014-10-05."

#[x@localhost afd]$ bash run-batch.sh -w 1 -b 31 -s 0.01 -o User:JPxG/Oracle -q 1
#[x@localhost afd]$ bash run-batch.sh -w 1 -g 1 -b 30 -l 2021-11-30 -v 1 -s 0.01 -o User:JPxG/Oracle/2021-11 -q 1
