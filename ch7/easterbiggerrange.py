def yearValid(year):
	if year <= 2099 and year >= 1900:
		return True
	else:
		return False

def main():
	year = input("Please enter a year in range 1900-2099: ")
	while yearValid(year) == False:
		year = input("The year you entered lies outside the range. Please enter another: ")
	a = year%19
	b = year%4
	c = year%7
	d = (19*a + 24)%30
	e = (2*b + 4*c + 6*d + 5)%7
	if year != 1954 and year != 1981 and year != 2049 and year != 2076:
		date = 22 + d + e
	else: date = 15 + d + e
	if date > 31:
		print "In year %d, Easter will be the %d of April." % (year, date - 31)
	else:
		print "In year %d, Easter will be the %d of March." % (year, date)
main()

	