# gpasortgui.py
# A program to sort student objects into GPA order
from graphics import *
from classButton import Button
import string

class Student:
    
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
        
    def getName(self):
        return self.name
    
    def getHours(self):
        return self.hours
        
    def getQPoints(self):
        return self.qpoints
    
    def gpa(self):
        return self.qpoints/self.hours
    
    def addGrade(self, gradePoint, credits):
        self.qpoints = self.qpoints + gradePoint
        self.hours = self.hours + credits
        
def makeStudent(infoStr):
    name, hours, qpoints = string.split(infoStr, " ")
    return Student(name, hours, qpoints)

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        outfile.write("%s\t%f\t%f\n" % (s.getName(), s.getHours(), s.getQPoints()))
    outfile.close()
    
def cmpGPA(s1, s2):
    return cmp(s1.gpa(), s2.gpa())

def cmpName(s1, s2):
	return cmp(s1.name, s2.name)

def cmpCredits(s1, s2):
	return cmp(s1.qpoints, s2.qpoints)
    
def main():
	win = GraphWin()
	win.setCoords(0,0,10,10)
	infilebutton = Entry(Point(5,8), 15)
	infilebutton.setText("Please enter the file to sort >> ")
	infilebutton.draw(win)
	while infilebutton.getText() == "Please enter the file to sort >> ":
		win.getMouse()
	filename = infilebutton.getText()
	outfilebutton = Entry(Point(5,2), 15)
	outfilebutton.setText("Please enter the file to write to >> ")
	outfilebutton.draw(win)
	while outfilebutton.getText() == "Please enter the file to write to >> ":
		win.getMouse()
	outfilename = outfilebutton.getText()
	data = readStudents(filename)
	
	bGPA = Button(win, Point(2,5), 3, 2, "GPA")
	bGPA.activate()
	bName = Button(win, Point(5,5), 3, 2, "Name")
	bName.activate()
	bCredits = Button(win, Point(8,5), 3, 2, "Credits")
	bCredits.activate()

	p = win.getMouse()
	while not(bGPA.clicked(p) or bName.clicked(p) or bCredits.clicked(p)):
		p = win.getMouse()
	if bGPA.clicked(p):
		bGPA.deactivate()
		data.sort(cmpGPA)
	elif bName.clicked(p):
		bName.deactivate()
		data.sort(cmpName)
	else:
		bCredits.deactivate()
		data.sort(cmpCredits)
	writeStudents(data, outfilename)
	print "The data has been written to", outfilename
    
if __name__ == '__main__':
    main()
    
