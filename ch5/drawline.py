from graphics import *
import math
def main():
	win = GraphWin("Please click two points to create a line")
	win.setCoords(0,0,10,10)
	p1 = win.getMouse()
	p2 = win.getMouse()
	l = Line(p1, p2)
	l.draw(win)
	mp = Point((p1.getX() + p2.getX())/2.0, (p1.getY() + p2.getY())/2.0)
	mp.setFill("cyan")
	mp.draw(win)
	
	slope = (p2.getX() - p1.getX())/(p2.getY() - p1.getY())
	length = math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)
	print "The slope of the line is", slope
	print "The length of the line is", length

main()