import string

def main(fname):
	infile = open(fname, 'r')
	temps = string.split(infile.read())
	cooldays = 0
	hotdays = 0
	for i in temps:
		if int(i) > 80:
			cooldays = cooldays + int(i) - 80
		elif int(i) < 60:
			hotdays = hotdays - int(i) + 60
	print hotdays, cooldays

main("degreedays.txt")
