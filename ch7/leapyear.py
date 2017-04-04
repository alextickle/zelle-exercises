import string

def valiDate(dateStr):
	day, month, year = eval(string.split(dateStr, "/"))
	print day, month, year

valiDate("02/03/2010")
	
	#if day > 31 or month > 12 or year < 0 or year > 9999:
		#return False
	#elif month = 2 and
