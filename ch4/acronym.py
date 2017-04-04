def main():
	import string
	phrase = raw_input("Please enter the phrase: ")
	a = string.split(phrase)
	acr = ""
	for i in a:
		acr = acr + i[0]
	print "The acronym is %s." % (string.upper(acr))

main()