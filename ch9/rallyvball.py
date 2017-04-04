import math
import random

def rallymain():
	probA, probB, n = getInputs()
	winsA, winsB = simNGames(probA, probB, n)
	printSummary(winsA, winsB)

def getInputs():
	a = input("Please enter the probability that A wins on his serve (0-1): ")
	b = input("Please enter the probability that B wins on his serve (0-1): ")
	n = input("Please enter the number of matches to simulate: ")
	return a, b, n

def printSummary(x, y):
	print "Wins for A: %d " % (x)
	print "Wins for B: %d " % (y)
	
def simNGames(probA, probB, n):
	winsA = winsB = 0
	for i in range(n):
		if simOneGame(probA, probB) == 'A':
			winsA = winsA + 1
		else:
			winsB = winsB + 1
	return winsA, winsB

def simOneGame(probA, probB):
	serving = 'A'
	scoreA = scoreB = 0
	winner = ""
	while gameOver(scoreA, scoreB) == False:
		if serving == 'A':
			if random.random() <= probA:
				scoreA = scoreA + 1
			else:
				scoreB = scoreB + 1
				serving = 'B'
		else:
			if random.random() <= probB:
				scoreB = scoreB + 1
			else:
				scoreA = scoreA + 1
				serving = 'A'
	if scoreA > scoreB:
		winner = 'A'
	else:
		winner = 'B'
	return winner
	
def gameOver(scoreA, scoreB):
	if ((scoreA >= 30 or scoreB >= 30) and abs(scoreA - scoreB) >= 2) == True:
		return True
	else:
		return False

rallymain()
	
