def main():
	import string
	fname = string.split(string.lower(raw_input("Please enter your full name: ")))
	letters = "abcdefghijklmnopqrstuvwxyz"
	nameval = 0
	for word in fname:
		for ch in word:
			nameval = nameval + string.find(letters, ch) + 1
	print "The value of your name is", nameval

main()
