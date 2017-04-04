from graphics import *
import math
def main():
	win = GraphWin("Please click 5 points to create a house")
	win.setCoords(0,0,10,10)
	p1 = win.getMouse()
	p2 = win.getMouse()
	house = Rectangle(p1,p2)
	house.draw(win)
	lhouse = abs(p1.getX() - p2.getX())
	ldoor = lhouse/5.0
	lwind = ldoor/2.0
	
	p3 = win.getMouse()
	door = Rectangle(p3, Point(p3.getX() - ldoor, p1.getY()))
	door.draw(win)
	
	p4 = win.getMouse()
	wind = Rectangle(Point(p4.getX()-lwind, p4.getY()-lwind,), Point(p4.getX()+lwind, p4.getY()+lwind))
	wind.draw(win)
	
	p5 = win.getMouse()
	roof = Polygon(p2, Point(p1.getX(), p2.getY()), p5)
	roof.draw(win)
	
	win.getMouse()

main()
