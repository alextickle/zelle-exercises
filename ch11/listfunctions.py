# listfunctions.py

def count(myList, x):
	count = 0
	for i in myList:
		if i == x:
			count = count + 1
	return count
	
def isin(myList, x):
	for i in myList:
		if i == x:
			return True
	return False
	
def index(myList, x):
	ind = 0
	for i in myList:
		if i == x:
			return ind
		ind = ind + 1

def reverse(myList):
	list2 = []
	for i in range(len(myList)):
		list2 = list2 + [myList[-(i + 1)]]
	return list2

def sort(myList):
	doOver = True
	while doOver:
		doOver = False
		print myList
		for i in range(len(myList) - 1):
			if myList[i] > myList[i + 1]:
				myList[i], myList[i + 1] = myList[i + 1], myList[i]
				doOver = True
	return myList
		
		
def main():
	myList = [3, 4, 5, 6, 3, 4, 2, 3]
	print myList
	print sort(myList)

main()
			
