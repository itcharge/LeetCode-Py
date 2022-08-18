class Solution:
    def insertionSort(self, arr):
        # 遍历无序序列
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i
            # 从右至左遍历有序序列
            while j > 0 and arr[j - 1] > temp:
                # 将有序序列中插入位置右侧的元素依次右移一位
                arr[j] = arr[j - 1]
                j -= 1
            # 将该元素插入到适当位置
            arr[j] = temp

        return arr

    def bucketSort(self, arr, bucket_size=5):
        # 计算待排序序列中最大值元素 arr_max 和最小值元素 arr_min
        arr_min, arr_max = min(arr), max(arr)
        # 定义桶的个数为 (最大值元素 - 最小值元素) // 每个桶的大小 + 1
        bucket_count = (arr_max - arr_min) // bucket_size + 1
        # 定义桶数组 buckets
        buckets = [[] for _ in range(bucket_count)]

        # 遍历原始数组元素，将每个元素装入对应区间的桶中
        for num in arr:
            buckets[(num - arr_min) // bucket_size].append(num)

        # 对每个桶内的元素单独排序，并合并到 res 数组中
        res = []
        for bucket in buckets:
            self.insertionSort(bucket)
            res.extend(bucket)

        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bucketSort(nums)