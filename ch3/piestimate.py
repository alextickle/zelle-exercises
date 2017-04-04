# piestimate.py
import math
def main():
	n = input("Please enter a value for n: ")
	pi = 0
	for i in range(n):
		if i % 2 == 0:
			pi = pi + 4/(2.0*i + 1)
		else:
			pi = pi - 4/(2.0*i + 1)
	print "Your estimate is %0.4f This is off by %0.4f." % (pi, abs(pi - math.pi))

main()
