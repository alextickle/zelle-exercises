from graphics import *
from classRegression import Regression

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
	
	r = Regression()
	point = win.getMouse()
	point.draw(win)
	r.addPoint(point)
	while inRect(point) == False:
		point = win.getMouse()
		if inRect(point) == False:
			point.draw(win)
			r.addPoint(point)
	r.update()
	r.drawLine(win)
	r.printPoints()
	x = input("Please enter an x value to predict the y value: ")
	Point(x, r.predict(x)).draw(win)
	print "The predicted y value is", r.predict(x)
	
	
	done.undraw()
	doneRect.undraw()
	win.getMouse()
	win.close()
	
main()
	
