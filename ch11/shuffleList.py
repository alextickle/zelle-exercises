import random

def shuffle(myList):
	for i in range(len(myList)):
		num = random.randrange(len(myList))
		myList[i], myList[num] = myList[num], myList[i]
	return myList

def main():
	myList = [1, 4, 5, 2, 4, 5, 4, 2]
	print shuffle(myList)

main()
	
