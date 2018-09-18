import math

size = float(raw_input("Area to be painted (m2): "))
liter = (size / 6) * 1.1
tupC = math.modf(liter / 18)
tupG = math.modf(liter / 3.6)

qttC = tupC[1]
if (tupC[0] > 0):
	qttC += 1

qttG = tupG[1]
if (tupG[0] > 0):
	qttG += 1
	
mix = int((liter - (tupC[1] * 18)) / 3.6)
if ((liter - (tupC[1] * 18) % 3.6 != 0)):
	mix += 1
	
print "Quantity of cans: ", qttC
print "Total price per can: ", qttC * 80
print "\nQuantity of gallons: ", qttG
print "Total price per gallon: ", qttG * 25
print "\nCans:", tupC[1], "and gallons", float(mix),". Total:", (tupC[1] * 80) + (mix * 25)