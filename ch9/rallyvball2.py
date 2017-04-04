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

print rallymain(.6, .6, 100)
	
