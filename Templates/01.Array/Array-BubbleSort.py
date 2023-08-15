class Solution:
    def bubbleSort(self, arr):
        # 第 i 趟遍历
        for i in range(len(arr) - 1):
            flag = False    # 是否发生交换的标志位
            # 从序列中前 n - i + 1 个元素的第 1 个元素开始，相邻两个元素进行比较
            for j in range(len(arr) - i - 1):
                # 相邻两个元素进行比较，如果前者大于后者，则交换位置
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = True
            if not flag:    # 此趟遍历未交换任何元素，直接跳出
                break
        
        return arr
    
    def sortArray(self, nums):
        return self.bubbleSort(nums)
    
    
print(Solution().sortArray([5, 2, 3, 6, 1, 4]))