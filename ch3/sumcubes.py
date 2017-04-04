def main():
	n = input("Please enter a value for n: ")
	sum = 0
	for i in range(n + 1):
		sum = sum + i**3
	print "The sum of the cubes of the first n numbers is", sum

main()