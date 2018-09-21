oldSal = float(raw_input("Enter the salary: "))

if (oldSal <= 280):
	inc = oldSal * 0.2
	perc = '20%'
elif (oldSal < 700):
	inc = oldSal * 0.15
	perc = '15%'
elif (oldSal < 1500):
	inc = oldSal * 0.1
	perc = '10%'
else:
	inc = oldSal * 0.05
	perc = '5%'
	
sal = oldSal + inc

print "Salary before resetting: R$", oldSal
print "percentage of increase applied:", perc
print "Increase amount: R$", inc
print "New salary: R$", sal