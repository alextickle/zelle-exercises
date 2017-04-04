import string

def sumSquaresfile(fname):	
	infile = open(fname, "r")
	fileVal = 0
	lineVal = 0
	all = string.split(infile.read())
	for i in all:
		fileVal = fileVal + (int(i))**2
	return fileVal

print sumSquaresfile("numbers.txt")
			
		
