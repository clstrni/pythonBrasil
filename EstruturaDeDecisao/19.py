num = raw_input('Enter a number less than 1000: ')
tst = int(num)

if (tst < 1000):
	aLen = len(num)
	
	if (aLen == 3):
		hun = int(num[0:1])
		ten = int(num[1:2])
		uni = int(num[2:])
		hunS = 'hundred'
		tenS = 'ten'
		uniS = 'unit'
		
		if (hun > 1):
			hunS = 'hundreds'
		
		if (ten > 1):
			tenS = 'tens'
		
		if (uni > 1):
			uniS = 'units'
		
		print '%s = %i %s, %i %s e %i %s' % (num, hun, hunS, ten, tenS, uni, uniS)
else:
	print "Invalid input number"