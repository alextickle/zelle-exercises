def sumN(n):
	sum = 0
	for i in range(1, n + 1, 1):
		sum = sum + i
	return sum

def sumNcubes(n):
	sum = 0
	for i in range(1, n + 1, 1):
		sum = sum + i**3
	return sum

def main():
	n = input("Please choose a value for n: ")
	print "The sum of the first n natural"
	print "numbers is %d, and the sum of the" % (sumN(n))
	print "cubes of the first n natural numbers"
	print "is %d." % (sumNcubes(n))

main()