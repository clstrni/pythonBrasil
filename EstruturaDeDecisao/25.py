count = 0
qst1 = raw_input('Did you call the victim? (y/n)\n').lower()
qst2 = raw_input('Were you at the crime scene? (y/n)\n').lower()
qst3 = raw_input('Do you live near the victim? (y/n)\n').lower()
qst4 = raw_input('Did you owe to the victim? (y/n)\n').lower()
qst5 = raw_input('Have you worked with the victim? (y/n)\n').lower()


if (qst1 == 'y'):
	count += 1

if (qst2 == 'y'):
	count += 1

if (qst3 == 'y'):
	count += 1

if (qst4 == 'y'):
	count += 1

if (qst5 == 'y'):
	count += 1
	
if (count == 5):
	print 'Murderer'
elif (count > 2):
	print 'Accomplice'
elif (count == 2):
	print 'Suspect'
else:
	print 'Innocent'