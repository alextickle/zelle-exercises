from random import *
def main():
	print "This program estimates the probability of rolling"
	print "five of a kind with five-sided die."
	hit = 0
	for i in range(100000):
		a = randrange(1, 6, 1)
		b = randrange(1, 6, 1)
		c = randrange(1, 6, 1)
		d = randrange(1, 6, 1)
		e = randrange(1, 6, 1)
		if a == b and b == c and c == d and d == e:
			hit = hit + 1
	print "There were %d hits out of 100,000 rolls." % (hit)
	print "This yields a probability of ~ %0.5f%%." % (hit * 100.0 / 100000)
	
main()
	
	
	
