# fibonacci.py
def fib(n):
	x = 1
	y = 0
	for i in range(n):
		z = x + y
		x = y
		y = z
	return z

print fib(6)
