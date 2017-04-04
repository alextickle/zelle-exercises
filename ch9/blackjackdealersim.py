from random import *

def main():
	print "This simulations calculates the probability that a dealer will bust given"
	print "a certain initial card."
	print "Ace: %0.0f%%" % (simNHands(1, 100))
	print "Two: %0.0f%%" % (simNHands(2, 100))
	print "Three: %0.0f%%" % (simNHands(3, 100))
	print "Four: %0.0f%%" % (simNHands(4, 100))
	print "Five: %0.0f%%" % (simNHands(5, 100))
	print "Six: %0.0f%%" % (simNHands(6, 100))
	print "Seven: %0.0f%%" % (simNHands(7, 100))
	print "Eight: %0.0f%%" % (simNHands(8, 100))
	print "Nine: %0.0f%%" % (simNHands(9, 100))
	print "Ten, Jack, Queen, or King: %0.0f%%" % (simNHands(10, 100))
	

def simNHands(dealertotal, n):
	hasAce = False
	dealertotal = 0
	draw = 0
	busts = 0
	for i in range(n):
		dealertotal = 0
		while dealertotal < 17:
			draw = randrange(1, 13)
			if draw == 1:
				hasAce = True
			elif draw == 11:
				draw = 10
			elif draw == 12:
				draw = 10
			elif draw == 13:
				draw = 10

			if hasAce == False:
				dealertotal = dealertotal + draw
			else:
				if dealertotal <= 11 and dealertotal >= 7:
					dealertotal = dealertotal + 10
				else:
					dealertotal = dealertotal + draw
		if dealertotal > 21:
			busts = busts + 1
	return busts	
	
main()
