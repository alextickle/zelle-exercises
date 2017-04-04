# rballmatches.py
from random import random

def main():
	printIntro()
	probA, probB, n = getInputs()
	winsA, winsB = bestofNGames(n, probA, probB)
	printSummary(winsA, winsB)

def printIntro():
	print "this program simulates (best of n) games of racquetball bewteen two"
	print "platers called A and B. The ability of each player is"
	print "indicated by a probability (0-1) that the player wins"
	print "the point while serving. Player A always has first serve."

def getInputs():
	a = input("What is the probability that player A wins the serve? ")
	b = input("What is the probability that player B wins the serve? ")
	n = input("Best of how many games? ")
	return a, b, n
	
def bestofNGames(n, probA, probB):
	winsA = winsB = 0
	while matchOver(winsA, winsB, n) == False:
		scoreA, scoreB = simOneGame(probA, probB)
		if scoreA > scoreB:
			winsA = winsA + 1
		else:
			winsB = winsB + 1
	return winsA, winsB

def simOneGame(probA, probB):
	serving = "A"
	scoreA = 0
	scoreB = 0
	while not gameOver(scoreA, scoreB):
		if serving == "A":
			if random() < probA:
				scoreA = scoreA + 1
			else:
				serving = "B"
		else:
			if random() < probB:
				scoreB = scoreB + 1
			else:
				serving = "A"
	return scoreA, scoreB

def gameOver(a, b):
	return a==15 or b ==15

def matchOver(winsA, winsB, n):
	return winsA > n/2.0 or winsB > n/2.0

def printSummary(winsA, winsB):
	n = winsA + winsB
	print "\nGames simulated:", n
	print "Wins for A: %d (%0.1f%%)" % (winsA, float(winsA)/n * 100)
	print "Wins for B: %d (%0.1f%%)" % (winsB, float(winsB)/n * 100)
	
if __name__ == '__main__': main()
