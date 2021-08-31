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
python3 detailpages.py             -v -b 1 -l 2016-04-01 -s 0.01
python3 render.py              -a -v -b 30 -l 2016-04-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2016-04 -i rendertest.txt -n "Attempt to fix single error on 2016-04-21, and 25-error trainwreck on 2016-01-01."

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
python3 upload.py      -v -o User:JPxG/Oracle/2013-07 -i rendertest.txt -n "Use new rendering to attempt error fix in 2013-07-26"
python3 main.py                 -o -v -b 1 -l 2013-07-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-07-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-07-25 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-07 -i rendertest.txt -n "Use new rendering to attempt error fix in 2013-07-25"
python3 main.py                 -o -v -b 1 -l 2013-07-08 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-07-08 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-07-08 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-07 -i rendertest.txt -n "Use new rendering to attempt error fix in 2013-07-08"
python3 main.py                 -o -v -b 1 -l 2013-05-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-05-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-05-25 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-05 -i rendertest.txt -n "Use new rendering to attempt error fix in 2013-05-25"
python3 main.py                 -o -v -b 1 -l 2013-03-18 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-03-18 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-03-18 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-03 -i rendertest.txt -n "Use new rendering to attempt 3 error fixes in 2013-03-18"
python3 main.py                 -o -v -b 1 -l 2013-03-12 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-03-12 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-03-12 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-03 -i rendertest.txt -n "Use new rendering to attempt error fix in 2013-03-12"
python3 main.py                 -o -v -b 1 -l 2013-03-04 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-03-04 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-03-04 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-03 -i rendertest.txt -n "Use new rendering to attempt error fix in 2013-03-04"
python3 main.py                 -o -v -b 1 -l 2013-02-21 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-02-21 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-02-21 -s 0.01
python3 render.py              -a -v -b 28 -l 2013-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-02 -i rendertest.txt -n "Use new rendering to attempt error fix in 2013-02-21"
python3 main.py                 -o -v -b 1 -l 2013-02-18 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-02-18 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-02-18 -s 0.01
python3 render.py              -a -v -b 28 -l 2013-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-02 -i rendertest.txt -n "Use new rendering to attempt 1 error fixes in 2013-02-18"
python3 main.py                 -o -v -b 1 -l 2013-02-05 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-02-05 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-02-05 -s 0.01
python3 render.py              -a -v -b 28 -l 2013-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-02 -i rendertest.txt -n "Use new rendering to attempt error fix in 2013-02-05"
python3 main.py                 -o -v -b 1 -l 2013-01-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-01-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-01-25 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-01 -i rendertest.txt -n "Use new rendering to attempt error fix in 2013-01-25"
python3 main.py                 -o -v -b 1 -l 2013-01-21 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-01-21 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-01-21 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-01 -i rendertest.txt -n "Use new rendering to attempt error fix in 2013-01-21"
python3 main.py                 -o -v -b 1 -l 2013-01-06 -s 0.01
python3 detail.py                  -v -b 1 -l 2013-01-06 -s 0.01
python3 detailpages.py             -v -b 1 -l 2013-01-06 -s 0.01
python3 render.py              -a -v -b 31 -l 2013-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2013-01 -i rendertest.txt -n "Use new rendering to attempt error fix in 2013-01-06"

python3 main.py                 -o -v -b 1 -l 2012-12-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-12-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-12-25 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-12 -i rendertest.txt -n "Use new renderer to attempt to fix 2 errors in 2012-12-25"
python3 main.py                 -o -v -b 1 -l 2012-12-10 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-12-10 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-12-10 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-12 -i rendertest.txt -n "Use new renderer to attempt to fix error in 2012-12-10"
python3 main.py                 -o -v -b 1 -l 2012-12-03 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-12-03 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-12-03 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-12-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-12 -i rendertest.txt -n "Use new renderer to attempt to fix error in 2012-12-03"
python3 main.py                 -o -v -b 1 -l 2012-11-06 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-11-06 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-11-06 -s 0.01
python3 render.py              -a -v -b 30 -l 2012-11-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-11 -i rendertest.txt -n "Use new renderer to attempt to fix error in 2012-11-06"
python3 main.py                 -o -v -b 1 -l 2012-10-19 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-10-19 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-10-19 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-10-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-10 -i rendertest.txt -n "Use new renderer to attempt to fix error in 2012-10-19"
python3 main.py                 -o -v -b 1 -l 2012-08-12 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-08-12 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-08-12 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-08-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-08 -i rendertest.txt -n "Use new renderer to attempt to fix error in 2012-08-12"
python3 main.py                 -o -v -b 1 -l 2012-07-31 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-07-31 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-07-31 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-07 -i rendertest.txt -n "Use new renderer to attempt to fix error in 2012-07-31"
python3 main.py                 -o -v -b 1 -l 2012-07-24 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-07-24 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-07-24 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-07 -i rendertest.txt -n "Use new renderer to attempt to fix error in 2012-07-24"
python3 main.py                 -o -v -b 1 -l 2012-07-21 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-07-21 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-07-21 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-07 -i rendertest.txt -n "Use new renderer to attempt to fix error in 2012-07-21"
python3 main.py                 -o -v -b 1 -l 2012-06-25 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-06-25 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-06-25 -s 0.01
python3 render.py              -a -v -b 30 -l 2012-06-30 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-06 -i rendertest.txt -n "Use new renderer to attempt to fix error in 2012-06-25"
python3 main.py                 -o -v -b 1 -l 2012-05-02 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-05-02 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-05-02 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-05-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-05 -i rendertest.txt -n "Use new renderer to attempt to fix error in 2012-05-02"
python3 main.py                 -o -v -b 1 -l 2012-03-20 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-03-20 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-03-20 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-03 -i rendertest.txt -n "Use new renderer to attempt to fix error in 2012-03-20"
python3 main.py                 -o -v -b 1 -l 2012-02-15 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-02-15 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-02-15 -s 0.01
python3 render.py              -a -v -b 28 -l 2012-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-02 -i rendertest.txt -n "Use new renderer to attempt to fix 3 errors in 2012-02-15"
python3 main.py                 -o -v -b 1 -l 2012-02-03 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-02-03 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-02-03 -s 0.01
python3 render.py              -a -v -b 28 -l 2012-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-02 -i rendertest.txt -n "Use new renderer to attempt to fix error in 2012-02-03"
python3 main.py                 -o -v -b 1 -l 2012-01-15 -s 0.01
python3 detail.py                  -v -b 1 -l 2012-01-15 -s 0.01
python3 detailpages.py             -v -b 1 -l 2012-01-15 -s 0.01
python3 render.py              -a -v -b 31 -l 2012-01-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2012-01 -i rendertest.txt -n "Use new renderer to attempt to fix 4 errors in 2012-01-15"




python3 main.py                 -o -v -b 1 -l 2020-03-23 -s 0.01
python3 detail.py                  -v -b 1 -l 2020-03-23 -s 0.01
python3 detailpages.py             -v -b 1 -l 2020-03-23 -s 0.01
python3 render.py              -a -v -b 31 -l 2020-03-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2020-03 -i rendertest.txt -n "Use new renderer to attempt to fix 1 error in 2020-03-23"

python3 main.py                 -o -v -b 1 -l 2021-02-19 -s 0.01
python3 detail.py                  -v -b 1 -l 2021-02-19 -s 0.01
python3 detailpages.py             -v -b 1 -l 2021-02-19 -s 0.01
python3 render.py              -a -v -b 28 -l 2021-02-28 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2021-02 -i rendertest.txt -n "Use new renderer to attempt to fix 1 error in 2021-02-19"

python3 main.py                 -o -v -b 1 -l 2021-07-17 -s 0.01
python3 detail.py                  -v -b 1 -l 2021-07-17 -s 0.01
python3 detailpages.py             -v -b 1 -l 2021-07-17 -s 0.01
python3 render.py              -a -v -b 31 -l 2021-07-31 -o rendertest.txt
python3 upload.py      -v -o User:JPxG/Oracle/2021-07 -i rendertest.txt -n "Use new renderer to attempt to fix 1 error in 2021-07-17"

