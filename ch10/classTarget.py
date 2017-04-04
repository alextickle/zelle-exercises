import math
from graphics import *

class Target:
	def __init__(self, xpos, ypos, width, height):
		self.xpos = xpos
		self.ypos = ypos
		self.height = height
		self.width = width
		self.rect = Rectangle(Point(self.xpos - self.width/2.0, self.ypos - self.height/2.0), Point(self.xpos + self.width / 2.0, self.ypos + self.height/2.0))
		self.rect.setFill("red")
		self.rect.setOutline("red")
		self.hit = False
	
	def draw(self, win):
		self.rect.draw(win)
	
	def targetHit(self, point):
		if abs(self.xpos - point.getX()) <= self.width/2.0 and abs(self.ypos - point.getY()) <= self.height/2.0:
			self.hit = True
			return True
		else:
			return False
	
	
		