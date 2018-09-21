liters = float(raw_input('How many liters?\n'))
fuel = raw_input('Type of fuel: (A-ethanol, G-gasoline)\n').upper()

if (fuel == 'A'):
	tot = liters * 1.9
elif (fuel == 'G'):
	tot = liters * 2.5
	
print "Amount to pay R$%f" % (tot)