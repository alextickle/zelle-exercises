from graphics import *
import turtle

class Face:

	def __init__(self, window, center, size):
		self.size = size
		self.w = window
		eyeSize = 0.15 * size
		eyeOff = size/3.0
		mouthSize = 0.8 * size
		mouthOff = size/2.0
		self.head = Circle(center, size)
		self.head.draw(window)
		self.head.setFill("yellow")
		self.head.setOutline("yellow")
		self.leftEye = Circle(center, eyeSize)
		self.leftEye.move(-eyeOff, eyeOff)
		self.leftEye.setFill("black")
		self.rightEye = Circle(center, eyeSize)
		self.rightEye.move(eyeOff, eyeOff)
		self.rightEye.setFill("black")
		self.leftEye.draw(window)
		self.rightEye.draw(window)
		p1 = center.clone()
		p1.move(-mouthSize/2, -mouthOff)
		p2 = center.clone()
		p2.move(mouthSize/2, -mouthOff)
		self.mouth = Line(p1,p2)
		self.mouth.draw(window)
		self.smile2 = Circle(Point((p2.getX() + p1.getX())/2.0, p1.getY()), size/3.0)
		self.smilerects = Rectangle(Point(self.smile2.getCenter().getX() - size/3.0, self.smile2.getCenter().getY()), Point(self.smile2.getCenter().getX() + size/3.0, self.smile2.getCenter().getY() + size/3.0))
		self.smilerects.setFill("yellow")
		self.smilerects.setOutline("yellow")
		self.smilerectf = Rectangle(Point(self.smile2.getCenter().getX() - size/3.0, self.smile2.getCenter().getY()), Point(self.smile2.getCenter().getX() + size/3.0, self.smile2.getCenter().getY() + size/3.0))
		self.smilerectf.setFill("yellow")
		self.smilerectf.setOutline("yellow")
		self.smilerectf.move(0, -self.size/3.0)
		self.winkEye = Line(Point(self.rightEye.getCenter().getX() - self.size/3.0, self.rightEye.getCenter().getY()), Point(self.rightEye.getCenter().getX() + self.size/3.0, self.rightEye.getCenter().getY()))
		
	def smile(self):
		self.mouth.undraw()
		self.smile2.draw(self.w)
		self.smilerects.draw(self.w)
	
	def frown(self):
		self.mouth.undraw()
		self.smile2.draw(self.w)
		self.smilerectf.draw(self.w)
	
	def wink(self):
		self.rightEye.undraw()
		self.winkEye.draw(self.w)
		
	def move(self, dx, dy):
		self.head.move(dx, dy)
		self.rightEye.move(dx, dy)
		self.leftEye.move(dx, dy)
		self.mouth.move(dx, dy)
		self.smile2.move(dx, dy)
		self.smilerects.move(dx, dy)
		self.smilerectf.move(dx, dy)
		self.winkEye.move(dx, dy)
		
		
	def reset(self):
		self.head.undraw()
		self.rightEye.undraw()
		self.leftEye.undraw()
		self.mouth.undraw()
		self.smile2.undraw()
		self.smilerects.undraw()
		self.smilerectf.undraw()
		self.winkEye.undraw()
		self.head.draw(self.w)
		self.mouth.draw(self.w)
		self.rightEye.draw(self.w)
		self.leftEye.draw(self.w)
	
	def undraw(self):
		self.head.undraw()
		self.rightEye.undraw()
		self.leftEye.undraw()
		self.mouth.undraw()
		self.smile2.undraw()
		self.smilerects.undraw()
		self.smilerectf.undraw()
		self.winkEye.undraw()
	
		
		
	
		
	

