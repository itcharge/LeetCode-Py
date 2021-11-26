class Solution:
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i
            while j > 0 and arr[j - 1] > temp:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = temp

        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.insertionSort(nums)