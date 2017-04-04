# decktest.py
from classPlayingCard import PlayingCard
from classDeck import Deck
import string

def main():
	n = input("How many cards would you like to deal out? ")
	d = Deck()
	d.shuffle()
	cards = []
	for i in range(n):
		cards = cards + [d.dealCard()]
	for i in cards:
		print i.__str__()

main()
		
