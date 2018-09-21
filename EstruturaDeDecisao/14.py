aList = []
note1 = float(raw_input("Enter note 1: "))
note2 = float(raw_input("Enter note 2: "))

aList.append(note1)
aList.append(note2)
avg = float(sum(aList)) / max(len(aList), 1)

print "Notes", aList
print "Average", avg

if avg < 4:
	print "Note E - DISAPPROVED"
elif avg < 6:
	print "Note D - DISAPPROVED"
elif avg < 7.5:
	print "Note C - APPROVED"
elif avg < 9:
	print "Note B - APPROVED"
else:
	print "Note A - APPROVED"
	
