from graphics import *
from classTracker import Tracker

def main():
	win = GraphWin()
	win.setCoords(0,0,10,10)
	c = Point(3,3)
	c.draw(win)
	d = Tracker(win, c)
	for i in range(5):
		a = win.getMouse()
		c.move(a.getX() - c.getX(), a.getY() - c.getY())
		d.update(c)
	win.close()

main()
		
