def main():
	score = input("Enter the quiz score (0-100): ")
	if score > 100 or score < 0:
		print "That is not a valid score!"
	elif score <= 59:
		print "F"
	elif score <= 69:
		print "D"
	elif score <= 79:
		print "C"
	elif score <= 89:
		print "B"
	else:
		print "A"
	
main()