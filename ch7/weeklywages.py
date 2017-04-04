def wages(hours, rate):
	total = 0
	if hours > 40:
		total = (hours - 40)* 1.5 * rate + 40 * rate
	else:
		total = hours * rate
	return total

print wages(40, 16)
		
