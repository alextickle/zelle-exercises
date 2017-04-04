from graphics import *
import math
def main():
	win = GraphWin("Please click two points to create a line")
	win.setCoords(0,0,10,10)
	p1 = win.getMouse()
	p2 = win.getMouse()
	rect = Rectangle(p1, p2)
	rect.draw(win)
	perimeter = 2*abs(p1.getX() - p2.getX()) + 2*abs(p1.getY() - p2.getY())
	area = (abs(p1.getX() - p2.getX()))*(abs(p1.getY() - p2.getY()))
	print "The perimeter of the rectangle is", perimeter
	print "The area of the rectangle is", area

main()