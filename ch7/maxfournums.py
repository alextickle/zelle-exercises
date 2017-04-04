def main():
	a, b, c, d = input("Please enter 4 numbers, separated by commas: ")
	max = 0
	if a >= b:
		if a >= c:
			if a >= d:
				max = a
			else:
				max = d
		elif c >= d:
			max = c
		else:
			max = d
	elif b >= c:
		if b >= d:
			max = b
		else:
			max = d
	elif c >= d:
		max = c
	else:
		max = d
	
	print "The maximum value is", max

main()
		