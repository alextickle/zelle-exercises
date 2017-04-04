def main():
	import string
	fname = raw_input("Please enter the filename: ")
	infile = open(fname, "r")
	total = string.split(infile.read())
	words = 0
	for word in total:
		words = words + 1
	print "This file contains %d words." % (words)

main()
