pay = float(raw_input("How much is your hourly payment?\n "))
hours = float(raw_input("How many hours do you work per month?\n "))
basic = pay * hours
hasIR = True

if (basic > 2500):
	ir = basic * 0.2
	perc = '20%'
elif (basic > 1500):
	ir = basic * 0.1
	perc = '10%'
elif (basic > 900):
	ir = basic * 0.05
	perc = '5%'
else:
	hasIR = False

inss = basic * 0.1
synd = basic * 0.03
fgts = basic * 0.11
disc = ir + inss + synd
net = basic - disc

print "Basic salary: R$", basic
print "(-) IR (", perc, "): R$", ir
print "(-) INSS (10%): R$", inss
print "(-) Syndicate (3%): R$", synd
print "FGTS (11%): R$", fgts
print "Total discounts: R$", disc
print "= Net salary: R$", net