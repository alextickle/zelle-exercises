def toDouble(apr):
	total = 1
	years = 0
	while total < 2:
		total = total * (1 + apr/100.0)
		years = years + 1
	return years

print toDouble(7)