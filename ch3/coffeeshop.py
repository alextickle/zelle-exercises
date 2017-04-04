# coffeeshop.py
def main():
	lbs = input("How many pounds of coffee would you like? ")
	cost = 0.86 * lbs + 1.50
	print "The total cost of %d lbs of coffee will be %0.2f." % (lbs, cost)

main()
	