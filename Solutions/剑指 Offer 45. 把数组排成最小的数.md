## [剑指 Offer 45. 把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)

- 标签：贪心、字符串、排序
- 难度：中等

## 题目大意

给定一个非负整数数组 `nums`。

要求：将数组中的数字拼接起来排成一个数，打印能拼接出的所有数字中的最小的一个。

## 解题思路

本质上是给数组进行排序。假设 `x`、`y` 是数组 `nums` 中的两个元素。如果拼接字符串 `x + y > y + x`，则 `x < y `。`x` 应该排在 `y` 前面。反之，则 `x > y`。

按照上述规则，对原数组进行排序。这里使用了 `functools.cmp_to_key` 自定义排序函数。

## 代码

```Python
import functools

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1

        nums_s = list(map(str, nums))
        nums_s.sort(key=functools.cmp_to_key(cmp))
        return ''.join(nums_s)
```

