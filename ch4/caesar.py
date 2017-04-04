def main():
	import string
	message = raw_input("Please enter a message: ")
	new = ""
	for ch in message:
		new = new + chr(ord(ch) + 2)
	print "The Caesar encoded message is", new

main()