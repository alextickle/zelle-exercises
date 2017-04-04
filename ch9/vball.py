# vball.py
import random
import math

def main():
	printIntro()
	n, probA, probB = getInputs()
	winsA, winsB = simNGames(n, probA, probB)
	printSummary(winsA, winsB)

def printIntro():
	print "This program simulates a game of volleyball between two players A and B"
	print "with given serve win probabilities."

def getInputs():
	n = input("Please enter the number of matches to simulate: ")
	probA = input("Please the probability that A scores on his/her serve (0-1): ")
	probB = input("Please the probability that B scores on his/her serve (0-1): ")
	return n, probA, probB

def simNGames(n, probA, probB):
	winsA = winsB = 0
	for i in range(n):
		scoreA, scoreB = simOneGame(probA, probB)
		if scoreA > scoreB:
			winsA = winsA + 1
		else:
			winsB = winsB + 1
	return winsA, winsB

def simOneGame(probA, probB):
	scoreA = scoreB = 0
	serving = "A"
	while gameOver != True:
		if serving == "A":
			if random.random() < probA:
				scoreA = scoreA + 1
			else:
				serving = "B"
		else:
			if random.random() < probB:
				scoreB = scoreB + 1
			else:
				serving = "A"
	return scoreA, scoreB
	
	return scoreA, scoreB

def gameOver(scoreA, scoreB):
	if abs(scoreA - scoreB) >= 2 and (scoreA > 15 or scoreB > 15):
		return True
	else:
		return False
		
def printSummary(winsA, winsB):
	print "Wins for A: %d (%0.1f%%)" % (winsA, float(winsA)/n * 100)
	print "Wins for B: %d (%0.1f%%)" % (winsB, float(winsB)/n * 100)

	
def vballmain():
	printIntrov()
	n, probA, probB = getInputsv()
	winsA, winsB = simNGamesv(n, probA, probB)
	printSummaryv(winsA, winsB)

def printIntrov():
	print "This program simulates a game of volleyball between two players A and B"
	print "with given serve win probabilities."

def getInputsv():
	n = input("Please enter the number of matches to simulate: ")
	probA = input("Please the probability that A scores on his/her serve (0-1): ")
	probB = input("Please the probability that B scores on his/her serve (0-1): ")
	return n, probA, probB

def simNGamesv(n, probA, probB):
	winsA = winsB = 0
	for i in range(n):
		scoreA, scoreB = simOneGame(probA, probB)
		if scoreA > scoreB:
			winsA = winsA + 1
		else:
			winsB = winsB + 1
	return winsA, winsB

def simOneGamev(probA, probB):
	scoreA = scoreB = 0
	serving = "A"
	while gameOverv != True:
		if serving == "A":
			if random.random() < probA:
				scoreA = scoreA + 1
			else:
				serving = "B"
		else:
			if random.random() < probB:
				scoreB = scoreB + 1
			else:
				serving = "A"
	return scoreA, scoreB
	
	return scoreA, scoreB

def gameOverv(scoreA, scoreB):
	if abs(scoreA - scoreB) >= 2 and (scoreA > 15 or scoreB > 15):
		return True
	else:
		return False
		
def printSummaryv(winsA, winsB):
	print "Wins for A: %d (%0.1f%%)" % (winsA, float(winsA)/n * 100)
	print "Wins for B: %d (%0.1f%%)" % (winsB, float(winsB)/n * 100)

	main()
		
