from graphics import *

class Regression:
	
	def __init__(self):
		self.points = []
		self.m = 0
		self.xbar = 0
		self.ybar = 0
	
	def addPoint(self, point):
		self.points = self.points + [point]
	
	def update(self):
		countp = 0
		sumx = 0
		sumy = 0
		for i in self.points:
			sumx = sumx + i.getX()
			countp = countp + 1.0
		self.xbar = sumx/countp
	
		for i in self.points:
			sumy = sumy + i.getY()
		self.ybar = sumy/countp
	
		mnum = 0
		mdenom = 0
		for i in self.points:
			mnum = mnum + (i.getX() * i.getY()) - countp * self.xbar * self.ybar
			mdenom = mdenom + (i.getX())**2 - (countp * self.xbar**2) 
	
		self.m = mnum/mdenom
	
	def drawLine(self, win):
		Line(Point(0, self.ybar + self.m * (-self.xbar)), Point(100, self.ybar + self.m * (100 - self.xbar))).draw(win)
		
	def printPoints(self):
		for i in self.points:
			print i.getX(),i.getY()
	
	def predict(self, x):
		return self.ybar + self.m * (x - self.xbar)
		