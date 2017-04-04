# spherevolume.py
import math

def main():
	r = input("Please enter the radius of the sphere: ")
	v = float(4)/3 * math.pi * r**3
	print "The volume of a sphere with radius %d is %0.2f." % (r, v)

main()
