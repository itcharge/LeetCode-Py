# 调整为大顶堆
def heapify(nums: [int], index: int, end: int):
	left = index * 2 + 1
	right = left + 1
	while left <= end:
		# 当前节点为非叶子结点
		max_index = index
		if nums[left] > nums[max_index]:
			max_index = left
		if right <= end and nums[right] > nums[max_index]:
			max_index = right
		if index == max_index:
			# 如果不用交换，则说明已经交换结束
			break
		nums[index], nums[max_index] = nums[max_index], nums[index]
		# 继续调整子树
		index = max_index
		left = index * 2 + 1
		right = left + 1

# 初始化大顶堆
def buildMaxHeap(nums: [int]):
	size = len(nums)
	# (size-2) // 2 是最后一个非叶节点，叶节点不用调整
	for i in range((size - 2) // 2, -1, -1):
		heapify(nums, i, size - 1)
	return nums

# 升序堆排序，思路如下：
# 1. 先建立大顶堆
# 2. 让堆顶最大元素与最后一个交换，然后调整第一个元素到倒数第二个元素，这一步获取最大值
# 3. 再交换堆顶元素与倒数第二个元素，然后调整第一个元素到倒数第三个元素，这一步获取第二大值
# 4. 以此类推，直到最后一个元素交换之后完毕。
def maxHeapSort(nums: [int]):
	buildMaxHeap(nums)
	size = len(nums)
	for i in range(size):
		nums[0], nums[size-i-1] = nums[size-i-1], nums[0]
		heapify(nums, 0, size-i-2)
	return nums
	
print(maxHeapSort([2,3,1,4,5]))