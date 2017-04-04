def main():
	score = input("Enter the quiz score (1-5): ")
	if score == 1:
		print "F"
	elif score == 2:
		print "D"
	elif score == 3:
		print "C"
	elif score == 4:
		print "B"
	elif score == 5:
		print "A"
	else:
		print "You did not enter a valid score!"
	
main()