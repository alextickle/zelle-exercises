from graphics import *

def main():
	win = GraphWin()
	win.setCoords(0, 0, 10, 10)
	
	circ1 = Circle(Point(5,5), 3)
	circ1.setFill("blue")
	circ1.setOutline("blue")
	circ1.draw(win)
	
	circ1 = Circle(Point(5,5), 2)
	circ1.setFill("yellow")
	circ1.setOutline("yellow")
	circ1.draw(win)
	
	circ1 = Circle(Point(5,5), 1)
	circ1.setFill("red")
	circ1.setOutline("red")
	circ1.draw(win)

	win.getMouse()

main()
	
