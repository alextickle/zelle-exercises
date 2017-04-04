def main():
	wt = input("Please enter your weight, in lbs: ")
	h = input("Please enter your height, in inches: ")
	bmi = wt*720.0/(h**2)
	if bmi < 19:
		print "Your BMI is %0.2f, and it is too low." % (bmi)
	elif bmi >= 19 and bmi <= 25:
		print "Your BMI is %0.2f, and it is within the healthy range." % (bmi)
	else:
		print "Your BMI is %0.2f, and it is too high!" % (bmi)
	

main()
	
