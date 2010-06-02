#!/usr/bin/env python

import time, sqlite3, sys
from datetime import date, datetime, timedelta
from optparse import OptionParser

def main():
	
	parser = OptionParser()
	parser.add_option("-d", "--db", dest="db_file", help="SMS DB File [default: %default]")
	parser.add_option("-s", "--start", dest="starttime", help="DD-MM-YY date to start at [default: %default]")
	parser.add_option("-e", "--end", dest="endtime", help="DD-MM-YY date to end at [default: %default]")
	parser.add_option("-n", "--number", dest="number", help="Phone # to search with - must match AddressBook.app format exactly, in quotes - e.g.: \"(888) 555-1212\"")
	parser.add_option("-c", "--chunksize", dest="chunksize", type="int", help="What size chunk to break the period into, in seconds [default: %default (1 hour = 3600 seconds)]")
	parser.add_option("-o", "--output", dest="output", help="What kind of output format? - Console, CSV, TSV [default: %default]")
	parser.add_option("-D", "--dateformat", dest="dateformat", help="stftime style date format [default: %default] (e.g. 'Wed 11AM')")

	parser.set_defaults(db_file="sms.db")
	parser.set_defaults(starttime=date.strftime(date.today() + timedelta(days=-7), "%d-%m-%y"))
	parser.set_defaults(endtime=date.strftime(date.today(), "%d-%m-%y"))
	parser.set_defaults(chunksize=43200)
	parser.set_defaults(output="Console")
	parser.set_defaults(dateformat="%m/%d/%y - %p")

	(options, args) = parser.parse_args()
	if not options.number:
		print "Missing phone number, option REQUIRED."
		sys.exit(2)

	data = runsearch(options.db_file, options.starttime, options.endtime, options.number, options.chunksize)
	output(data, options.output, options.dateformat)
	sys.exit()
	
def output(data, output, dateformat):

	if (output == "CSV") or (output =="csv"):
		# Pretty print to the console
		printformat = "%s,%s,%s"
	elif (output == "TSV") or (output == "tsv"):
		# Tab seperated
		printformat = "%s\t%s\t%s"
	else:
		#Default to console
		printformat = "Date: %s\t\t In: %s\t\tOut:%s"


	for row in data:
		print printformat % (time.strftime(dateformat, row[0]), row[1], row[2])

def runsearch(dbfile, start, end, number, chunksize):
	conn = sqlite3.connect(dbfile)
	db = conn.cursor()
	
	# SMS DB - flags determine the direction of the message - sent or recieved
	out_query = "SELECT COUNT(*) FROM message WHERE flags='3' AND address=? AND date > ? AND date < ?"
	in_query = "SELECT COUNT(*) FROM message WHERE flags='2' AND address=? AND date > ? AND date < ?"

	# this is convoluted, but it takes the user input "dd-mm-yy" format time stamp, converts it to a unix timestamp.  Python datetime doesn't HAVE a 'totimestamp' capability, 
	# so you have to convert to a time tuple and use the "time" module's mktime() function instead.
	startstamp 	= time.mktime(datetime.strptime(start, "%d-%m-%y").timetuple())
	endstamp 	= time.mktime(datetime.strptime(end, "%d-%m-%y").timetuple())

	results = []
	# converting everything to 'int' to keep xrange happy.
	for x in xrange(int(startstamp), int(endstamp), int(chunksize)):
		outmsg = db.execute(out_query, (number, x, x+int(chunksize-1)))
		a = outmsg.fetchall()[0]
		inmsg = db.execute(in_query, (number, x, x+int(chunksize-1)))
		b = inmsg.fetchall()[0]

		row = [time.gmtime(x), a[0], b[0]]
		results.append(row)
	
	return results


if __name__ == "__main__":
	main()