from graphics import *
from classTarget import Target
from random import *
from classProjectile import getInputs

def main():
	win = GraphWin()
	win.setCoords(0,0,10,10)
	t = Target(5, 3, 1)
	t.draw(win)
	p = win.getMouse()
	print t.targetHit(p)

main()
