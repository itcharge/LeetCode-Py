class Solution:
    def selectionSort(self, arr):
        for i in range(len(arr) - 1):
            # 记录未排序序列中最小数的索引
            min_i = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_i]:
                    min_i = j
            # 如果找到最小数，将 i 位置上元素与最小数位置上元素进行交换
            if i != min_i:
                arr[i], arr[min_i] = arr[min_i], arr[i]
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.selectionSort(nums)