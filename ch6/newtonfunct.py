import math

def nextGuess(guess, x):
	return (guess + (x/guess))/2.0

def main():
	x = input("Enter a number to guess the square root of: ")
	n = input("Enter the number of times to guess: ")
	guess = x/2.0
	for i in range(n):
		guess = nextGuess(guess, x)
		
	print "The final guess is %0.2f, and it is off by %0.2f." % (guess, abs(math.sqrt(x) - guess))

main()
