def main():
	print "This program calculates the distance between an observer and a lightening strike"
	print "given the time elapsed from flash to boom."
	time = input("Please enter the time elapsed, in seconds: ")
	d = 1100/5280.00 * time
	print "The lightening struck ground roughly %0.2f miles away." % (d)

main()