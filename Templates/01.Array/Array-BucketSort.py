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

    def bucketSort(self, arr, bucket_size=5):
        arr_min, arr_max = min(arr), max(arr)
        bucket_count = (arr_max - arr_min) // bucket_size + 1
        buckets = [[] for _ in range(bucket_count)]

        for num in arr:
            buckets[(num - arr_min) // bucket_size].append(num)

        res = []
        for bucket in buckets:
            self.insertionSort(bucket)
            res.extend(bucket)

        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bucketSort(nums)