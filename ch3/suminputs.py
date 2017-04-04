def main():
	n = input("Please enter the number of numbers to sum: ")
	sum = 0
	for i in range(n):
		a = input("Please enter the number: ")
		sum = sum + a
	print "The sum of these numbers is", sum

main()