# groupdraw.py
from graphics import *
from classGraphicsGroup import GraphicsGroup

def main():
	win = GraphWin()
	win.setCoords(0,0,100,100)
	a = GraphicsGroup(Point(50,50))
	circ = Circle(Point(40,40), 10)
	circ.setFill("blue")
	circ.setOutline("blue")
	tri = Polygon(Point(35, 35), Point(35, 50), Point(50, 35))
	tri.setFill("red")
	tri.setOutline("red")
	a.addObject(circ)
	a.addObject(tri)
	a.draw(win)
	p = win.getMouse()
	a.move(p.getX() - a.anchor.getX(), p.getY() - a.anchor.getY())
	win.getMouse()
	a.undraw()
	win.getMouse()
	win.close()

main()
	
	
