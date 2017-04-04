# classCircButton.py
from graphics import *
import math

class CircButton:

	"""A CircButton is a labeled Circle in a window.
	It is activated or deactivated with the activate()
	and deactivate() methods. The clicked(p) method
	returns true if the button is active and p is inside it."""

	def __init__(self, win, center, radius, label):
		"""Creates a circular button, eg:
		qb = Button(myWin, centerPoint, radius, 'Quit')"""
		self.radius = radius
		self.circ = Circle(center, radius)
		self.circ.setFill('lightgray')
		self.circ.draw(win)
		self.label = Text(center, label)
		self.label.draw(win)
		self.deactivate()
		
	def clicked(self, p):
		"Returns true if button active and p is inside"
		return self.active and \
		self.circ.getRadius() >= math.sqrt((p.getX() - (self.circ.getCenter()).getX())**2 + (p.getY() - (self.circ.getCenter()).getY())**2)
		
		
	def getLabel(self):
		return self.label.getText()
	
	def activate(self):
		"Sets this button to 'active'"
		self.label.setFill('black')
		self.circ.setWidth(2)
		self.active = True
	
	def deactivate(self):
		"Sets this button to 'inactive'"
		self.label.setFill('darkgrey')
		self.circ.setWidth(1)
		self.active = False
	
		