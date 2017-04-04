#stats2.py
from math import sqrt

def getNumbers():
	nums = []
	xStr = raw_input("Enter a number (<Enter> to quit) >> ")
	while xStr != "":
		x = eval(xStr)
		nums.append(x)
		xStr = raw_input("Enter a number (<Enter> to quit) >> ")
	return nums
	
def mean(nums):
	sum = 0.0
	for num in nums:
		sum = sum + num
	return sum / len(nums)

def stdDev(nums, xbar):
	sumDevSq = 0.0
	for num in nums:
		dev = num - xbar
		sumDevSq = sumDevSq + dev * dev
	return sqrt(sumDevSq/(len(nums) - 1))

def meanStdDev(nums):
	sumDevSq = 0.0
	for num in nums:
		sum = sum + num
	xbar = sum / len(nums)
	for num in nums:
		dev = num - xbar
		sumDevSq = sumDevsSq + dev * dev
	stdev = sqrt(sumDevSq/ (len(nums) - 1))
	return xbar, stdev

def median(nums):
	nums.sort()
	size = len(nums)
	midPos = size / 2
	if size % 2 == 0:
		median = (nums[midPos] + nums[midPos - 1]) / 2.0
	else:
		median = nums[midPos]
	return median
	
def main():
	print "This program computes mean, median, and standard deviation."
	
	data = getNumbers()
	xbar = mean(data)
	std = stdDev(data, xbar)
	med = median(data)
	
	print "\nThe mean is", xbar
	print "The standard deviation is", std
	print "The median is", med

if __name__ == '__main__': main()
