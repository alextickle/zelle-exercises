from graphics import *
import math

def main():
	win = GraphWin()
	win.setCoords(-5, -5, 5, 5)
	
	circ1 = Circle(Point(0,0), 3)
	circ1.setFill("blue")
	circ1.setOutline("blue")
	circ1.draw(win)
	
	circ2 = Circle(Point(0,0), 2)
	circ2.setFill("yellow")
	circ2.setOutline("yellow")
	circ2.draw(win)
	
	circ3 = Circle(Point(0,0), 1)
	circ3.setFill("red")
	circ3.setOutline("red")
	circ3.draw(win)
	
	score = 0
	for i in range(5):
		point = win.getMouse()
		dist = math.sqrt((point.getX())**2 + (point.getY())**2)
		if dist < 1:
			score = score + 3
		elif dist < 2:
			score = score + 2
		elif dist < 3:
			score = score + 1
	print "You scored %d points!" % (score)

main()
	
	
main()
	
