import math

def validate():
	valid = False
	while valid == False:
		n = input("Enter a value for x that is greater than 2: ")
		if n > 2:
			valid = True
		else:
			valid = False
	return n
def primeornot():
	x = validate()
	prime = True
	for i in range(2, int(math.sqrt(x) + 1), 1):
		if x % i == 0:
			prime = False
			break
	if prime == True:
		print "%d is a prime number." % (x)
	else:
		print "%d is NOT a prime number." % (x)
	
primeornot()
		
	
