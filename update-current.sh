# JPxG, 2022 January 1
# A cute little script to update the "current" redirects.

MM=$(date +%m)
YYYY=$(date +%Y)

echo "#redirect [[User:JPxG/Oracle/$YYYY-$MM]]" > data/output/redirect.txt
python3 upload.py -o User:JPxG/Oracle/current -i redirect.txt -n "Updating redirect." -z

rm data/output/redirect.txt