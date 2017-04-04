def main():
	limit = input("Please enter the speed limit: ")
	speed = input("Please enter the clocked speed: ")
	if speed <= limit:
		print "Legal!"
	elif speed > 100:
		ticket = 50 + 5*(speed - limit) + 200
		print "You were speeding! You owe $%d." % (ticket)
	else:
		ticket = 50 + 5*(speed - limit)
		print "You were speeding! You owe $%d." % (ticket)
	
main()
	
