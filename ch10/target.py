from graphics import *
from classTarget import Target
from random import *
from classProjectile import Projectile
from time import *

def main():
	win = GraphWin(200,200)
	win.setCoords(0,0,10,10)
	t = Target(randrange(2,9,1),randrange(2,9,1), 2, 2)
	t.draw(win)
	while t.hit == False:
		angle, velocity, height, time = getInputs()
		c = Projectile(angle, velocity, height)
		c.draw(win)
		while c.getY() > 0:
			c.update(time)
			sleep(0.25)
			if t.targetHit(Point(c.getX(), c.getY())) == True:
				break
		if t.hit == True:
			print "You hit the target!\n"
		else:
			print "You missed!\n"
	
	win.getMouse()
	
def getInputs():
	a = input("Enter the launch angle (in degrees): ")
	v = input("Enter the initial velocity (in meters/sec): ")
	h = input("Enter the initial height (in meters): ")
	t = input("Enter the time initerval between position calculations: ")
	return a, v, h, t

main()
	
