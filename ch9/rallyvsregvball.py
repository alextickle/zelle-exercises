import math
import random

def rallymain(probAr, probBr, nr):
	winsAr, winsBr = simNGamesr(probAr, probBr, nr)
	return winsAr, winsBr
	
def simNGamesr(probAr, probBr, nr):
	winsAr = winsBr = 0
	for i in range(nr):
		if simOneGamer(probAr, probBr) == 'A':
			winsAr = winsAr + 1
		else:
			winsBr = winsBr + 1
	return winsAr, winsBr

def simOneGamer(probAr, probBr):
	serving = 'A'
	scoreAr = scoreBr = 0
	winner = ""
	while gameOverr(scoreAr, scoreBr) == False:
		if serving == 'A':
			if random.random() <= probAr:
				scoreAr = scoreAr + 1
			else:
				scoreBr = scoreBr + 1
				serving = 'B'
		else:
			if random.random() <= probBr:
				scoreBr = scoreBr + 1
			else:
				scoreAr = scoreAr + 1
				serving = 'A'
	if scoreAr > scoreBr:
		winner = 'A'
	else:
		winner = 'B'
	return winner
	
def gameOverr(scoreAr, scoreBr):
	if ((scoreAr >= 30 or scoreBr >= 30) and abs(scoreAr - scoreBr) >= 2) == True:
		return True
	else:
		return False


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

def vballmain(probAv, probBv, nv):
	winsAv, winsBv = simNGamesv(nv, probAv, probBv)
	return winsAv, winsBv
	

def simNGamesv(nv, probAv, probBv):
	winsAv = winsBv = 0
	for i in range(nv):
		scoreAv, scoreBv = simOneGamev(probAv, probBv)
		if scoreAv > scoreBv:
			winsAv = winsAv + 1
		else:
			winsBv = winsBv + 1
	return winsAv, winsBv

def simOneGamev(probAv, probBv):
	scoreAv = scoreBv = 0
	serving = "A"
	while gameOverv(scoreAv, scoreBv) != True:
		if serving == "A":
			if random.random() < probAv:
				scoreAv = scoreAv + 1
			else:
				serving = "B"
		else:
			if random.random() < probBv:
				scoreBv = scoreBv + 1
			else:
				serving = "A"
	return scoreAv, scoreBv
	
	return scoreAv, scoreBv

def gameOverv(scoreAv, scoreBv):
	if abs(scoreAv - scoreBv) >= 2 and (scoreAv > 15 or scoreBv > 15):
		return True
	else:
		return False
	
def main():
	print "This program illustrates the different ways in which serve win probability affects overall wins for rally and non-rally scoring"
	n = input("Please enter a number of games to compare: ")
	a = input("Enter the probability of A winning the serve: ")
	b = input("Enter the probability of B winning the serve: ")
	winsAr, winsBr = rallymain(a, b, n)
	winsAv, winsBv = vballmain(a, b, n)
	print "With rally scoring A won %d games and B won %d games." % (winsAr, winsBr)
	print "And with non-rally scoring, A won %d games and B won %d games." % (winsAv, winsBv)

main()
