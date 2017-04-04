def main():
	n = input("Please enter a value for n: ")
	sum = 0
	for i in range(n + 1):
		sum = sum + i
	print "The sum of the first %d numbers is %d." % (n, sum)

main()
	