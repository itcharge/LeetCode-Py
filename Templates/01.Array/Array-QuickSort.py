import random


class Solution:
    def randomPartition(self, arr: [int], low: int, high: int):
        i = random.randint(low, high)
        arr[i], arr[high] = arr[high], arr[i]
        return self.partition(arr, low, high)

    def partition(self, arr: [int], low: int, high: int):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.randomPartition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums, 0, len(nums) - 1)