# JPxG, 2022 January 1
# This runs render-year.sh for the current year.
# If it's January, runs it for the previous year as well.


MM=$(date +%m)
YYYY=$(date +%Y)
YYYX=$(($YYYY - 1))

bash render-year.sh $YYYY

if [ $MM \< 2 ]; then
	bash render-year.sh $YYYX
fi