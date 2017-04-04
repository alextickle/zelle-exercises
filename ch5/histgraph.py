from graphics import *
import string

def main():
	fname = raw_input("Please enter the name of the file: ")
	infile = open(fname, "r")
	scores = infile.read()
	win = GraphWin()
	win.setCoords(0,0,11,len(scores))
	for i in range(1,10):
		Rectangle(Point(i,0), Point(i + 0.5, scores.count(str(i)))).draw(win)
		
main()
		
