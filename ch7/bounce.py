from graphics import *
import math
from time import sleep

def main():
	win = GraphWin()
	win.setCoords(-1000, -1000, 1000, 1000)
	
	circ = Circle(Point(0,0), 100)
	circ.setFill("blue")
	circ.setOutline("blue")
	circ.draw(win)
	
	dx = 15
	dy = 3
	for i in range(10000):
		if (circ.getCenter()).getX() >= 1000 or (circ.getCenter()).getX() <= -1000:
			dx = -dx
		if (circ.getCenter()).getY() >= 1000 or (circ.getCenter()).getY() <= -1000:
			dy = -dy
		circ.move(dx, dy)
		sleep(0.005)

main()
		
	
	
	
