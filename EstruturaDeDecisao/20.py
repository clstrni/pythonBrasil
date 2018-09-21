aList = []
note1 = float(raw_input("Enter note 1: "))
note2 = float(raw_input("Enter note 2: "))
note3 = float(raw_input("Enter note 3: "))

aList.append(note1)
aList.append(note2)
avg = float(sum(aList)) / max(len(aList), 1)

if avg == 10:
	print "Note %f\nStudent approved with Distinction!" % (avg)
elif avg >= 7:
	print "Note %f\nStudent approved!" % (avg)
else:
	print "Note %f\nStudent disapproved!" % (avg)