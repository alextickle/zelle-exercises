import math

def triarea(a, b, c):
	s = (a + b + c)/2.0
	return math.sqrt(s*(s - a)*(s - b)*(s - c))

print triarea(3, 4, 5)