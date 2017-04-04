def search(x, nums):
	low = 0
	high = len(nums - 1)
	while low <= high:
		mid = (low + high)/2
		item = nums[mid]
		if x == item:
			return mid
		elif x < item:
			high = mid - 1
		else"
			low = mid + 1
	return -1