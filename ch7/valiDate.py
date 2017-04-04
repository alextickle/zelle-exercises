import string

def valiDate(dateStr):
	dayStr, monthStr, yearStr = string.split(dateStr, "/")
	day, month, year = int(dayStr), int(monthStr), int(yearStr)
	if day > 31 or month > 12 or year < 0 or year > 9999:
		return False
	elif month == 2 and day > 28:
		return False
	elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
		return False
	else:
		return True
print valiDate("02/29/2010")
	
	
