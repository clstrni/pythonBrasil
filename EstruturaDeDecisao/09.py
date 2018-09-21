num1 = float(raw_input("Enter a number: "))
num2 = float(raw_input("Enter another number: "))
num3 = float(raw_input("Enter other number: "))
lst = [num1, num2, num3]

print "Numbers sorted:", sorted(lst, reverse=True)