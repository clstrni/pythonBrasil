aList = []
note1 = float(raw_input("Enter note 1: "))
note2 = float(raw_input("Enter note 2: "))

aList.append(note1)
aList.append(note2)
avg = float(sum(aList)) / max(len(aList), 1)

if avg == 10:
	print "Student approved with Distinction!"
elif avg >= 7:
	print "Student approved!"
else:
	print "Student disapproved!"