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
		
	def addLetterGrade(self, letter, credits):
		grades = ["A+", "A", "A-", "B+", "B"]
		points = [4.0, 3.7, 3.6, 3.5, 3.0] 
		pos = 0
		pointtoadd = 0
		for i in grades:
			if i == letter:
				pointtoadd = points[pos]
			pos = pos + 1 
		self.qpoints = self.qpoints + pointtoadd
		self.hours = self.hours + credits