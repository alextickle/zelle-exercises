from graphics import *
import string

def main():
	fname = raw_input("Please enter the name of the file: ")
	infile = open(fname, "r")
	n = eval((infile.readline()))
	win = GraphWin()
	win.setCoords(-100,0,110,7)
	student = ""
	grade = 0
	for i in range(n-1):
		student, gstr = string.split(infile.readline())
		Text(Point(-45, 6-i), student).draw(win)
		Rectangle(Point(0, 6-i), Point(eval(gstr), 5.5-i)).draw(win)
	win.getMouse()

main()
		
