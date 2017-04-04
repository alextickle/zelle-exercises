# testchangelist.py
def main():
	a = ["a", "b", "c", "d"]
	count = 0
	for i in a:
		a[count] = "c"
		count = count + 1
	print a

main()
	
