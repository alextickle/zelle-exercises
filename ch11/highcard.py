# highcard.py
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
	print highcard(cards)
		
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
	


