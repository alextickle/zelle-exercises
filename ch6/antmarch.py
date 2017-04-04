def march(num):
	print "The ants go marching %s by %s, hurrah! hurrah!" % (num, num)
	print "The ants go marching %s by %s, hurrah! hurrah!" % (num, num)
	print "The ants go marching %s by %s," % (num, num)
	print "The little one stops to suck his thumb,"
	print "And they all go marching down."
	print 
	
def main():
	allnums = ["one", "two", "three", "four", "five"]
	for i in allnums:
		march(i)
	
main()
