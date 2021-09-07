## [剑指 Offer 57 - II. 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)

- 标签：数学、双指针、枚举
- 难度：简单

## 题目大意

给定一个正整数 `target`。

要求：输出所有和为 `target` 的连续正整数序列（至少含有两个数）。序列中的数字由小到大排列，不同序列按照首个数字从小到大排列。

## 解题思路

滑动窗口求解。具体做法如下：

- 初始化窗口，令 `left = 1`，`right = 2`。
- 计算 `sum = (left + right) * (right - left + 1) // 2`。
- 如果 `sum == target`，时，将其加入答案数组中。
- 如果 `sum < target` 时，说明需要扩大窗口，则 `right += 1`。
- 如果 `sum > target` 时，说明需要缩小窗口，则 `left += 1`。
- 直到 `left >= right` 时停止，返回答案数组。

## 代码

```Python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right = 1, 2
        res = []
        while left < right:
            sum = (left + right) * (right - left + 1) // 2
            if sum == target:
                arr = []
                for i in range(0, right - left + 1):
                    arr.append(i + left)
                res.append(arr)
                left += 1
            elif sum < target:
                right += 1
            else:
                left += 1
        return res
```

