def main():
	x1, y1 = input("Enter the first point (x, y): ")		
	x2, y2 = input("Enter the second point (x, y): ")
	slope = (y2 - y1)/float(x2 - x1)
	print "The slope of the line between these two points is", slope

main()
	