# pizzacost2.py
import math

def pizzaarea(d):
	return math.pi * (d/2.0)**2  
	
def costperinch(area, p):
	return area/p

def main():
	price = input("Please enter the price of the pizza, in dollars: ")
	diameter = input("Please enter the diameter, in inches: ")
	print "The price per square inch is %0.2f." % (costperinch(pizzaarea(diameter), price))

main()
