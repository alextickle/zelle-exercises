from graphics import *

def main():
	win = GraphWin("Chimp", 500, 500)
	win.setCoords(0, 0, 10, 10)
	Image(Point(5,5), chimp.jpeg).draw(win)
	win.getMouse()
	
main()
	

	
