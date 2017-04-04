# rballshutouts.py
from random import random

def main():
	printIntro()
	probA, probB, n = getInputs()
	winsA, winsB, shutoutsA, shutoutsB = bestofNGames(n, probA, probB)
	printSummary(winsA, winsB, shutoutsA, shutoutsB)

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
	winsA = winsB = shutoutsA = shutoutsB = 0
	while matchOver(winsA, winsB, n) == False:
		scoreA, scoreB, shtotA, shtotB = simOneGame(probA, probB)
		if scoreA > scoreB:
			winsA = winsA + 1
		else:
			winsB = winsB + 1
		if shtotA == True:
			shutoutsA = shutoutsA + 1
		elif shtotB == True:
			shutoutsB = shutoutsB + 1
	return winsA, winsB, shutoutsA, shutoutsB

def simOneGame(probA, probB):
	serving = "A"
	scoreA = 0
	scoreB = 0
	shutoutA = False
	shutoutB = False
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
	if scoreA == 0:
		shutoutB = True
	elif scoreB == 0:
		shutoutA = True
	shutout = True
	return scoreA, scoreB, shutoutA, shutoutB

def gameOver(a, b):
	return a==15 or b ==15

def matchOver(winsA, winsB, n):
	return winsA > n/2.0 or winsB > n/2.0

def printSummary(winsA, winsB, shutoutsA, shutoutsB):
	n = winsA + winsB
	print "\nGames simulated:", n
	print "Wins for A: %d (%0.1f%%)" % (winsA, float(winsA)/n * 100)
	print "Wins for B: %d (%0.1f%%)" % (winsB, float(winsB)/n * 100)
	print "Shutouts for A: %d (%0.1F%%)" % (shutoutsA, float(shutoutsA)/n * 100)
	print "Shutouts for B: %d (%0.1F%%)" % (shutoutsB, float(shutoutsB)/n * 100)
	
if __name__ == '__main__': main()
