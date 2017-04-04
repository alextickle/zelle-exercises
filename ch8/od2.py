import string

def main():
	startod = input("Please enter the initial odometer reading: ")
	both = raw_input("Please enter the current odometer reading and gas consumed after the first leg, separated by a space: ")
	startlegod = startod
	gastot = 0
	print "!!!"
	while both != False:
		endlegod, gascon = int(string.split(both, " "))
		gastot = gastot + gascon
		print "The MPG for this leg was %0.2f." % ((endlegod - startlegod)/gascon)
		startlegod = endlegod 
		both = raw_input("Please enter the current odometer reading and gas consumed, separated by a space (<Enter> to exit) ")
	print "MPG for the entire trip was %0.2f" % (endlegod - startod)/gastot

main()
