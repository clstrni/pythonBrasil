straw = float(raw_input('Amount of strawberry (Kg): '))
apple = float(raw_input('Amount of Apple(Kg): '))

if (straw <= 5):
	totStraw = straw * 2.5
else:
	totStraw = straw * 2.2

if (apple <= 5):
	totApple = apple * 2.5
else:
	totApple = apple * 2.2
	
total = totApple + totStraw
	
if ((straw + apple) > 8) or (total > 25):
	total *= 0.9
	
print "Total to pay: R$", total