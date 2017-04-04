def main():
	wt = input("Please enter your weight, in lbs: ")
	h = input("Please enter your height, in inches: ")
	bmi = wt*720.0/(h**2)
	if bmi < 19:
		print "Your BMI is too low."
	elif bmi >= 19 and bmi <= 25:
		print "Your BMI is within the healthy range."
	else:
		print "Your BMI is too high!"
	

main()
	
