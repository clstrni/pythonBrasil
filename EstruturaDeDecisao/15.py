sd1 = float(raw_input("Side one: "))
sd2 = float(raw_input("side two: "))
sd3 = float(raw_input("Side three: "))
sum1 = sd1 + sd2
sum2 = sd2 + sd3

if (sum1 < sd3) or (sum2 < sd1):
	print "Invalid values!"
else:
	if (sd1 == sd2 == sd3):
		print "Equilateral triangle"
	elif (sd1 == sd2 != sd3) or (sd1 != sd2 == sd3):
		print "Isosceles triangle"
	elif (sd1 != sd2 != sd3):
		print "Scalene triangle"