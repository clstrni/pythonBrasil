beef = int(raw_input("Choose your beef:\n1 - Double Fillet\n2 - Rump\n3 - Filet Steak\n"))
pound = float(raw_input("Input the pound: "))
card = int(raw_input("Payment:\n1 - Card Tabajara\n2 - Another\n"))

if (beef == 1):
	if (pound <= 5):
		total = pound * 4.9
	else:
		total = pound * 5.8
	print "Double Fillet - %f Kg" % (pound)
elif (beef == 2):
	if (pound <= 5):
		total = pound * 5.9
	else:
		total = pound * 6.8
	print "Rump - %f Kg" % (pound)
elif (beef == 3):
	if (pound <= 5):
		total = pound * 6.9
	else:
		total = pound * 7.8
	print "Filet Steak - %f Kg" % (pound)
	
print "Total price: R$%f" % (total)

if (card == 1):
	print "Payment by Card Tabajara"
	desc = total * 0.05
	print "Discount: R$%f" % (desc)
else:
	print "Payment by Another"
	desc = 0
	
print "Total to pay: R$%f" % (total - desc)