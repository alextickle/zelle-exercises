from graphics import *

def moveTo(shape, newCenter):
	shape.move(newCenter.getX() - (shape.getCenter()).getX(), newCenter.getY() - (shape.getCenter()).getY())
	
def main():
	win = GraphWin()
	win.setCoords(0, 0, 10, 10)
	circ = Circle(Point(5,5), 1.5)
	circ.setFill("blue")
	circ.setOutline("blue")
	circ.draw(win)
	
	for i in range(10):
		moveTo(circ, win.getMouse())
	win.close()
	
main()
	
	
	
