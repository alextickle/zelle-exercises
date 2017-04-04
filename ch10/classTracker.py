from graphics import *

class Tracker:
	def __init__(self, window, objToTrack):
		self.circ = Circle(Point(50, 50), 5)
		self.circ.draw(window)
		
	def update(self, objToTrack):
		self.circ.move(objToTrack.getX() - self.circ.getCenter().getX(), objToTrack.getY() - self.circ.getCenter().getY())
		