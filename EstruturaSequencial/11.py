import math

int1 = raw_input("Enter first integer number: ")
int2 = raw_input("Enter second integer number: ")
real = raw_input("Enter real number: ")

itemA = (float(int1) * 2) * (float(int2) / 2)
itemB = (float(int1) * 3) + float(real)
itemC = math.pow(float(real), 3)

print "Item A is: ", itemA
print "Item B is: ", itemB
print "Item C is: ", itemC