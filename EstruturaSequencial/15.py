pay = raw_input("How much is your hourly payment?\n ")
hours = raw_input("How many hours you work in the month?\n ")
basic = float(pay) * float(hours)
ir = basic * 0.11
inss = basic * 0.08
synd = basic * 0.05
net = basic - ir - inss - synd

print "+ Basic salary: R$", basic
print "- IR (11%): R$", ir
print "- INSS (8%): R$", inss
print "- Syndicate (5%): R$", synd
print "= Net salary: R$", net