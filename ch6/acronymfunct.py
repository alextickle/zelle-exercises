import string

def acronym(phrase):
	a = string.split(phrase)
	acr = ""
	for i in a:
		acr = acr + i[0]
	return string.upper(acr)

print acronym("Alexander Ward Tickle")
