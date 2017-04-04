def main():
	import math
	x = input("Enter a number to guess the square root of: ")
	n = input("Enter the number of times to guess: ")
	guess = x/2.0
	for i in range(n):
		guess = (guess + (x/guess))/2
	print "The final guess is %0.2f, and it is off by %0.2f." % (guess, abs(math.sqrt(x) - guess))

main()