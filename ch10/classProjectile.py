import math
from graphics import *

class Projectile:
	
	def __init__(self, angle, velocity, height):
		self.xpos = 0.0
		self.ypos = height
		theta = math.pi * angle / 180.0
		self.xvel = velocity * math.cos(theta)
		self.yvel = velocity * math.sin(theta)
		self.circ = Circle(Point(self.xpos, self.ypos), 0.5)
		self.circ.setFill("black")
	
	def getX(self):
		return self.xpos
		
	def getY(self):
		return self.ypos
		
	def getYvel(self):
		return self.yvel
		
	def update(self, time):
		x0, y0 = self.xpos, self.ypos
		self.xpos = self.xpos + time * self.xvel
		yvel1 = self.yvel - time * 9.8
		self.ypos = self.ypos + time * (self.yvel + yvel1)/2.0
		self.yvel = yvel1
		self.circ.move(self.xpos - x0, self.ypos - y0)
		
	def draw(self, win):
		self.circ.draw(win)
		
def getInputs():
	a = input("Enter the launch angle (in degrees): ")
	v = input("Enter the initial velocity (in meters/sec): ")
	h = input("Enter the initial height (in meters): ")
	t = input("Enter the time initerval between position calculations: ")
	return a, v, h, t
	
def main():
	angle, vel, h0, time = getInputs()
	cball = Projectile(angle, vel, h0)
	while cball.getY() >= 0:
		cball.update(time)
	print "\nDistance traveled: %0.1f meters." % (cball.getX())


