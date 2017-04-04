# classStatSet.py
import math

class StatSet:
	
	def __init__(self):
		self.statset = []
	
	def addNumber(self, x):
		self.statset = self.statset + [x]
		
	def mean(self):
		n = float(len(self.statset))
		sum = 0
		for i in self.statset:
			sum = sum + i
		return sum/n
	
	def median(self):
		length = len(self.statset)
		if length % 2 == 0:
			return ((self.statset[length/2 - 1] + self.statset[length/2 + 1])/2)
		else:
			return self.statset[length/2 + 1]
	
	def stdDev(self):
		n = float(len(self.statset))
		xbar = self.mean()
		sum = 0
		for i in self.statset:
			sum = sum + math.sqrt(((i - xbar)**2)/n)
		return sum
		
	def count(self):
		return len(self.statset)
	
	def min(self):
		self.statset.sort()
		return self.statset[0]
	
	def max(self):
		self.statset.sort()
		return self.statset[-1]
			