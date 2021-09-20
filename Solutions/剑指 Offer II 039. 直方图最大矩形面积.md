## [剑指 Offer II 039. 直方图最大矩形面积](https://leetcode-cn.com/problems/0ynMMM/)

- 标签：栈、数组、单调栈
- 难度：困难

## 题目大意

给定一个非负整数数组 `heights` ，`heights[i]` 用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

要求：计算出在该柱状图中，能够勾勒出来的矩形的最大面积。

## 解题思路

思路一：枚举「宽度」。一重循环枚举所有柱子，第二重循环遍历柱子右侧的柱子，所得的宽度就是两根柱子形成区间的宽度，高度就是这段区间中的最小高度。然后计算出对应面积，记录并更新最大面积。这样下来，时间复杂度为 $O(n^2)$。

思路二：枚举「高度」。一重循环枚举所有柱子，以柱子高度为当前矩形高度，然后向两侧延伸，遇到小于当前矩形高度的情况就停止。然后计算当前矩形面积，记录并更新最大面积。这样下来，时间复杂度也是 $O(n^2)$。

思路三：利用「单调栈」减少两侧延伸的复杂度。枚举所有柱子，如果当前柱子高度大于等于栈顶柱体的高度，则直接将当前柱体高度入栈。否则则说明当前柱体找到了右边第一个小于当前柱体高度的柱体，那么就可以向右将宽度扩展到此处。出栈后，新的栈顶柱体就是出栈柱体向左找到第一个比其小的高度，那么就可以向左将宽度扩展到此处。此时将栈顶柱体高度出栈来计算以栈顶柱体为高度的矩形面积。

## 代码

```Python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        ans = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                cur = stack.pop(-1)
                left = stack[-1] + 1 if stack else 0
                right = i - 1
                ans = max(ans, (right - left + 1) * heights[cur])
            stack.append(i)

        return ans
```

