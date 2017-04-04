def main():
	import string
	date = raw_input("Enter the date in MM/DD/YYYY format: ")
	months = ["January", "February", "March", "April", "May", "June", "July",
	"August", "September", "October", "November", "December"]
	month, day, year = string.split(date, "/")
	print "The date is %d %s, %d." % (eval(day), months[eval(month) + 1], eval(year))

main()
