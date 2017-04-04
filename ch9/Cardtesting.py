from random import *

class Card:
	def __init__(self, name, value):
		self.val = value
		self.name = name
	
	def getVal(self):
		return self.val
	
	def getName(self):
		return self.name
		

def showHand(hand):
	for i in hand:
		print i.getName,

def main():
	a = Card("Ace", 2)
	print a.getName()

main()
