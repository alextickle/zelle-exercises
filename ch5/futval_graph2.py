# futval_graph.py
from graphics import *

def main():
	print "This program plots the growth of a 10 year investment."
	principal = input("Enter the initial principal: ")
	apr = input("Enter the annualized interest rate: ")
	
	win = GraphWin("Investment Growth Chart", 320, 240)
	win.setBackground("white")
	win.setCoords(-1.75, -200, 11.5, 10400)
	Text(Point(-1, 0), ' 0.0K').draw(win)
	Text(Point(-1, 2500), ' 2.5K').draw(win)
	Text(Point(-1, 5000), ' 5.0K').draw(win)
	Text(Point(-1, 7500), ' 7.5.0K').draw(win)
	Text(Point(-1, 10000), ' 10.0K').draw(win)
	
	bar = Rectangle(Point(0,0), Point(1, principal))
	bar.setFill("green")
	bar.setWidth(2)
	bar.draw(win)
	
	for year in range(1,11):
		principal = principal * (1 + apr)
		bar = Rectangle(Point(year, 0), Point(year + 1, principal))
		bar.setFill("green")
		bar.setWidth(2)
		bar.draw(win)
	
	raw_input("Press <Enter> to quit")
	win.close()
main()
	