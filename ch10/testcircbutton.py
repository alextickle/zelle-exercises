from graphics import *
from classCircButton import CircButton

def main():
	win = GraphWin()
	win.setCoords(0,0,10,10)
	a = CircButton(win, Point(5,5), 2, "Click me!")
	a.activate()
	p = win.getMouse()
	while a.clicked(p) == False:
		p = win.getMouse()
	win.getMouse()
	win.close()
main()
