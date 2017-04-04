# rankcards.py
from classPlayingCard import PlayingCard
import string

def main():
	filename = raw_input("Please enter the file containing a list of cards: ")
	cards = []
	infile = open(filename, 'r')
	for line in infile:
		r,s = string.split(line)
		newcard = PlayingCard(r,s)
		cards = cards + [newcard]
	rank(cards)
	for i in cards:
		print
		print i.__str__()

def rank(c):
	done = False
	while done == False:
		done = True
		pos = -1
		count = 0
		for i in c:
			pos = pos + 1
			if pos > len(c) - 2:
				break
			if c[pos + 1].rank < c[pos].rank:
				c[pos], c[pos + 1] = c[pos + 1], c[pos]
				done = False
	done = False
	while done == False:
		done = True
		pos = -1
		count = 0
		for i in c:
			pos = pos + 1
			if pos > len(c) - 2:
				break
			if c[pos + 1].suitrank < c[pos].suitrank:
				c[pos], c[pos + 1] = c[pos + 1], c[pos]
				done = False
	return c

def royalflush(hand):
	rank(hand)
	a = hand[0].suit
	for i in hand:
		if i.suit != a:
			return False
	if hand[0].rank == 10 and hand[1].rank == 11 and hand[2].rank == 12 and hand[3].rank == 13 and hand[4].rank == 1:
		return True
	else:
		return False
	
	
	
main()
