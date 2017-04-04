def main():
	try:
		a, b, c = input("Please enter the coefficients of a quadratic equation (a, b, c): ")
		discRoot = math.sqrt(b * B - 4 * a * c)
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)
		print "\nThe solutions are: ", root1, root2
	except ValueError, exc0bj:
		msg = str(exc0bj)
		if msg == "math domain error":
			print "No real roots"
		elif msg == "unpack tuple of wrong size":
			print "You didn't enter the right number of coefficients"
		else:
			print "Something went wrong, sorry!"
	except NameError:
		print "You didn't enter three numbers"
	except TypeError:
		print "Your inputs were not all numbers"
	except SyntaxError:
		print "Your input was not in the correct form. Missing comma?"
	except:
		print "Something went wrong, sorry!"
	
main()
	
	