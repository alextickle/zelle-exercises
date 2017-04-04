from graphics import *
from classTracker import Tracker
from classProjectile import Projectile
from time import sleep

def main():
	win = GraphWin()
	win.setCoords(0,0,10,10)
	c = Projectile(45, 8 , 1)
	c.draw(win)
	d = Tracker(win, c)
	while c.getY() > 0:
		c.update(.05)
		d.update(c)
		sleep(.1)
	win.getMouse()
	win.close()

main()
		
