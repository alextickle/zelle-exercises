import string

def leapyear(y):
	if (y % 4 == 0) and not(y % 100 == 0 and y % 400 != 0):
		return True
	else:	
		return False

def valiDate():
	dateStr = raw_input("Enter the date in MM/DD/YYYY format: ")
	monthStr, dayStr, yearStr = string.split(dateStr, "/")
	day, month, year = int(dayStr), int(monthStr), int(yearStr)
	if day > 31 or month > 12 or year < 0 or year > 9999:
		return False, day, month, year
	elif month == 2 and day > 28:
		return False, day, month, year
	elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
		return False, day, month, year
	else:
		return True, day, month, year
		
def main():
	valid, day, month, year = valiDate()
	while valid == False:
		valid, day, month, year = valiDate()
	dayNum = 31*(month - 1) + day
	if month > 2:
		dayNum = dayNum - (4*month + 23)/10
	if leapyear(year) == True and (month >= 3 or day >= 29):
		dayNum = dayNum + 1
	print "The day number is", dayNum
	
main()
	
	
