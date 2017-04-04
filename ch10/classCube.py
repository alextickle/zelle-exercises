class Cube:
	def __init__(self, side):
		self.side = side
		self.volume = side**3
		self.area = side**2
		
	def getArea(self):
		return self.area
	
	def getVol(self):
		return self.volume
		
def main():
	s = input("Please enter the length of a side: ")
	a = Cube(s)
	print "Side: %d" % (a.side)
	print "Area: %d" % (a.area)
	print "Volume: %d" % (a.volume)
	
main()
