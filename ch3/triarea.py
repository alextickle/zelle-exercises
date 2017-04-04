def main():
	import math
	s1, s2, s3 = input("Please enter the lengths of the 3 sides of the triangle, separated by commas: ")
	s = (s1 + s2 + s3)/2.0
	a = math.sqrt(s*(s - s1)*(s - s2)*(s - s3))
	print "The area of the triangle is", a

main()