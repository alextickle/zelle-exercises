from graphics import *

def main():
	win = GraphWin("Click Me!")
	for i in range(3):
		p = win.getMouse()
		print "You clicked (%d, %d)" % (p.getX(), p.getY())

main()
	