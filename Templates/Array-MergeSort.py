class Solution:
    def merge(self, left_arr, right_arr):
        arr = []
        while left_arr and right_arr:
            if left_arr[0] <= right_arr[0]:
                arr.append(left_arr.pop(0))
            else:
                arr.append(right_arr.pop(0))
        while left_arr:
            arr.append(left_arr.pop(0))
        while right_arr:
            arr.append(right_arr.pop(0))
        return arr

    def mergeSort(self, arr):
        size = len(arr)
        if size < 2:
            return arr
        mid = len(arr) // 2
        left_arr, right_arr = arr[0: mid], arr[mid:]
        return self.merge(self.mergeSort(left_arr), self.mergeSort(right_arr))

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)