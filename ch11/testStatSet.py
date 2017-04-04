# testStatSet.py
from classStatSet import StatSet

def main():
	a = StatSet()
	for i in range(20):
		a.addNumber(i)
	print a.mean()
	print a.median()
	print a.stdDev()
	print a.count()
	print a.min()
	print a.max()

main()
	
