import time
from random import *
from graphics import *
from math import *

def main():
	win = GraphWin()
	win.setCoords(-30,-30,30,30)
	a = Point(0,0)
	for i in range(1000):
		angle = random() * 2 * pi
		b = Point(a.getX() + cos(angle), a.getY() + sin(angle))
		c = Line(a, b)
		c.draw(win)
		a = b
		time.sleep(.05)
	
	win.getMouse()
	
main()
	
