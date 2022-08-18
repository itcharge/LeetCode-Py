class Solution:
    def countingSort(self, arr):
        # 计算待排序序列中最大值元素 arr_max 和最小值元素 arr_min
        arr_min, arr_max = min(arr), max(arr)
        # 定义计数数组 counts，大小为 最大值元素 - 最小值元素 + 1
        size = arr_max - arr_min + 1
        counts = [0 for _ in range(size)]
        
        # 统计值为 num 的元素出现的次数
        for num in arr:
            counts[num - arr_min] += 1
        
        # 计算元素排名
        for j in range(1, size):
            counts[j] += counts[j - 1]

        # 反向填充目标数组
        res = [0 for _ in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            # 根据排名，将 arr[i] 放在数组对应位置
            res[counts[arr[i] - arr_min] - 1] = arr[i]
            # 将 arr[i] 的对应排名减 1
            counts[arr[i] - arr_min] -= 1

        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.countingSort(nums)