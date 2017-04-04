def removeDup(list):
	for num in list:
		count = 0
		for i in list:
			if i == num:
				count = count + 1
		if count > 1:
			list.remove(num)
	return list
		
	

def main():
	list = [1, 2, 6, 3, 5, 2, 4, 4, 3, 4, 5]
	print removeDup(list)

main()
