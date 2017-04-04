import string

def main():
	fname = raw_input("Please enter the filename: ")
	infile = open(fname, 'r')
	startod = float(infile.readline())
	both = infile.readline()
	startlegod = startod
	gastot = 0.0
	while both != "":
		endlegodStr, gasconStr = string.split(both, " ")
		endlegod = float(endlegodStr)
		gascon = float(gasconStr)
		gastot = gastot + gascon
		print "The MPG for this leg was %0.2f." % ((endlegod - startlegod)/gascon)
		startlegod = endlegod 
		both = infile.readline()
	print "MPG for the entire trip was %0.2f" % ((endlegod - startod)/gastot)
	
main()
