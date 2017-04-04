from graphics import *
from classFace import Face
from classButton import Button
from time import sleep

def main():
	win = GraphWin()
	win.setCoords(0,0,10,10)
	a = Face(win, Point(5,5), 2)
	p = Point(0,0)
	dx, dy = 0.5, 0.25
	fnum = 0
	for i in range(10000):
		a.move(dx, dy)
		if a.head.getCenter().getX() >= 10 or a.head.getCenter().getX() <= 0:
			dx = -dx
			fnum = cycleFace(a, fnum)
		if a.head.getCenter().getY() >= 10 or a.head.getCenter().getY() <= 0:
			dy = -dy
			fnum = cycleFace(a, fnum)
		sleep(.1)
	a.undraw()
	win.close()

def cycleFace(face, fnum):
	if fnum == 0:
		face.reset()
		face.wink()
		fnum = fnum + 1
	elif fnum == 1:
		face.reset()
		face.frown()
		fnum = fnum + 1
	elif fnum == 2:
		face.reset()
		face.smile()
		fnum = fnum + 1
	elif fnum == 3:
		face.reset()
		fnum = 0
	return fnum
	
	
		

main()
