from graphics import *

def main():
	win = GraphWin()
	win.setCoords(0, 0, 10, 10)
	
	tree = Polygon(Point(2,2), Point(5,2), Point(3.5, 5))
	tree.setFill("green")
	tree.setOutline("green")
	tree.draw(win)
	
	trunk = Rectangle(Point(3,2), Point(4,0))
	trunk.setFill("brown")
	trunk.setOutline("brown")
	trunk.draw(win)
	
	snow1 = Circle(Point(7,2), 2)
	snow1.draw(win)
	
	snow2 = Circle(Point(7,5), 1)
	snow2.draw(win)

main()
