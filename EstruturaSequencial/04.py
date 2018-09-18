aList = []
num1 = raw_input("Enter your first number: ")
num2 = raw_input("Enter your second number: ")
num3 = raw_input("Enter your third number: ")
num4 = raw_input("Enter your fourth number: ")

aList.append(float(num1))
aList.append(float(num2))
aList.append(float(num3))
aList.append(float(num4))
avg = float(sum(aList)) / max(len(aList), 1)

print "The average is: ", avg