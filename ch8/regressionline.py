from graphics import *

def inRect(point):
	if point.getX() <= 85 and point.getX() >= 55 and point.getY() <= 25 and point.getY() >= 15:
		return True
	else:
		return False

def main():
	win = GraphWin()
	win.setCoords(0,0,100,100)
	done = Text(Point(70, 20), "Done")
	doneRect = Rectangle(Point (55, 15), Point(85, 25))
	done.draw(win)
	doneRect.draw(win)
	point = win.getMouse()
	point.draw(win)
	points = [point]
	while inRect(point) == False:
		point = win.getMouse()
		if inRect(point) == False:
			point.draw(win)
			points = points + [point]
	
	countp = 0
	sumx = 0
	sumy = 0
	for i in points:
		sumx = sumx + i.getX()
		countp = countp + 1.0
	xbar = sumx/countp
	
	for i in points:
		sumy = sumy + i.getY()
	ybar = sumy/countp
	
	mnum = 0
	mdenom = 0
	for i in points:
		mnum = mnum + (i.getX() * i.getY()) - countp * xbar * ybar
		mdenom = mdenom + (i.getX())**2 - (countp * xbar**2) 
	
	m = mnum/mdenom
	
	Line(Point(0, ybar + m * (-xbar)), Point(100, ybar + m * (100 - xbar))).draw(win)
	
	done.undraw()
	doneRect.undraw()
	win.getMouse()
	win.close()
	
main()
	
