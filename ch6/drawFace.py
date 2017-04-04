from graphics import *

def drawFace(center, size, win):
	win.setCoords(0,0,10,10)
	face = Circle(center, size)
	face.setFill("yellow")
	face.draw(win)
	
	eye1 = Point(center.getX() + 1, center.getY() + 1)
	eye1.draw(win)
	
	eye2 = Point(center.getX() - 1, center.getY() + 1)
	eye2.draw(win)
	
	smile = Line(Point(center.getX() - 2, center.getY() - 2), Point(center.getX() + 2, center.getY() - 2))
	smile.draw(win)

drawFace(Point(5,5), 4, GraphWin())
