from graphics import *

def main():
	win = GraphWin()
	win.setCoords(0, 0, 10, 10)
	
	Circle(Point(5,5), 3).draw(win)
	Circle(Point(4,6), 0.5).draw(win)
	Circle(Point(6,6), 0.5).draw(win)
	Line(Point(4, 3), Point(6, 3)).draw(win)
	win.getMouse()

main()
