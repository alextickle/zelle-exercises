def main():
	n = input("Choose a value: ")
	print "index     %d" % (n)
	for i in range(10):
		n = n * 1.0342546
		print "%-4.d %0.6f" % (i + 1, n)

main()
