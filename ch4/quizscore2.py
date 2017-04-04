def main():
	score = input("Please enter the quiz score: ")
	grades = ["A", "A", "B", "C", "D", "F", "F", "F", "F", "F", "F"]
	print "You received a(n) %s." % (grades[-(score/10 + 1)])
main()
