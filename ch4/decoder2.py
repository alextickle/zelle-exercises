def main():
	import string
	todecode = raw_input("Please enter the message to decode: ")
	a = string.split(todecode)
	message = []
	for i in a:
		i = chr(eval(i))
		message = message + [i]
	final = string.join(message)
	print final
main()
	