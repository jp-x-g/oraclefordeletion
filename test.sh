
bash render-year.sh 2020
bash render-year.sh 2019
bash render-year.sh 2018
bash render-year.sh 2017
bash render-year.sh 2016
bash render-year.sh 2015
bash render-year.sh 2014
bash render-year.sh 2013
bash render-year.sh 2012
bash render-year.sh 2011
bash render-year.sh 2010
bash render-year.sh 2009
bash render-year.sh 2008
bash render-year.sh 2007
bash render-year.sh 2006
bash render-year.sh 2005
bash render-year.sh 2004

python3 main.py                 -o -v -b 1 -l 2002-01-09 -s 0.01
python3 detail.py                  -v -b 1 -l 2002-01-09 -s 0.01
python3 detailpages.py             -v -b 1 -l 2002-01-09 -s 0.01 -z
python3 renderarticles.py       -a -v -b 1 -l 2002-01-09 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/Mypages -i rendertest.txt -n "Update."


python3 main.py                 -o -v -b 1 -i test.txt -s 0.01;python3 detail.py                  -v -b 1 -l 2001-01-01 -s 0.01;python3 detailpages.py             -v -b 1 -l 2001-01-01 -s 0.01 -z;python3 renderarticles.py       -a -v -b 1 -l 2001-01-01 -o rendertest.txt;python3 upload.py      -v -o User:JPxG/Oracle/Largest_AfDs -i rendertest.txt -n "Update with new software."

python3 main.py                 -o -v -b 30 -l 2021-09-30 -s 0.01
python3 detail.py                  -v -b 30 -l 2021-09-30 -s 0.01
python3 detailpages.py             -v -b 30 -l 2021-09-30 -s 0.01
python3 render.py               -a -v -b 30 -l 2021-09-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2021-09 -i rendertest.txt -n "Create page for September 2021."


# test

day=$(date +%d)

if [ "$day" > 20 ]; then
	echo "$day"
fi


python3 main.py                 -o -v -b 1 -l 2021-06-22 -s 0.01
python3 detail.py                  -v -b 1 -l 2021-06-22 -s 0.01
python3 detailpages.py             -v -b 1 -l 2021-06-22 -s 0.01
python3 render.py              -a -v -b 30 -l 2021-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2021-06 -i rendertest.txt -n "Attempt, once again, to fix two of the loathed 'AMPERSAND BUG' for 2021-06-22."


python3 main.py                 -o -v -b 1 -l 2021-06-22 -s 0.01
python3 detail.py                  -v -b 1 -l 2021-06-22 -s 0.01
python3 detailpages.py             -v -b 1 -l 2021-06-22 -s 0.01
python3 render.py              -a -v -b 30 -l 2021-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2021-06 -i rendertest.txt -n "Attempt, once again, to fix two of the loathed 'AMPERSAND BUG' for 2021-06-22."

python3 main.py                 -o -v -b 1 -l 2020-12-13 -s 0.01
python3 detail.py                  -v -b 1 -l 2020-12-13 -s 0.01
python3 detailpages.py             -v -b 1 -l 2020-12-13 -s 0.01
python3 render.py              -a -v -b 31 -l 2020-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2020-12 -i rendertest.txt -n "Attempt to fix AfD boilerplate bug for 2020-12-13."

python3 main.py                 -o -v -b 1 -l 2020-03-11 -s 0.01
python3 detail.py                  -v -b 1 -l 2020-03-11 -s 0.01
python3 detailpages.py             -v -b 1 -l 2020-03-11 -s 0.01
python3 render.py              -a -v -b 31 -l 2020-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2020-03 -i rendertest.txt -n "Attempt to fix the dreaded 'ampersand bug' for 2020-03-11."

python3 main.py                 -o -v -b 1 -l 2020-01-27 -s 0.01
python3 detail.py                  -v -b 1 -l 2020-01-27 -s 0.01
python3 detailpages.py             -v -b 1 -l 2020-01-27 -s 0.01
python3 render.py              -a -v -b 31 -l 2020-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2020-01 -i rendertest.txt -n "Attempt to fix AfD multi-space transclusion bug for 2020-01-27."

python3 main.py                 -o -v -b 1 -l 2019-07-24 -s 0.01
python3 detail.py                  -v -b 1 -l 2019-07-24 -s 0.01
python3 detailpages.py             -v -b 1 -l 2019-07-24 -s 0.01
python3 render.py              -a -v -b 31 -l 2019-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2019-07 -i rendertest.txt -n "Attempt to fix U+200E LEFT-TO-RIGHT MARK bug for 2019-07-24."

python3 main.py                 -o -v -b 1 -l 2019-06-04 -s 0.01
python3 detail.py                  -v -b 1 -l 2019-06-04 -s 0.01
python3 detailpages.py             -v -b 1 -l 2019-06-04 -s 0.01
python3 render.py              -a -v -b 30 -l 2019-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2019-06 -i rendertest.txt -n "Attempt to fix U+200E LEFT-TO-RIGHT MARK bug for 2019-07-24."

python3 main.py                 -o -v -b 1 -l 2019-05-22 -s 0.01
python3 detail.py                  -v -b 1 -l 2019-05-22 -s 0.01
python3 detailpages.py             -v -b 1 -l 2019-05-22 -s 0.01
python3 render.py              -a -v -b 31 -l 2019-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2019-05 -i rendertest.txt -n "Attempt to fix U+200E LEFT-TO-RIGHT MARK bug for 2019-05-22."

python3 main.py                 -o -v -b 1 -l 2018-03-27 -s 0.01
python3 detail.py                  -v -b 1 -l 2018-03-27 -s 0.01
python3 detailpages.py             -v -b 1 -l 2018-03-27 -s 0.01
python3 render.py              -a -v -b 31 -l 2018-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2018-03 -i rendertest.txt -n "Attempt to fix single error on 2018-03-27."

python3 main.py                 -o -v -b 1 -l 2017-12-13 -s 0.01
python3 detail.py                  -v -b 1 -l 2017-12-13 -s 0.01
python3 detailpages.py             -v -b 1 -l 2017-12-13 -s 0.01
python3 main.py                 -o -v -b 1 -l 2017-12-12 -s 0.01
python3 detail.py                  -v -b 1 -l 2017-12-12 -s 0.01
python3 detailpages.py             -v -b 1 -l 2017-12-12 -s 0.01
python3 render.py              -a -v -b 31 -l 2017-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2017-12 -i rendertest.txt -n "Attempt to fix 1 U+200E LEFT-TO-RIGHT MARK bug on 2017-12-13 and one on 2017-12-12."

python3 main.py                 -o -v -b 1 -l 2017-08-17 -s 0.01
python3 detail.py                  -v -b 1 -l 2017-08-17 -s 0.01
python3 detailpages.py             -v -b 1 -l 2017-08-17 -s 0.01
python3 render.py              -a -v -b 31 -l 2017-08-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2017-08 -i rendertest.txt -n "Fix bug from deleted AfD page."

python3 main.py                 -o -v -b 1 -l 2017-05-27 -s 0.01
python3 detail.py                  -v -b 1 -l 2017-05-27 -s 0.01
python3 detailpages.py             -v -b 1 -l 2017-05-27 -s 0.01
python3 render.py              -a -v -b 31 -l 2017-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2017-05 -i rendertest.txt -n "Attempt to fix single error on 2017-05-27."

python3 main.py                 -o -v -b 1 -l 2017-03-13 -s 0.01
python3 detail.py                  -v -b 1 -l 2017-03-13 -s 0.01
python3 detailpages.py             -v -b 1 -l 2017-03-13 -s 0.01
python3 render.py              -a -v -b 31 -l 2017-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2017-03 -i rendertest.txt -n "Attempt to fix single error on 2017-03-13."

python3 main.py                 -o -v -b 1 -l 2016-09-08 -s 0.01
python3 detail.py                  -v -b 1 -l 2016-09-08 -s 0.01
python3 detailpages.py             -v -b 1 -l 2016-09-08 -s 0.01
python3 render.py              -a -v -b 30 -l 2016-09-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2016-09 -i rendertest.txt -n "Attempt to fix single error on 2016-09-08."

python3 main.py                 -o -v -b 1 -l 2016-05-31 -s 0.01
python3 detail.py                  -v -b 1 -l 2016-05-31 -s 0.01
python3 detailpages.py             -v -b 1 -l 2016-05-31 -s 0.01
python3 main.py                 -o -v -b 1 -l 2016-05-29 -s 0.01
python3 detail.py                  -v -b 1 -l 2016-05-29 -s 0.01
python3 detailpages.py             -v -b 1 -l 2016-05-29 -s 0.01
python3 render.py              -a -v -b 31 -l 2016-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2016-05 -i rendertest.txt -n "Attempt to fix single error on 2016-05-31 and one on 2016-05-29."

python3 main.py                 -o -v -b 1 -l 2016-04-21 -s 0.01
python3 detail.py                  -v -b 1 -l 2016-04-21 -s 0.01
python3 detailpages.py             -v -b 1 -l 2016-04-21 -s 0.01
python3 main.py                 -o -v -b 1 -l 2016-04-01 -s 0.01
python3 detail.py                  -v -b 1 -l 2016-04-01 -s 0.01
python3 detailpages.py            -v -b 30 -l 2016-04-30 -s 0.01
python3 render.py              -a -v -b 30 -l 2016-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2016-04 -i rendertest.txt -n "Improved rendering for error sorting (note: the April Fools header has been manually removed from the skeleton json)."

python3 main.py                 -o -v -b 1 -l 2016-02-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2016-02-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2016-02-25 -s 0.01
python3 render.py              -a -v -b 29 -l 2016-02-29 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2016-02 -i rendertest.txt -n "Attempt to fix single error on 2016-02-25 ([[Wikipedia:Articles for deletion/List of English-language euphemisms for profanities]])."

# https://en.wikipedia.org/w/index.php?title=Wikipedia:Articles_for_deletion/Log/2016_May_29&action=edit

python3 main.py                 -o -v -b 1 -l 2015-10-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2015-10-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2015-10-25 -s 0.01
python3 render.py              -a -v -b 31 -l 2015-10-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2015-10 -i rendertest.txt -n "Attempt to fix Unicode error on 2015-10-25."

python3 main.py                 -o -v -b 1 -l 2015-09-29 -s 0.01
python3 detail.py                  -v -b 1 -l 2015-09-29 -s 0.01
python3 detailpages.py             -v -b 1 -l 2015-09-29 -s 0.01
python3 render.py              -a -v -b 30 -l 2015-09-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2015-09 -i rendertest.txt -n "Attempt to fix single error on 2015-10-29."

python3 main.py                 -o -v -b 1 -l 2015-09-29 -s 0.01
python3 detail.py                  -v -b 1 -l 2015-09-29 -s 0.01
python3 detailpages.py             -v -b 1 -l 2015-09-29 -s 0.01
python3 main.py                 -o -v -b 1 -l 2015-09-10 -s 0.01
python3 detail.py                  -v -b 1 -l 2015-09-10 -s 0.01
python3 detailpages.py             -v -b 1 -l 2015-09-10 -s 0.01
python3 render.py              -a -v -b 30 -l 2015-09-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2015-09 -i rendertest.txt -n "Attempt to fix single error on 2015-10-29, and 2 on 2015-09-10."

python3 main.py                 -o -v -b 1 -l 2015-07-17 -s 0.01
python3 detail.py                  -v -b 1 -l 2015-07-17 -s 0.01
python3 detailpages.py             -v -b 1 -l 2015-07-17 -s 0.01
python3 render.py              -a -v -b 31 -l 2015-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2015-07 -i rendertest.txt -n "Attempt to fix the dreaded 'ampersand bug' on 2015-07-17."

python3 main.py                 -o -v -b 1 -l 2015-05-12 -s 0.01
python3 detail.py                  -v -b 1 -l 2015-05-12 -s 0.01
python3 detailpages.py             -v -b 1 -l 2015-05-12 -s 0.01
python3 render.py              -a -v -b 31 -l 2015-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2015-05 -i rendertest.txt -n "Attempt to fix error on 2015-05-12."

python3 main.py                 -o -v -b 1 -l 2015-03-29 -s 0.01
python3 detail.py                  -v -b 1 -l 2015-03-29 -s 0.01
python3 detailpages.py             -v -b 1 -l 2015-03-29 -s 0.01
python3 render.py              -a -v -b 31 -l 2015-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2015-03 -i rendertest.txt -n "Attempt to fix error on 2015-03-29."

python3 main.py                 -o -v -b 1 -l 2014-11-04 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-11-04 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-11-04 -s 0.01
python3 render.py              -a -v -b 30 -l 2014-11-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-11 -i rendertest.txt -n "Attempt to fix render error on 2014-11-04"

python3 main.py                 -o -v -b 1 -l 2014-10-11 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-10-11 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-10-11 -s 0.01
python3 render.py              -a -v -b 31 -l 2014-10-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-10 -i rendertest.txt -n "Attempt to fix two errors (redlinks) on 2014-10-11"

python3 main.py                 -o -v -b 1 -l 2014-10-05 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-10-05 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-10-05 -s 0.01
python3 render.py              -a -v -b 31 -l 2014-10-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-10 -i rendertest.txt -n "Attempt to fix two errors (redlinks) on 2014-10-11, and 1 unicode error on 2014-10-05."


python3 main.py                 -o -v -b 1 -l 2014-09-09 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-09-09 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-09-09 -s 0.01
python3 main.py                 -o -v -b 1 -l 2014-09-08 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-09-08 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-09-08 -s 0.01
python3 main.py                 -o -v -b 1 -l 2014-09-05 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-09-05 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-09-05 -s 0.01
python3 render.py              -a -v -b 30 -l 2014-09-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-09 -i rendertest.txt -n "Fix one error on each of 2014-09-09, 2014-09-08, and 2014-09-05."

python3 main.py                 -o -v -b 1 -l 2014-08-31 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-08-31 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-08-31 -s 0.01
python3 render.py              -a -v -b 31 -l 2014-08-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-08 -i rendertest.txt -n "Attempt to fix three Unicode errors on AfDs on 2014-08-31."

python3 main.py                 -o -v -b 1 -l 2014-07-22 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-07-22 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-07-22 -s 0.01
python3 render.py              -a -v -b 31 -l 2014-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-07 -i rendertest.txt -n "Try to handle bizarre line-break-in-the-middle-of-a-transclusion on 2014-07-22."

python3 main.py                 -o -v -b 1 -l 2014-06-24 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-06-24 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-06-24 -s 0.01
python3 render.py              -a -v -b 30 -l 2014-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-06 -i rendertest.txt -n "Attempt to fix error on 2014-06-24."

python3 main.py                 -o -v -b 1 -l 2014-03-24 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-03-24 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-03-24 -s 0.01
python3 render.py              -a -v -b 30 -l 2014-03-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-03 -i rendertest.txt -n "Attempt to fix error on 2014-03-24."

python3 main.py                 -o -v -b 1 -l 2014-02-28 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-02-28 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-02-28 -s 0.01
python3 render.py              -a -v -b 28 -l 2014-02-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-02 -i rendertest.txt -n "Attempt to fix error on 2014-02-28."

python3 main.py                 -o -v -b 1 -l 2014-01-16 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-01-16 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-01-16 -s 0.01
python3 render.py              -a -v -b 31 -l 2014-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-01 -i rendertest.txt -n "Attempt to fix error on 2014-01-16."

# Redo the fucked-up dates from 2014 10 11.
python3 main.py                 -o -v -b 1 -l 2014-10-11 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-10-11 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-10-11 -s 0.01
python3 render.py              -a -v -b 31 -l 2014-10-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-10 -i rendertest.txt -n "Fix both errors from 2014-10-11 for good this time I hope."


Fix perplexing combination of [[Wikipedia:Articles for deletion/Malaysian Wrestling Federation/Fans]], [[Wikipedia:Articles for deletion/Victory Pro Wrestling]], and [[Wikipedia:Articles for deletion/Top Quality Wrestling]]

python3 render.py              -a -v -b 30 -l 2014-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-04 -i rendertest.txt -n "It seems that Wikipedia won't let the bot upload this page (who knows why)."


2013-07: Mariam Amash (2 nomination), Dudley Persse Joynt‎, List of God of War: Ascension downloadable content‎
2013-05: Plant creatures (Dungeons & Dragons)
2013-03: The Union (professional wrestling) ‎, ShoMiz ‎, Emma and Summer Rae ‎, DickPunks, 2013 Bangladesh Anti-Hindu violence
2013_02: Madura Station, Obamafuscation‎, Fred Krahe, Editing Murder of Brandon Brown
2013-01: Broadvision Perspectives‎, Neil Trevett, Jacek Wiśniewski

python3 main.py                 -o -v -b 1 -l 2014-04-15 -s 0.01
python3 detail.py                  -v -b 1 -l 2014-04-15 -s 0.01
python3 detailpages.py             -v -b 1 -l 2014-04-15 -s 0.01
python3 render.py              -a -v -b 30 -l 2014-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2014-04 -i rendertest.txt -n "Attempt to fix error on 2014-04-15."
python3 main.py                 -o -v -b 1 -l 2013-07-26 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-07-26 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-07-26 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-07 -i rendertest.txt -n "attempt error fix in 2013-07-26"
python3 main.py                 -o -v -b 1 -l 2013-07-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-07-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-07-25 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-07 -i rendertest.txt -n "Use new ampersand-capable rendering to  attempt error fix in 2013-07-25"
python3 main.py                 -o -v -b 1 -l 2013-07-08 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-07-08 -s 0.01
python3 detailpages.py            -v -b 31 -l 2013-07-31 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-07 -i rendertest.txt -n "Improve rendering."
python3 main.py                 -o -v -b 1 -l 2013-05-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-05-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-05-25 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-05 -i rendertest.txt -n "Use new ampersand-capable rendering to  attempt error fix in 2013-05-25"
python3 main.py                 -o -v -b 1 -l 2013-03-18 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-03-18 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-03-18 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-03 -i rendertest.txt -n "Use new ampersand-capable rendering to  attempt 3 error fixes in 2013-03-18"
python3 main.py                 -o -v -b 1 -l 2013-03-12 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-03-12 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-03-12 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-03 -i rendertest.txt -n "Improve linking to unretrievable AfDs"
python3 main.py                 -o -v -b 1 -l 2013-03-04 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-03-04 -s 0.01
python3 detailpages.py            -v -b 31 -l 2013-03-31 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-03 -i rendertest.txt -n "New code that gives more specific information about rendering errors"
python3 main.py                 -o -v -b 1 -l 2013-02-21 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-02-21 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-02-21 -s 0.01
python3 render.py              -a -v -b 28 -l 2013-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-02 -i rendertest.txt -n "New code that gives more specific information about rendering errors"
python3 main.py                 -o -v -b 1 -l 2013-02-18 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-02-18 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-02-18 -s 0.01
python3 render.py              -a -v -b 28 -l 2013-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-02 -i rendertest.txt -n "Use new ampersand-capable rendering to  attempt 1 error fixes in 2013-02-18"
python3 main.py                 -o -v -b 1 -l 2013-02-05 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-02-05 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-02-05 -s 0.01
python3 render.py              -a -v -b 28 -l 2013-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-02 -i rendertest.txt -n "Improve error rendering."
python3 main.py                 -o -v -b 1 -l 2013-01-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-01-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-01-25 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-01 -i rendertest.txt -n "Use new ampersand-capable rendering to  attempt error fix in 2013-01-25"
python3 main.py                 -o -v -b 1 -l 2013-01-21 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-01-21 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-01-21 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-01 -i rendertest.txt -n "Attempt error fix in 2013-01-21"
python3 main.py                 -o -v -b 1 -l 2013-01-06 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-01-06 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-01-06 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-01 -i rendertest.txt -n "Use new ampersand-capable rendering to  attempt error fix in 2013-01-06"

python3 main.py                 -o -v -b 1 -l 2012-12-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-12-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-12-25 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-12 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-12-25"
python3 main.py                 -o -v -b 1 -l 2012-12-10 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-12-10 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-12-10 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-12 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-12-10"
python3 main.py                 -o -v -b 1 -l 2012-12-03 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-12-03 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-12-03 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-12 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-12-03"
python3 main.py                 -o -v -b 1 -l 2012-11-06 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-11-06 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-11-06 -s 0.01
python3 render.py              -a -v -b 30 -l 2012-11-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-11 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-11-06"
python3 main.py                 -o -v -b 1 -l 2012-10-19 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-10-19 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-10-19 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-10-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-10 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-10-19"
python3 main.py                 -o -v -b 1 -l 2012-08-12 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-08-12 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-08-12 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-08-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-08 -i rendertest.txt -n "re-parse of 2012-08-12"
python3 main.py                 -o -v -b 1 -l 2012-07-31 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-07-31 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-07-31 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-07 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-07-31"
python3 main.py                 -o -v -b 1 -l 2012-07-24 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-07-24 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-07-24 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-07 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-07-24"
python3 main.py                 -o -v -b 1 -l 2012-07-21 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-07-21 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-07-21 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-07 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-07-21"
python3 main.py                 -o -v -b 1 -l 2012-06-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-06-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-06-25 -s 0.01
python3 render.py              -a -v -b 30 -l 2012-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-06 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-06-25"
python3 main.py                 -o -v -b 1 -l 2012-05-02 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-05-02 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-05-02 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-05 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-05-02"
python3 main.py                 -o -v -b 1 -l 2012-03-20 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-03-20 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-03-20 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-03 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-03-20"
python3 main.py                 -o -v -b 1 -l 2012-02-15 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-02-15 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-02-15 -s 0.01
python3 render.py              -a -v -b 28 -l 2012-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-02 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-02-15"
python3 main.py                 -o -v -b 1 -l 2012-02-03 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-02-03 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-02-03 -s 0.01
python3 render.py              -a -v -b 28 -l 2012-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-02 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-02-03"
python3 main.py                 -o -v -b 1 -l 2012-01-15 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-01-15 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-01-15 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-01 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2012-01-15"

python3 main.py                 -o -v -b 1 -l 2011-12-04 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-12-04 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-12-04 -s 0.01
python3 render.py              -a -v -b 31 -l 2011-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-12 -i rendertest.txt -n "re-parse of 2011-12-04"
python3 main.py                 -o -v -b 1 -l 2011-12-24 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-12-24 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-12-24 -s 0.01
python3 render.py              -a -v -b 31 -l 2011-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-12 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-12-24"
python3 main.py                 -o -v -b 1 -l 2011-12-20 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-12-20 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-12-20 -s 0.01
python3 render.py              -a -v -b 31 -l 2011-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-12 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-12-20"
python3 main.py                 -o -v -b 1 -l 2011-11-30 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-11-30 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-11-30 -s 0.01
python3 render.py              -a -v -b 30 -l 2011-11-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-11 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-11-30"
python3 main.py                 -o -v -b 1 -l 2011-11-02 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-11-02 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-11-02 -s 0.01
python3 render.py              -a -v -b 30 -l 2011-11-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-11 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-11-02"
python3 main.py                 -o -v -b 1 -l 2011-10-16 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-10-16 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-10-16 -s 0.01
python3 render.py              -a -v -b 31 -l 2011-10-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-10 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-10-16"
python3 main.py                 -o -v -b 1 -l 2011-10-19 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-10-19 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-10-19 -s 0.01
python3 render.py              -a -v -b 31 -l 2011-10-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-10 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-10-19"
python3 main.py                 -o -v -b 1 -l 2011-08-13 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-08-13 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-08-13 -s 0.01
python3 render.py              -a -v -b 31 -l 2011-08-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-08 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-08-13"
python3 main.py                 -o -v -b 1 -l 2011-05-27 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-05-27 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-05-27 -s 0.01
python3 render.py              -a -v -b 31 -l 2011-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-05 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-05-27"
python3 main.py                 -o -v -b 1 -l 2011-05-24 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-05-24 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-05-24 -s 0.01
python3 render.py              -a -v -b 31 -l 2011-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-05 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-05-24"
python3 main.py                 -o -v -b 1 -l 2011-05-16 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-05-16 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-05-16 -s 0.01
python3 render.py              -a -v -b 31 -l 2011-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-05 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-05-16"
python3 main.py                 -o -v -b 1 -l 2011-04-26 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-04-26 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-04-26 -s 0.01
python3 render.py              -a -v -b 30 -l 2011-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-04 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-04-26"
python3 main.py                 -o -v -b 1 -l 2011-04-21 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-04-21 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-04-21 -s 0.01
python3 render.py              -a -v -b 30 -l 2011-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-04 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-04-21"
python3 main.py                 -o -v -b 1 -l 2011-04-14 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-04-14 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-04-14 -s 0.01
python3 render.py              -a -v -b 30 -l 2011-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-04 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-04-14"
python3 main.py                 -o -v -b 1 -l 2011-04-13 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-04-13 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-04-13 -s 0.01
python3 render.py              -a -v -b 30 -l 2011-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-04 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-04-13"

python3 main.py                 -o -v -b 1 -l 2011-03-08 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-03-08 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-03-08 -s 0.01
python3 render.py              -a -v -b 31 -l 2011-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-03 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-03-08"
python3 main.py                 -o -v -b 1 -l 2011-03-05 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-03-05 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-03-05 -s 0.01
python3 render.py              -a -v -b 31 -l 2011-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-03 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-03-05"

python3 main.py                 -o -v -b 1 -l 2011-02-05 -s 0.01
python3 detail.py                  -v -b 1 -l 2011-02-05 -s 0.01
python3 detailpages.py             -v -b 1 -l 2011-02-05 -s 0.01
python3 render.py              -a -v -b 28 -l 2011-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2011-02 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2011-02-05"
python3 main.py                 -o -v -b 1 -l 2010-12-04 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-12-04 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-12-04 -s 0.01
python3 render.py              -a -v -b 31 -l 2010-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-12 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-12-04"
python3 main.py                 -o -v -b 1 -l 2010-12-03 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-12-03 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-12-03 -s 0.01
python3 render.py              -a -v -b 31 -l 2010-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-12 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-12-03"
python3 main.py                 -o -v -b 1 -l 2010-11-13 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-11-13 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-11-13 -s 0.01
python3 render.py              -a -v -b 30 -l 2010-11-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-11 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-11-13"
python3 main.py                 -o -v -b 1 -l 2010-10-22 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-10-22 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-10-22 -s 0.01
python3 render.py              -a -v -b 31 -l 2010-10-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-10 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-10-22"
python3 main.py                 -o -v -b 1 -l 2010-09-23 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-09-23 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-09-23 -s 0.01
python3 render.py              -a -v -b 30 -l 2010-09-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-09 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-09-23"
python3 main.py                 -o -v -b 1 -l 2010-09-01 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-09-01 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-09-01 -s 0.01
python3 render.py              -a -v -b 30 -l 2010-09-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-09 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-09-01"
python3 main.py                 -o -v -b 1 -l 2010-08-27 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-08-27 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-08-27 -s 0.01
python3 render.py              -a -v -b 31 -l 2010-08-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-08 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-08-27"
python3 main.py                 -o -v -b 1 -l 2010-06-17 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-06-17 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-06-17 -s 0.01
python3 render.py              -a -v -b 30 -l 2010-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-06 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-06-17"
python3 main.py                 -o -v -b 1 -l 2010-06-11 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-06-11 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-06-11 -s 0.01
python3 render.py              -a -v -b 30 -l 2010-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-06 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-06-11"
python3 main.py                 -o -v -b 1 -l 2010-06-01 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-06-01 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-06-01 -s 0.01
python3 render.py              -a -v -b 30 -l 2010-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-06 -i rendertest.txt -n "re-parse of 2010-06-01"
python3 main.py                 -o -v -b 1 -l 2010-05-26 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-05-26 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-05-26 -s 0.01
python3 render.py              -a -v -b 31 -l 2010-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-05 -i rendertest.txt -n "Perhaps this will fix it."
python3 main.py                 -o -v -b 1 -l 2010-04-29 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-04-29 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-04-29 -s 0.01
python3 render.py              -a -v -b 30 -l 2010-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-04 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-04-29"
python3 main.py                 -o -v -b 1 -l 2010-04-17 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-04-17 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-04-17 -s 0.01
python3 render.py              -a -v -b 30 -l 2010-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-04 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-04-17"
python3 main.py                 -o -v -b 1 -l 2010-04-10 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-04-10 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-04-10 -s 0.01
python3 render.py              -a -v -b 30 -l 2010-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-04 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-04-10"
python3 main.py                 -o -v -b 1 -l 2010-04-07 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-04-07 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-04-07 -s 0.01
python3 render.py              -a -v -b 30 -l 2010-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-04 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-04-07"
python3 main.py                 -o -v -b 1 -l 2010-03-31 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-03-31 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-03-31 -s 0.01
python3 render.py              -a -v -b 31 -l 2010-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-03 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-03-31"
python3 main.py                 -o -v -b 1 -l 2010-03-20 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-03-20 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-03-20 -s 0.01
python3 render.py              -a -v -b 31 -l 2010-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-03 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-03-20"
python3 main.py                 -o -v -b 1 -l 2010-03-14 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-03-14 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-03-14 -s 0.01
python3 render.py              -a -v -b 31 -l 2010-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-03 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-03-14"
python3 main.py                 -o -v -b 1 -l 2010-03-12 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-03-12 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-03-12 -s 0.01
python3 render.py              -a -v -b 31 -l 2010-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-03 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-03-12"
python3 main.py                 -o -v -b 1 -l 2010-03-09 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-03-09 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-03-09 -s 0.01
python3 render.py              -a -v -b 31 -l 2010-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-03 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-03-09"
python3 main.py                 -o -v -b 1 -l 2010-03-08 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-03-08 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-03-08 -s 0.01
python3 render.py              -a -v -b 31 -l 2010-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-03 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-03-08"
python3 main.py                 -o -v -b 1 -l 2010-02-28 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-02-28 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-02-28 -s 0.01
python3 render.py              -a -v -b 28 -l 2010-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-02 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-02-28"
python3 main.py                 -o -v -b 1 -l 2010-02-09 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-02-09 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-02-09 -s 0.01
python3 render.py              -a -v -b 28 -l 2010-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-02 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-02-09"
python3 main.py                 -o -v -b 1 -l 2010-01-06 -s 0.01
python3 detail.py                  -v -b 1 -l 2010-01-06 -s 0.01
python3 detailpages.py             -v -b 1 -l 2010-01-06 -s 0.01
python3 render.py              -a -v -b 31 -l 2010-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2010-01 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2010-01-06"
python3 main.py                 -o -v -b 1 -l 2009-12-30 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-12-30 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-12-30 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-12 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-12-30"
python3 main.py                 -o -v -b 1 -l 2009-12-06 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-12-06 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-12-06 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-12 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-12-06"
python3 main.py                 -o -v -b 1 -l 2009-12-04 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-12-04 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-12-04 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-12 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-12-04"
python3 main.py                 -o -v -b 1 -l 2009-12-02 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-12-02 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-12-02 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-12 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-12-02"
python3 main.py                 -o -v -b 1 -l 2009-11-29 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-11-29 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-11-29 -s 0.01
python3 render.py              -a -v -b 30 -l 2009-11-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-11 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-11-29"
python3 main.py                 -o -v -b 1 -l 2009-10-22 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-10-22 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-10-22 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-10-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-10 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-10-22"
python3 main.py                 -o -v -b 1 -l 2009-09-07 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-09-07 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-09-07 -s 0.01
python3 render.py              -a -v -b 30 -l 2009-09-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-09 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-09-07"
python3 main.py                 -o -v -b 1 -l 2009-08-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-08-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-08-25 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-08-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-08 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-08-25"
python3 main.py                 -o -v -b 1 -l 2009-08-19 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-08-19 -s 0.01
python3 detailpages.py            -v -b 31 -l 2009-08-31 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-08-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-08 -i rendertest.txt -n "re-propertize of all days and re-render page"
python3 main.py                 -o -v -b 1 -l 2009-07-29 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-07-29 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-07-29 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-07 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-07-29"
python3 main.py                 -o -v -b 1 -l 2009-07-01 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-07-01 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-07-01 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-07 -i rendertest.txt -n "improved error interpretation"
python3 main.py                 -o -v -b 1 -l 2009-06-21 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-06-21 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-06-21 -s 0.01
python3 render.py              -a -v -b 30 -l 2009-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-06 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-06-21"
python3 main.py                 -o -v -b 1 -l 2009-06-17 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-06-17 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-06-17 -s 0.01
python3 render.py              -a -v -b 30 -l 2009-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-06 -i rendertest.txt -n "improved error interpretation"
python3 main.py                 -o -v -b 1 -l 2009-06-05 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-06-05 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-06-05 -s 0.01
python3 render.py              -a -v -b 30 -l 2009-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-06 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-06-05"
python3 main.py                 -o -v -b 1 -l 2009-06-04 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-06-04 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-06-04 -s 0.01
python3 render.py              -a -v -b 30 -l 2009-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-06 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-06-04"
python3 main.py                 -o -v -b 1 -l 2009-06-02 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-06-02 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-06-02 -s 0.01
python3 render.py              -a -v -b 30 -l 2009-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-06 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-06-02"
python3 main.py                 -o -v -b 1 -l 2009-05-27 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-05-27 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-05-27 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-12 -i rendertest.txt -n "improved error interpretation"
python3 render.py              -a -v -b 30 -l 2009-11-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-11 -i rendertest.txt -n "improved error interpretation"
python3 render.py              -a -v -b 31 -l 2009-10-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-10 -i rendertest.txt -n "improved error interpretation"
python3 render.py              -a -v -b 30 -l 2009-09-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-09 -i rendertest.txt -n "improved error interpretation"
python3 render.py              -a -v -b 31 -l 2009-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-07 -i rendertest.txt -n "improved error interpretation"
python3 render.py              -a -v -b 30 -l 2009-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-06 -i rendertest.txt -n "improved error interpretation"
python3 render.py              -a -v -b 31 -l 2009-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-05 -i rendertest.txt -n "improved error interpretation"
python3 render.py              -a -v -b 31 -l 2009-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-03 -i rendertest.txt -n "improved error interpretation"
python3 render.py              -a -v -b 28 -l 2009-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-02 -i rendertest.txt -n "improved error interpretation"
python3 render.py              -a -v -b 31 -l 2009-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-01 -i rendertest.txt -n "improved error interpretation"
python3 main.py                 -o -v -b 1 -l 2009-05-04 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-05-04 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-05-04 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-05 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-05-04"
python3 main.py                 -o -v -b 1 -l 2009-04-04 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-04-04 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-04-04 -s 0.01
python3 render.py              -a -v -b 30 -l 2009-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-04 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-04-04"
python3 main.py                 -o -v -b 1 -l 2009-04-03 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-04-03 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-04-03 -s 0.01
python3 render.py              -a -v -b 30 -l 2009-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-04 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-04-03"
python3 main.py                 -o -v -b 1 -l 2009-03-21 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-03-21 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-03-21 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-03 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-03-21"
python3 main.py                 -o -v -b 1 -l 2009-03-17 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-03-17 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-03-17 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-03 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-03-17"
python3 main.py                 -o -v -b 1 -l 2009-02-24 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-02-24 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-02-24 -s 0.01
python3 render.py              -a -v -b 28 -l 2009-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-02 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-02-24"
python3 main.py                 -o -v -b 1 -l 2009-02-15 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-02-15 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-02-15 -s 0.01
python3 render.py              -a -v -b 28 -l 2009-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-02 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-02-15"
python3 main.py                 -o -v -b 1 -l 2009-01-29 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-01-29 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-01-29 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-01 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-01-29"
python3 main.py                 -o -v -b 1 -l 2009-01-20 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-01-20 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-01-20 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-01 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-01-20"
python3 main.py                 -o -v -b 1 -l 2009-01-17 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-01-17 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-01-17 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-01 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-01-17"
python3 main.py                 -o -v -b 1 -l 2009-01-09 -s 0.01
python3 detail.py                  -v -b 1 -l 2009-01-09 -s 0.01
python3 detailpages.py             -v -b 1 -l 2009-01-09 -s 0.01
python3 render.py              -a -v -b 31 -l 2009-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2009-01 -i rendertest.txt -n "Use improved parsing, and improved error interpretation, for entire month as well as specific re-parse of 2009-01-09"


