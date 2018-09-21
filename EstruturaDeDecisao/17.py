import calendar

year = int(raw_input("Report the year: "))

if (calendar.isleap(year)):
	print "Leap year"
else:
	print "No leap year"