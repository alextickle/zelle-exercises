from graphics import *
import math
def main():
	win = GraphWin("Please click three points to create a triangle")
	win.setCoords(0,0,10,10)
	p1 = win.getMouse()
	p2 = win.getMouse()
	p3 = win.getMouse()
	tri = Polygon(p1, p2, p3)
	tri.draw(win)
	l1 = math.sqrt((p1.getX() -p2.getX())**2 + (p1.getY() - p2.getY())**2)
	l2 = math.sqrt((p2.getX() -p3.getX())**2 + (p2.getY() - p3.getY())**2)
	l3 = math.sqrt((p1.getX() -p3.getX())**2 + (p1.getY() - p3.getY())**2)
	per = l1 + l2 + l3
	s = per/2
	area = math.sqrt(s*(s-l1)*(s-l2)*(s-l3))
	print "The area of the triangle is", area

main()