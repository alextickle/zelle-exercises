import time
import random
from graphics import *
from math import *

def main():
	win = GraphWin()
	win.setCoords(-10,-10,10,10)
	a = Circle(Point(0,0), .5)
	a.setFill("blue")
	a.setOutline("blue")
	a.draw(win)
	grid = []
	countx = -10
	county = -10
	for i in range(-10, 10, 1):
		grid = grid + [Line(Point(-10, i), Point(10, i))]
		for j in range(-10, 10, 1):
			grid = grid + [Line(Point(j, -10), Point(j, 10))]
	for k in grid:
		k.draw(win)
	xory = [-1,1]
	borf = [-1,1]
	dx, dy = 0, 0
	walked = []
	for i in range(100):
		if random.choice(xory) > 0:
			dx = 0
			if random.choice(borf) > 0:
				dy = 1
			else:
				dy = -1
		else:
			dy = 0
			if random.choice(borf) > 0:
				dx = 1
			else:
				dx = -1
		a.move(dx, dy)
		time.sleep(.25)
		p = Point(a.getCenter().getX(), a.getCenter().getY())
		walked = walked + [p]
	win.getMouse()
	print walked
	
main()
	
