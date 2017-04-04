def main():
	q = input("Enter the number of quarters: ")
	d = input("Dimes: ")
	n = input("Nickels: ")
	p = input("Pennies: ")
	total = (25*q + 10*d + 5*n + p)/100.0
	print "You have a total of %$0.2f." % (total)

main()
