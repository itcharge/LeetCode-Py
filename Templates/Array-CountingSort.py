class Solution:
    def countingSort(self, arr):
        arr_min, arr_max = min(arr), max(arr)
        size = arr_max - arr_min + 1
        counts = [0 for _ in range(size)]

        for num in arr:
            counts[num - arr_min] += 1
        for j in range(1, size):
            counts[j] += counts[j - 1]

        res = [0 for _ in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            res[counts[arr[i] - arr_min] - 1] = arr[i]
            counts[arr[i] - arr_min] -= 1

        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.countingSort(nums)