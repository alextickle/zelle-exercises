from graphics import *
from classFace import Face
from classButton import Button

def main():
	win = GraphWin()
	win.setCoords(0,0,10,10)
	a = Face(win, Point(5,5), 3)
	smileb = Button(win, Point(1.5,9), 3, 1, 'Smile')
	smileb.activate()
	winkb = Button(win, Point(5, 9), 3, 1, 'Wink')
	winkb.activate()
	frownb = Button(win, Point(8.5, 9), 3, 1, 'Frown')
	frownb.activate()
	quitb = Button(win, Point(8.5,1), 3,1, 'Quit')
	quitb.activate()
	p = Point(0,0)
	while quitb.clicked(p) == False:
		p = win.getMouse()
		a.reset()
		if smileb.clicked(p) == True:
			a.smile()
		elif frownb.clicked(p) == True:
			a.frown()
		elif winkb.clicked(p) == True:
			a.wink()
	a.undraw()
	win.close()
	
		

main()
