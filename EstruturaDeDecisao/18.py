import calendar
import datetime

dtS = raw_input('Enter a date ("dd/mm/yyyy"): ')

dtC = dtS.rsplit('/', 3)
day = int(dtC[0])
mon = int(dtC[1])
year = int(dtC[2])

inv = False
try:
	datetime.datetime(year, mon, day)
except ValueError:
	inv = True

if (inv):
	print("%s is invalid date" % dtS)
else:
	print("%s is valid date" % dtS)