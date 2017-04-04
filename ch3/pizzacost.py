# pizzacost.py
def main():
	import math
	price = input("Please enter the price of the pizza, in dollars: ")
	diameter = input("Please enter the diameter, in inches: ")
	if diameter >= 10:
		print('That is a big pizza!')
	else:
		print('That is a small pizza!')
	priceperin = price / (4 * math.pi * (diameter/2.0)**2)
	print('The price per square inch is %0.2f.' % (priceperin))

main()
