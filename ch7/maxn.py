def main():
	n = input("How many numbers are there? ")
	max = input("Enter a number >> ")
	for i in range(n - 1):
		x = input("Enter a number >> ")
		if x > max:
			max = x
	print "The largest value is", max

main()