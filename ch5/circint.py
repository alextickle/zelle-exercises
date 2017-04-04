from graphics import *
import math

def main():
	r = input("Please enter the radius of the circle: ")
	yint = input("Please enter the y intercept of the line: ")
	
	win = GraphWin()
	win.setCoords(-10, -10, 10, 10)
	circ = Circle(Point(0,0), r)
	circ.draw(win)
	l = Line(Point(-10, yint), Point(10, yint))
	l.draw(win)
	
	p1 = Point(math.sqrt(r**2 - yint**2), yint)
	p2 = Point(-(math.sqrt(r**2 - yint**2)), yint)
	p1.setFill("red")
	p2.setFill("red")
	p1.draw(win)
	p2.draw(win)
	
	print "The two points of intersection are (%0.2f, %d) and (%0.2f, %d)." % (p1.getX(), yint, p2.getX(), yint)

main()