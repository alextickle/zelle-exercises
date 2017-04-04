# classGraphicsGroup.py

class GraphicsGroup:

	def __init__(self, anchor):
		self.all = []
		self.anchor = anchor
	
	def getAnchor(self):
		return self.anchor
		
	def addObject(self, x):
		self.all = self.all + [x]
		
	def move(self, dx, dy):
		for i in self.all:
			i.move(dx,dy)
		self.anchor.move(dx,dy)
	
	def draw(self, win):
		for i in self.all:
			i.draw(win)
	
	def undraw(self, win):
		for i in self.all:
			i.undraw(win)
		
	
	