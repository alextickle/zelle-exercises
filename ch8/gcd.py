def main():
	m, n = input("Please enter two numbers, separated by a comma.")
	while m != 0:
		n, m = m, n%m
	print "The greatest common denominator is ", n

main()