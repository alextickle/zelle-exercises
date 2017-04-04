# gpasort2.py
# A program to sort student objects into GPA order

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
    
def main():
    print "This program sorts student grade information by GPA, credits, or name"
    filename = raw_input("Enter the filename of the file to sort >> ")
    print
    data = readStudents(filename)
    studenttuplelist = []
    finalstudentlist = []
    for i in data:
        studenttuplelist = studenttuplelist + [(i.gpa(), i.getName())]
    studenttuplelist.sort()
    for t in studenttuplelist:
        for s in data:
            if t[1] == s.getName():
                finalstudentlist = finalstudentlist + [s]
    for i in finalstudentlist:
        print i.getName()
    
if __name__ == '__main__':
    main()
    
