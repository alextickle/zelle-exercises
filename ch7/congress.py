def main():
	age = input("Please enter your age: ")
	yearscit = input("Please enter the number of years that you've been a US citizen: ")
	senate = "No"
	house = "No"
	if age >= 30 and yearscit >= 9:
		sentate = "Yes"
		house = "Yes"
	elif age >= 25 and yearscit >= 7:
		house = "Yes"
	print "Eligible for the Senate? %s" % (senate)
	print "Eligible for the House? %s" % (house)

main()
		
