import random

def randomPartition(nums: [int], low: int, high: int):
		i = random.randint(low, high)
		nums[i], nums[high] = nums[high], nums[i]
		return partition(nums, low, high)

def partition(nums: [int], low: int, high: int):
	x = nums[high]
	i = low-1
	for j in range(low, high):
		if nums[j] <= nums[high]:
			i += 1
			nums[i], nums[j] = nums[j], nums[i]
	nums[i+1], nums[high] = nums[high], nums[i+1]
	return i+1

def quickSort(nums: [int], low: int, high: int):
	n = len(nums)
	if low < high:
		pi = randomPartition(nums, low, high)
		quickSort(nums, low, pi-1)
		quickSort(nums, pi+1, high)

	return nums
				
print(quickSort([1,3,2,5,6,4], 0, 5))