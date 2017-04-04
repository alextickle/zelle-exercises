from graphics import *
from random import *

def main():
	print "This program uses Monte Carlo techniques to estimate pi."
	win = GraphWin()
	win.setCoords(-1,-1,1,1)
	target = Circle(Point(0,0), 1)
	target.setFill('red')
	target.draw(win)
	
	n = input("Enter the number of darts to throw: ")
	hits = 0
	for i in range(n):
		randpoint = Point(2 * random() -1, 2 * random() - 1)
		randpoint.draw(win)
		if (randpoint.getX())**2 + (randpoint.getY())**2 <= 1:
			hits = hits + 1
			randpoint.setFill('yellow')
	print "The estimate for the value of pi is %0.4f" % ((4.0000 * hits)/n)

main()
		
	
