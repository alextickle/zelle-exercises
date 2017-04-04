def main():
	import string
	sent = raw_input("Please enter a sentence: ")
	a = string.split(sent)
	letters = 0
	words = 0
	for word in a:
		words = words + 1
		for ch in word:
			letters = letters + 1
	print "The average word length is", letters/float(words)

main()
