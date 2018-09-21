let = raw_input("Shift M-morning ou V-afternoon ou N-evening: ").upper()

if (let == 'M'):
	print "Good morning!"
elif (let == 'V'):
	print "Good afternoon!"
elif (let == 'N'):
	print "Good evening!"
else:
	print "Invalid value!"