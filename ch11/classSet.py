# classSet.py

class Set:
	
	def __init__(self, elements):
		self.elements = elements
	
	def addElement(self, x):
		self.elements = self.elements + [x]
	
	def deleteElement(self, x):
		self.elements.remove(x)
	
	def member(self, x):
		return x in self.elements
		
	def intersection(self, set2):
		newset = []
		for i in self.elements:
			for j in set2:
				if i == j:
					newset = newset + [i]
		repeats = True
		while repeats:
			repeats = False
			for i in newset:
				if newset.count(i) > 1:
					newset.remove(i)
					repeats = True
		return newset
	
	def union(self, set2):
		newset = self.elements
		for i in set2:
			newset = newset + [i]
		repeats = True
		while repeats:
			repeats = False
			for i in newset:
				if newset.count(i) > 1:
					newset.remove(i)
					repeats = True
		return newset
		
	def subtract(self, set2):
		newset = self.elements
		for i in set2:
			if i in newset:
				newset.remove(i)
		return newset
		
		