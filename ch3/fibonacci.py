# fibonacci.py
def main():
	print "This program demonstrates the Fibonacci sequence."
	n = input("Please enter a value for n: ")
	x = 1
	y = 0
	for i in range(n):
		z = x + y
		x = y
		y = z
		
		print z
def fib(n):
	x = 1
	y = 0
	for i in range(n):
		z = x + y
		x = y
		y = z
	return z

print fib(5)
