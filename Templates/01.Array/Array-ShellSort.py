class Solution:
    def shellSort(self, arr):
        size = len(arr)
        gap = size // 2
        # 按照 gap 分组
        while gap > 0:
            # 对每组元素进行插入排序
            for i in range(gap, size):
                # temp 为每组中无序序列第 1 个元素
                temp = arr[i]
                j = i
                # 从右至左遍历每组中的有序序列元素
                while j >= gap and arr[j - gap] > temp:
                    # 将每组有序序列中插入位置右侧的元素依次在组中右移一位
                    arr[j] = arr[j - gap]
                    j -= gap
                # 将该元素插入到适当位置
                arr[j] = temp
            # 缩小 gap 间隔
            gap = gap // 2
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.shellSort(nums)