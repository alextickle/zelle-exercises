def toNumbers(strList):
	valWord = 0
	valList = 0
	for word in strList:
		for chr in word:
			valWord = valWord + ord(chr)
		valList = valList + valWord
		valWord = 0
	return valList
		
print toNumbers(["hc", "fc", "fc", "de"])
	
