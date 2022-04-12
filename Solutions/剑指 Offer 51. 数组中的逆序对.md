# [剑指 Offer 51. 数组中的逆序对](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/)

- 标签：树状数组、线段树、数组、二分查找、分治、有序集合、归并排序
- 难度：困难

## 题目大意

给定一个数组 `nums`。

要求：计算出数组中的逆序对的总数。

## 解题思路

可以用树状数组解决。

数组 `tree[i]` 表示数字 `i` 是否在序列中出现过，如果数字 `i` 已经存在于序列中，`tree[i] = 1`，否则 `tree[i] = 0`。按序列从左到右将值为 `nums[i]` 的元素当作下标为`nums[i]`，赋值为 `1` 插入树状数组里，这时，比 `nums[i]` 大的数个数就是 `i + 1 - query(a)`。将全部结果累加起来就是逆序数了。

## 代码

```Python
import bisect

class BinaryIndexTree:

    def __init__(self, n):
        self.size = n
        self.tree = [0 for _ in range(n + 1)]

    def lowbit(self, index):
        return index & (-index)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += self.lowbit(index)

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        size = len(nums)
        sort_nums = sorted(nums)
        for i in range(size):
            nums[i] = bisect.bisect_left(sort_nums, nums[i]) + 1

        bit = BinaryIndexTree(size)
        ans = 0
        for i in range(size):
            bit.update(nums[i], 1)
            ans += (i + 1 - bit.query(nums[i]))
        return ans
```

