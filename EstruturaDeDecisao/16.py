import math

a = float(raw_input("Enter the coefficient A: "))
b = float(raw_input("Enter the coefficient B: "))
c = float(raw_input("Enter the coefficient C: "))

if (a == 0):
	print "Coefficient A must be greater than zero"
else:
	delta = math.pow(b, 2) - (4 * a * c)
	
	if (delta < 0):
		print "There are no real roots"
	elif (delta == 0):
		print "There are one real root"
		x = -b / (2 * a)
		print "Root:", x
	else:
		print "There are two real roots"
		x1 = (-b + math.sqrt(delta)) / (2 * a)
		x2 = (-b - math.sqrt(delta)) / (2 * a)
		print "Root 1:", x1, "\nRoot 2:", x2