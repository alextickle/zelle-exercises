def main():
	n = input("Please enter the number of numbers to average: ")
	sum = 0
	for i in range(n):
		a = input("Please enter the number: ")
		sum = sum + a
	print "The average of these numbers is", float(sum)/n

main()