import math

num1 = float(raw_input('Input first number: '))
num2 = float(raw_input('Input second number: '))
ope = raw_input('What operation? (+, -, /, *)\n')

if (num2 != 0):
	if (ope == '+'):
		tot = num1 + num2
	elif (ope == '-'):
		tot = num1 - num2
	elif (ope == '*'):
		tot = num1 * num2
	elif (ope == '/'):
		tot = num1 / num2

	print "Result is", tot
	
	if (math.fmod(tot, 2)):
		print "Even"
	else:
		print "Odd"
		
	if (tot > 0):
		print "Positive"
	else:
		print "Negative"
		
	if (tot.is_integer()):
		print "Integer"
	else:
		print "Float"
else:
	print "Result is zero"