import math

size = float(raw_input("Area to be painted (m2): "))
liter = size / 3
tup = math.modf(liter / 18)

if (tup[0] == '0.0'):
	qtt = tup[1]
else:
	qtt = tup[1] + 1
	
print "Quantity of cans: ", qtt
print "Total price: ", qtt * 80