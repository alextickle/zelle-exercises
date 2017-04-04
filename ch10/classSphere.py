# classSphere.py
import math

class Sphere:

	def __init__(self, radius):
		self.radius = radius
		
	def getRadius(self):
		return self.radius
	
	def surfaceArea(self):
		return 4 * math.pi * self.radius**2
		
	def volume(self):
		return 4/3.0 * math.pi * self.radius**3
	

def main():
	r = input("Please enter the radius of the sphere: ")
	a = Sphere(r)
	print "Radius: %d" % (a.getRadius())
	print "Surface Area: %0.2f" % (a.surfaceArea())
	print "Volume: %0.2f" % (a.volume())
	
main()
