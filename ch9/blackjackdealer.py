from random import *

def main():
	n = 5
	hasAce = False
	dealertotal = 0
	draw = 0
	busts = 0
	for i in range(n):
		print
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
			print draw, dealertotal
		if dealertotal > 21:
			busts = busts + 1
	print "The dealer busted %d times in %d hands (%0.0f%%)" % (busts, n, float(busts)/n * 100) 
	
main()
