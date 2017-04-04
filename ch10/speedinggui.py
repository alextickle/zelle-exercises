from classButton import Button
from graphics import *

def main():
	win = GraphWin(400, 500)
	win.setCoords(0,0,20,20)
	
	limit = Entry(Point(10,18), 10)
	limit.setText("Speed Limit: ")
	limit.draw(win)
	win.getMouse()
	while limit.getText() == "Speed Limit: ":
		win.getMouse()
	limitint = eval(limit.getText())
	
	speed = Entry(Point(10,13), 10)
	speed.setText("Clocked Speed: ")
	speed.draw(win)
	win.getMouse()
	while speed.getText() == "Clocked Speed: ":
		win.getMouse()
	speedint = eval(speed.getText())
	
	speeding = Button(win, Point(10,10), 9, 2, "Speeding?")
	speeding.activate()
	
	
	while speeding.clicked(win.getMouse()) == False:
		win.getMouse()
	yorn = Text(Point(10, 5), "")
	if speedint <= limitint:
		yorn.setText("No!")
	elif speedint > 100:
		ticket = 50 + 5*(speedint - limitint) + 200
		yorn.setText("You were speeding! You owe $%d." % (ticket)) 
	else:
		ticket = 50 + 5*(speedint - limitint)
		yorn.setText("You were speeding! You owe $%d." % (ticket)) 
	yorn.draw(win)
	win.getMouse()
	win.close()
	
main()
	


