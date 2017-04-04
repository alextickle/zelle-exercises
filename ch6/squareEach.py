def squareEach(nums):
	count = -1
	for i in nums:
		count = count + 1
		nums[count] = i**2
	return nums

print squareEach([3, 4, 5, 6, 7, 3])
