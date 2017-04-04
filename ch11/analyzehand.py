# analyzehand.py
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
	if royalflush(cards):
		print "Royal Flush"
	elif straightflush(cards):
		print "Straight Flush"
	elif straight(cards):
		print "Straight"
	elif flush(cards):
		print "Flush"
	elif fourofkind(cards):
		print "Four of a Kind"
	elif fullhouse(cards):
		print "Full House"
	elif threeofkind(cards):
		print "Three of a Kind"
	elif twopair(cards):
		print "Two Pair"
	elif pair(cards):
		print "Pair"
	else:
		print "High Card: %s" % (highcard(cards))
		

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

def rankbynum(c):
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
	return c

def royalflush(hand):
	rank(hand)
	a = hand[0].suit
	for i in hand:
		if i.suit != a:
			return False
	if hand[0].rank == 1 and hand[1].rank == 10 and hand[2].rank == 11 and hand[3].rank == 12 and hand[4].rank == 13:
		return True
	else:
		return False
	
def straightflush(hand):
	rank(hand)
	s = hand[0].suit
	for i in hand:
		if i.suit != s:
			return False
	count = hand[0].rank
	br = False
	for i in hand:
		if i.rank != count: 
			if i.rank != count + 8:
				return False
			else:
				if br == True:
					return False
				else:
					br = True
					count = i.rank
		count = count + 1
		if count > 13:
			count = 1
	return True

def straight(hand):
	rankbynum(hand)
	count = hand[0].rank
	br = False
	for i in hand:
		if i.rank != count: 
			if i.rank != count + 8:
				return False
			else:
				if br == True:
					return False
				else:
					br = True
					count = i.rank
		count = count + 1
		if count > 13:
			count = 1
	return True
	
def flush(hand):
	rank(hand)
	s = hand[0].suit
	for i in hand:
		if i.suit != s:
			return False
	return True

def fourofkind(hand):
	rank(hand)
	used = []
	for i in hand:
		used = used + [i.rank]
	if used.count(hand[0].rank) == 4 or used.count(hand[1].rank) == 4:
		return True
	else:
		return False

def fullhouse(hand):
	rank(hand)
	used = []
	for i in hand:
		used = used + [i.rank]
	for i in hand:
		if used.count(i.rank) != 3 and used.count(i.rank) != 2:
			return False
	return True

def threeofkind(hand):
	rank(hand)
	used = []
	for i in hand:
		used = used + [i.rank]
	hasthree = False
	notfull = False
	for j in used:
		if used.count(j) == 3:
			hasthree = True
		else:
			if used.count(j) != 2:
				notfull = True
	if hasthree and notfull:
		return True
	else:
		return False

def twopair(hand):
	used = []
	for i in hand:
		used = used + [i.rank]
	count = 0
	for j in used:
		if used.count(j) == 2:
			count = count + 1
	if count == 4:
		return True
	else:
		return False
	
def pair(hand):
	used = []
	for i in hand:
		used = used + [i.rank]
	count1 = 0
	count2 = 0
	for j in used:
		if used.count(j) == 2:
			count2 = count2 + 1
		elif used.count(j) == 1:
			count1 = count1 + 1
	if count1 == 3 and count2 == 2:
		return True
	else:
		return False

def highcard(cards):
	high = cards[0]
	for i in cards:
		if i.rank == 1:
			high = i
			break
		if i.rank > high.rank:
			high = i
	return high.__str__()
	
	
main()
