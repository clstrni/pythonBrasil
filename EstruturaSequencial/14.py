wei = raw_input("Enter the weight of the fish: ")

if float(wei) > 50:
	exc = float(wei) - 50
	mul = exc * 4
	print "Weight exceeded: %f\n Fine: %f" % (exc, mul)
else:
	print "Weight is good!"