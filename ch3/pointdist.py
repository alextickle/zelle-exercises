def main():
	import math
	x1, y1 = input("Enter the first point (x, y): ")		
	x2, y2 = input("Enter the second point (x, y): ")
	d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	print "The distance between these two points is", d

main()