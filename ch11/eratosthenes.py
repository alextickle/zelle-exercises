def main():
	n = input("Please enter a value for n: ")
	list = []
	primes = []
	for i in range(2, n + 1, 1):
		list = list + [i]
	factor = 0
	while len(list) != 0:
		primes = primes + [list[0]]
		factor = list[0]
		list.remove(list[0])
		for i in list:
			if i % factor == 0:
				list.remove(i)
	print primes

main()