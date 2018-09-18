sex = raw_input("What's your sex? (M (male) / F (female))\n")
hei = raw_input("Enter the height: ")

if (sex == "M"):
	ideal = 72.7 * float(hei) - 58
else:
	ideal = 62.1 * float(hei) - 44.7
	
print "Ideal weight is: ", ideal