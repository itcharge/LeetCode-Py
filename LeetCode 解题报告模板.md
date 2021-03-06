

# [0026. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

## 题目相关

- 标签：数组
- 关键词：双指针

## 题目大意

给定一个有序数组，删除重复元素，并输出去除重复元素之后数组的长度。要求不能使用额外的数组空间

## 解题思路

因为数组是有序的，那么重复的元素一定会相邻。

删除重复元素，实际上就是将不重复的元素移到数组左侧。考虑使用 2 个指针，一个在前边记作 p，指向去除重复元素后的数组的末尾位置。一个在后边记作 q，指向当前元素。

具体算法如下：

1. p 指针置为 0，q 指针置为 1。
2. 比较 p 位置元素和 q 位置上元素是否相等。
   1. 如果相等，将 q 后移 1 位。
   2. 如果不相等，则将 q 位置的元素复制到 p+1 位置上，p 后移 1 位，q 后移 1 位。（此时相当于过滤掉了 p+1~q 位置上的重复元素）
3. 重复上述过程，直到 q 等于数组长度。
4. 返回 p+1 即为新数组长度。

## 代码

```Python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        p, q = 0, 1
        while (q < len(nums)):
            if nums[p] != nums[q]:
                nums[p+1] = nums[q]
                p += 1
            q += 1
        return p+1
```

