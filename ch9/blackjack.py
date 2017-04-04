from random import *

class Card:
	def __init__(self, name, value):
		self.val = value
		self.name = name
	
	def getVal(self):
		return self.val
	
	def getName(self):
		return self.name

def main():
	print "This program simulates the game of blackjack."
	deck = [Card("Ace", 1), Card("Two", 2), Card("Three", 3), 
	Card("Four", 4), Card("Five", 5), Card("Six", 6), Card("Seven", 7),
	Card("Eight", 8), Card("Nine", 9), Card("Ten", 10), Card("Jack", 10), 
	Card("Queen", 10), Card("King", 10)]
	handplayer = []
	handdealer = []
	playertotal = 0
	dealertotal = 0
	winner = ""
	while bust(playertotal) == False and bust(dealertotal) == False:
		handplayer = handplayer + [choice(deck)]
		print "The player's hand: ", showHand(handplayer)
		playertotal = totalVal(handplayer)
		if bust(playertotal) == True:
			print "Player busted!"
			winner = "dealer"
			break
		elif playertotal == 21:
			winner = "player"
			break
		handdealer = handdealer + [choice(deck)]
		print "The dealer's hand: ", showHand(handdealer), "\n"
		dealertotal = totalVal(handdealer)
		if bust(dealertotal) == True:
			print "Dealer busted!"
			winner = "player"
		elif dealertotal == 21:
			winner = "dealer"
			break
	print "The winner of this hand is", winner
	
	
def hasAce(hand):
	ace = False
	for i in hand:
		if i.getName() == "Ace":
			ace = True
	return ace

def showHand(hand):
	for i in hand:
		print i.getName(),

def totalVal(hand):
	total = 0
	for i in hand:
		total = total + i.getVal()
	if hasAce(hand) == True and total <= 10 and total >= 7:
		total = total + 9
	return total
	
def bust(total):
	return total > 21

main()

		
		
	
	
	
	
