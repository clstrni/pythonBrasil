val = int(raw_input('Service value: '))

if (val > 10) and (val < 601):
	note100 = val / 100
	note50 = (val - (note100 * 100)) / 50
	note10 = (val - (note100 * 100) - (note50 * 50)) / 10
	note5 = (val - (note100 * 100) - (note50 * 50) - (note10 * 10)) / 5
	note1 = val - (note100 * 100) - (note50 * 50) - (note10 * 10) - (note5 * 5)
	
	print 'Notes from 100: {}'.format(note100)
	print 'Notes from 50: {}'.format(note50)
	print 'Notes from 10: {}'.format(note10)
	print 'Notes from 5: {}'.format(note5)
	print 'Notes from 1: {}'.format(note1)
else:
	print "Invalid value"