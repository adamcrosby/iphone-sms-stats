#iPhone SMS Database stats generator#

##Current Status##
Currently functioning for frequency generation (ie: how many in/out messages for a specific time period for a specific phone number).
This script requires the iphone SMS database to be available, and unencrypted.  By default, this database file is called 

	3d0d7e5fb2ce288813306e4d4636395e047a3d28.mddata

and is located in

	~/Library/Application\ Support/MobileSync/Backup/<phone guid>/
	
on Mac OS X.  

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
	                        [default: 43200 (12 hours)]
	  -o OUTPUT, --output=OUTPUT
	                        What kind of output format? - Console, CSV, TSV
	                        [default: Console]
	  -D DATEFORMAT, --dateformat=DATEFORMAT
	                        stftime style date format [default: %m/%d/%y - %p] (e.g.
	                        '05/29/10 - AM')

###Example Usage###

####Show default chart for a number####

	python lulz.py -n "+18885551212"
	Date: 05/30/10 - AM		 In: 0		Out:0
	Date: 05/30/10 - PM		 In: 12		Out:10
	Date: 05/31/10 - AM		 In: 0		Out:1
	Date: 05/31/10 - PM		 In: 8		Out:4
	Date: 06/01/10 - AM		 In: 9		Out:6
	Date: 06/01/10 - PM		 In: 3		Out:3

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


