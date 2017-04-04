from graphics import *
import math
from time import *

class Projectile:
	
	def __init__(self, angle, velocity, height):
		self.xpos = 0.0
		self.ypos = height
		theta = math.pi * angle / 180.0
		self.xvel = velocity * math.cos(theta)
		self.yvel = velocity * math.sin(theta)
	
	def getX(self):
		return self.xpos
		
	def getY(self):
		return self.ypos
		
	def update(self, time):
		self.xpos = self.xpos + time * self.xvel
		yvel1 = self.yvel - time * 9.8
		self.ypos = self.ypos + time * (self.yvel + yvel1)/2.0
		self.yvel = yvel1
		
def getInputs():
	a = input("Enter the launch angle (in degrees): ")
	v = input("Enter the initial velocity (in meters/sec): ")
	h = input("Enter the initial height (in meters): ")
	t = input("Enter the time initerval between position calculations: ")
	return a, v, h, t
	
def main():
	angle, vel, h0, time = getInputs()
	win = GraphWin()
	win.setCoords(0, 0, 25, 25)
	ball = Circle(Point(0, h0), 1)
	ball.setFill('black')
	ball.draw(win)
	
	cball = Projectile(angle, vel, h0)
	while cball.getY() >= 0:
		cball.update(time)
		ball.undraw()
		ball.move(cball.getX() - (ball.getCenter()).getX(), cball.getY() - (ball.getCenter()).getY())
		ball.draw(win)
		sleep(.5)

	win.getMouse()

main()
