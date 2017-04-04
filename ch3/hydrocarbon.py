def main():
	h = input("Please enter the number of hydrogen atoms: ")
	c = input("Please enter the number of carbon atoms: ")
	o = input("Please enter the number of oxygen atoms: ")
	w = 1.0079 * h + 12.011 * c + 15.9994 * o
	print "The total weight of the molecule is", w

main()