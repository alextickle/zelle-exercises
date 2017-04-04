import random

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

	
print vballmain(.5, .6, 100)
