import string

def main():
	startStr = raw_input("Please enter the start time, in HH:MM format: ")
	endStr = raw_input("Please enter the end time, in HH:MM format: ")
	startStrHr, startStrMin = string.split(startStr, ":")
	startHr = eval(startStrHr)
	startMin = eval(startStrMin)
	endStrHr, endStrMin = string.split(endStr, ":")
	endHr = eval(endStrHr)
	endMin = eval(endStrMin)
	if endHr > 9:
		bill = (endHr - 9)*1.75 + endMin*(1.75/60) + (9 - startHr)*2.5 - startMin*(2.5/60)
	else:
		bill = (endHr - startHr)*2.5 - (endMin - startMin)*(2.5/60)
	print "The total bill is $%0.2f." % (bill)

main()
