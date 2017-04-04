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
	
def validate(n):
	if n % 2 == 0:
		return True
	else:
		return False

def nprimes(n):
	primes = []
	primecount = 0
	count = 0
	while primecount < n - 1:
		count = count + 1
		if primeornot(count) == True:
			primes = primes + [count]
			primecount = primecount + 1
	return primes
	
def main():
	n = input("Please enter an even number: ")
	while validate(n) == False:
		n = input("Please enter an EVEN number: ")
	found = False
	primes1, primes2 = nprimes(n), nprimes(n)
	for a in primes1:
		for b in primes2:
			if a + b == n:
				found = True
				break
		if found == True:
			break
	print "The two prime numbers that sum to %d are %d and %d." % (n, a, b)

main()
	
