from classButton import Button
from graphics import *
from random import *

def main():
	win = GraphWin("Three Button Monty")
	win.setCoords(0,0,20,20)
	a = Button(win, Point(3, 10), 4, 10, "A")
	a.activate()
	
	b = Button(win, Point(10, 10), 4, 10, "B")
	b.activate()
	
	c = Button(win, Point(17, 10), 4, 10, "C")
	c.activate()
	
	header = Text(Point(10, 19), "Pick a door!")
	header.draw(win)
	doors = [a, b, c]
	door = choice(doors)
	print "Correct door: ", door.getLabel()
	
	p = win.getMouse()
	while a.clicked(p) == False and b.clicked(p) == False and c.clicked(p) == False:
		p = win.getMouse()
	chosen = a
	for i in doors:
		if i.clicked(p) == True:
			chosen = i
	chosen.rect.setFill("red")
	print "Guessed door: ", chosen.getLabel()
	if chosen == door:
		header.setText("Correct!")
		door.rect.setFill("blue")
	else:
		header.setText("Incorrect!")
		door.rect.setFill("blue")
	win.getMouse()
	win.close()
main()
	
