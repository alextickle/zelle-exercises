from graphics import *
import string

class PlayingCard:
	def __init__(self, rank, suit):
		self.suit = string.lower(suit[0])
		self.rank = eval(rank)
		names = ["Ace", "2", "3", "4", "5", "6", "7", "8",
		"9", "10", "Jack", "Queen", "King"]
		suitnames = ["Diamonds", "Clubs", "Hearts", "Spades"]
		self.cardname = names[self.rank - 1]
		self.suitname = ""
		self.suitrank = 0
		if self.suit == "d":
			self.suitname = suitnames[0]
			self.suitrank = 0
		elif self.suit == "c":
			self.suitname = suitnames[1]
			self.suitrank = 1
		elif self.suit == "h":
			self.suitname = suitnames[2]
			self.suitrank = 2
		else:
			self.suitname = suitnames[3]
			self.suitrank = 3
		
	def getRank(self):
		return self.rank
	
	def getSuit(self):
		return self.suit
	
	def BJValue(self):
		if 10 <= self.rank <= 13:
			return 10
		else:
			return self.rank
			
	def __str__(self):
		return self.cardname + " of " + self.suitname
	
	def draw(self, win, center):
		fname = self.suitname + self.cardname + ".gif"	
		myImage = Image(center, fname)
		myImage.draw(win)

