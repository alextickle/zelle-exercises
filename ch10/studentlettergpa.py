from classStudent import Student
import string

def main():
	name = raw_input("Please enter the student's name: ")
	a = Student(name, 0, 0)
	n = input("How many courses do you have to enter: ")
	for i in range(n):
		gradeStr = raw_input("Please enter the Grade (A+, etc) and Course Hours, separated by a comma: ")
		grade, hours = string.split(gradeStr, ",")
		h = eval(hours)
		a.addLetterGrade(grade, h)
	print "%s's GPA is %0.2f." % (a.getName(), a.gpa())

main()
