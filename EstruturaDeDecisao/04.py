let = raw_input("Enter a letter: ").lower()
lst = ['a', 'e', 'i', 'o', 'u']

if (lst.count(let) > 0):
	print "Letter is vowel!"
else:
	print "Letter is consonant!"