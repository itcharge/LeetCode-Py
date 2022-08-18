class Solution:
    def radixSort(self, arr):
        # 桶的大小为所有元素的最大位数
        size = len(str(max(arr)))

        # 从低位到高位依次遍历每一位，以各个数位值为索引，对数组进行按数位排序
        for i in range(size):
            # 使用一个长度为 10 的桶来存放各个位上的元素
            buckets = [[] for _ in range(10)]
            # 遍历数组元素，根据元素对应位上的值，将其存入对应位的桶中
            for num in arr:
                buckets[num // (10 ** i) % 10].append(num)
            # 清空原始数组
            arr.clear()
            # 从桶中依次取出对应元素，并重新加入到原始数组
            for bucket in buckets:
                for num in bucket:
                    arr.append(num)

        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.radixSort(nums)