# testclassSet.py
from classSet import Set

def main():
	a = Set([1, 2, 3, 4, 5])
	print a.elements
	a.addElement(6)
	print a.elements
	a.deleteElement(6)
	print a.elements
	print a.member(5)
	print a.intersection([1,2,3])
	print a.union([1,5,7,8,9])
	print a.subtract([1,2,3,4])

main()
	