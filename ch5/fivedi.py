from graphics import *

def main():
	win = GraphWin()
	win.setCoords(0,0,100,100)
	
	die1 = Rectangle(Point(15,30), Point(25, 15))
	die1.draw(win)
	
	die2 = die1.clone()
	die2.draw(win)
	die2.move(30,0)
	
	die3 = die1.clone()
	die3.draw(win)
	die3.move(60,0)
	
	die4 = die1.clone()
	die4.draw(win)
	die4.move(0,50)
	
	die5 = die1.clone()
	die5.draw(win)
	die5.move(30,50)
	
	die6 = die1.clone()
	die6.draw(win)
	die6.move(60,50)
	
	win.getMouse()

main()
	
	
	
