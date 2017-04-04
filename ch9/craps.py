from random import *

def main():
	print "This program simulates a game of craps."
	n = input("Please enter the games you would like to simulate: ")
	print
	wins = simNGames(n)
	print "You won %d times out of %d, for a winning percentage of %f%%." % (wins, n, (float(wins)/n) * 100)
	
def simNGames(n):
	wins = 0
	for i in range(n):
		if simOneGame() == True:
			wins = wins + 1
	return wins
	

def simOneGame():
	print
	die1 = randrange(1, 6, 1)
	die2 = randrange(1, 6, 1)
	print "The initial roll is", die1, "and", die2
	total = die1 + die2
	rolltotal = 0
	if total == 2 or total == 3 or total == 12:
		print "\n"
		print "Loss"
		print "------------------------------------------"
		return False
	elif total == 7 or total == 11:
		print "\n"
		print "Win"
		print "------------------------------------------"
		return True
	else:
		while rolltotal != total and rolltotal != 7:
			roll1 = randrange(1, 6, 1)
			roll2 = randrange(1, 6, 1)
			print "Rolled a", roll1, "and", roll2
			rolltotal = roll1 + roll2
		if rolltotal == total:
			print "\n"
			print "Win"
			print "------------------------------------------"            
			return True
		else:
			print "\n"
			print "Loss"
			print "------------------------------------------" 
			return False

main()
			
	
	
	
