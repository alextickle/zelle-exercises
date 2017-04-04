from graphics import *
	
def main():
	win = GraphWin()
	shape = Rectangle(Point(50,50), Point(40,40))
	shape.setOutline("red")
	shape.setFill("red")
	shape.draw(win)
	for i in range(5):
		p = win.getMouse()
		a = Rectangle(p, Point(p.getX() - 10, p.getY() - 10))
		a.setOutline("red")
		a.setFill("red")
		a.draw(win)
	Text(Point(100, 100), "Click to exit").draw(win)
	win.getMouse()
	win.close()

main()
