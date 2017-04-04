from random import randrange
from graphics import GraphWin, Point

from classButton import Button
from DieViewColor import DieViewColor

def main():
	win = GraphWin("Dice Roller")
	win.setCoords(0, 0, 10, 10)
	win.setBackground("green2")
	
	die1 = DieViewColor(win, Point(3, 7), 2)
	die2 = DieViewColor(win, Point(7,7), 2)
	die1.setColor('blue')
	die2.setColor('red')
	rollButton = Button(win, Point(5,4.5), 6, 1, "Roll Dice")
	rollButton.activate()
	quitButton = Button(win, Point(5,1), 2, 1, "Quit")
	
	pt = win.getMouse()
	while not quitButton.clicked(pt):
		if rollButton.clicked(pt):
			value1 = randrange(1,7)
			die1.setValue(value1)
			value2 = randrange(1,7)
			die2.setValue(value2)
			quitButton.activate()
		pt = win.getMouse()
		
	win.close()

main()
