def recBinSearch(x, nums, low, high):
	if low > high:
		return - 1
	mid = (low + high) / 2
	item = nums[mid]
	if item == x:
		return mid
	elif x < item:
		return recBinSearch(x, nums, low, mid - 1)
	else:
		return recBinSearch(x, nums, mid + 1, high)
		