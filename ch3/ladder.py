def main():
	import math
	deg = input("Please enter the angle that the ladder makes with the house, in degrees: ")
	length = input("Please enter the length of the ladder, in feet: ")
	rad = (math.pi)/180 * deg
	h = length * math.sin(rad)
	print "The height reached is", h

main()