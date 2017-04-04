# classDeck.py
from classPlayingCard import PlayingCard
import string
import random

class Deck:
	def __init__(self):
		self.deck = []
		infile = open("deck.txt", 'r')
		for line in infile:
			r,s = string.split(line)
			newcard = PlayingCard(r,s)
			self.deck = self.deck + [newcard]
		infile.close()
	
	def reset(self):
		self.deck = []
		infile = open(filename, 'deck.txt')
		for line in infile:
			r,s = string.split(line)
			newcard = PlayingCard(r,s)
			self.deck = self.deck + [newcard]
		infile.close()
	
	def shuffle(self):
		for i in range(len(self.deck)):
			num = random.randrange(len(self.deck))
			self.deck[i], self.deck[num] = self.deck[num], self.deck[i]
	
	def dealCard(self):
		a = self.deck[0]
		self.deck.remove(self.deck[0])
		return a
	
	def cardsLeft(self):
		return len(self.deck)
		
		
	
		