#iPhone SMS Database stats generator#

##Current Status##
Currently functioning for frequency generation (ie: how many in/out messages for a specific time period for a specific phone number).

##Usage##
Options:
	  -h, --help            show this help message and exit
	  -d DB_FILE, --db=DB_FILE
	                        SMS DB File [default: sms.db]
	  -s STARTTIME, --start=STARTTIME
	                        DD-MM-YY date to start at [default: 26-05-10]
	  -e ENDTIME, --end=ENDTIME
	                        DD-MM-YY date to end at [default: 02-06-10]
	  -n NUMBER, --number=NUMBER
	                        Phone # to search with - must match AddressBook.app
	                        format exactly, in quotes - e.g.: "(888) 555-1212"
	  -c CHUNKSIZE, --chunksize=CHUNKSIZE
	                        What size chunk to break the period into, in seconds
	                        [default: 3600 (1 hour = 3600 seconds)]
	  -o OUTPUT, --output=OUTPUT
	                        What kind of output format? - Console, CSV, TSV
	                        [default: Console]
	  -D DATEFORMAT, --dateformat=DATEFORMAT
	                        stftime style date format [default: %a %I%p] (e.g.
	                        'Wed 11AM')

###Example Usage###

####Show default chart for a number####

	python lulz.py -n "+18885551212"
	Date: 10/05/30 - AM		 In: 0		Out:1
	Date: 10/05/30 - PM		 In: 79		Out:90
	Date: 10/05/31 - AM		 In: 47		Out:29
	Date: 10/05/31 - PM		 In: 44		Out:41
	Date: 10/06/01 - AM		 In: 4		Out:7
	Date: 10/06/01 - PM		 In: 30		Out:29

####Show same number, but with chart broken into 1 hr chunks instead of 12 hour, with a timestamp change####
	python lulz.py -n "+18885551212" -c 3600 --dateformat "%y/%m/%d %I%p"
	Date: 10/05/30 08PM		 In: 0		Out:0
	Date: 10/05/30 09PM		 In: 32		Out:28
	Date: 10/05/30 10PM		 In: 9		Out:15
	Date: 10/05/30 11PM		 In: 2		Out:0
	Date: 10/05/31 12AM		 In: 24		Out:29
	Date: 10/05/31 01AM		 In: 12		Out:18
	Date: 10/05/31 02AM		 In: 0		Out:0
	Date: 10/05/31 03AM		 In: 0		Out:0
	Date: 10/05/31 04AM		 In: 0		Out:0


