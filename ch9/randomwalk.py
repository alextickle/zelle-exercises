from random import *

def main():
	location = 0
	n = input("Please enter a value for n: ")
	deviations = 0
	a = [-1, 1]
	for i in range(n):
		for i in range(1000):
			step = choice(a)
			location = location + step
		deviations = deviations + location
	print "The average number of steps from start is %f." % (float(deviations)/n)
	
main()
	
