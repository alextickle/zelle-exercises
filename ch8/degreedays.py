import string

def main():
	temps = string.split(raw_input("Please enter the daily mean temperatures, separated by commas: "))
	cooldays = 0
	hotdays = 0
	for i in temps:
		if int(i) > 80:
			cooldays = cooldays + int(i) - 80
		elif int(i) < 60:
			hotdays = hotdays - int(i) + 60
	print hotdays, cooldays

main()
