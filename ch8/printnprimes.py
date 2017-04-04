import math
	
def primeornot(x):
	prime = True
	for i in range(2, int(math.sqrt(x) + 1), 1):
		if x % i == 0:
			prime = False
			break
	if prime == True:
		return True
	else:
		return False
	
def primeston():
	n = input("Please enter a value for n: ")
	primes = []
	for i in range(1, n + 1, 1):
		if primeornot(i) == True:
			primes = primes + [i]
	print "The list of primes up to n is", primes

def printnprimes():
	n = input("Please enter a value for n: ")
	print "Here is a list of the first n primes"
	primecount = 0
	count = 0
	while primecount < n - 1:
		count = count + 1
		if primeornot(count) == True:
			print count,
			primecount = primecount + 1
	
	
printnprimes()
		
	
