import math

num = float(raw_input('Input a integer number: '))

if (math.fmod(num, 2)):
	print "The number is odd"
else:
	print "The number is even"