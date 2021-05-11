# LeetCode-Py

LeetCode 题解, Solutions to LeetCode by Python

# LeetCode 刷题顺序和技巧

# 1. LeetCode 刷题顺序

如果是新手刷题的话，推荐先从简单等级的算法题开始刷起。等简单题上手熟练之后，再开始按照标签类别，刷中等难度的题。中等难度的题刷差不多之后，可以考虑刷面试题 or 难题。

其实 LeetCode 官方网站上就有整理好的刷题清单。链接为：[https://leetcode-cn.com/leetbook/](https://leetcode-cn.com/leetbook/)

我这里稍微做了一下整理。推荐刷题顺序如下：

1. [初级算法](https://leetcode-cn.com/leetbook/detail/top-interview-questions-easy/)
2. [数组类算法](https://leetcode-cn.com/leetbook/detail/all-about-array/)
3. [数组和字符串](https://leetcode-cn.com/leetbook/detail/array-and-string/)
4. [链表类算法](https://leetcode-cn.com/leetbook/detail/linked-list/)
5. [哈希表](https://leetcode-cn.com/leetbook/detail/hash-table/)
6. [队列 & 栈](https://leetcode-cn.com/leetbook/detail/queue-stack/)
7. [递归](https://leetcode-cn.com/leetbook/detail/recursion/)
8. [二分查找](https://leetcode-cn.com/leetbook/detail/binary-search/)
9. [二叉树](https://leetcode-cn.com/leetbook/detail/data-structure-binary-tree/)
10. [中级算法](https://leetcode-cn.com/leetbook/detail/top-interview-questions-medium/)
11. [高级算法](https://leetcode-cn.com/leetbook/detail/top-interview-questions-hard/)
12. [算法面试题汇总](https://leetcode-cn.com/leetbook/detail/top-interview-questions/)

# 2. LeetCode 刷题技巧

## 2.1 「5 分钟思考法」

「5 分钟思考法」意思就是如果一道题如果 5 分钟之内有思路，就立即动手解题。如果 5 分钟之后还没有思路，就直接去看题解。然后根据题解的思路，自己去实现代码。如果发现自己看了题解也无法实现代码，就认真阅读题解的代码，并理解代码的逻辑。

刷题其实跟英语里边的背单词过程是类似的。

一开始，先学简单的单词，掌握了基本词汇之后，再学习词组，学习句子，然后再看文章。而且，背单词的时候也不是背一遍就会了。而是不断的重复记忆。

算法刷题也是一样，零基础刷题的时候，不要过分纠结怎么自己就想不出来算法的解法，怎么就想不到更加高效的方法。学英语的时候，不也是从第一个字母开始学起的嘛。

一开始的时候，不会做的题就去看题解，尽可能的快速入门。

## 2.2 「重复刷题」

算法题有时候一遍刷过去，过的时间长了可能就忘了，看到之前做的题不能够立马想到解题思路。这其实还是跟背单词一样，单词也不是看一遍就完全记住了。所以题目刷完一遍并不是结束了，还需要不断的回顾。

而且，一道题目可能有多种解法，还可能有复杂度更低的算法思路。

最开始做的时候，可能是一种思路，再做第二遍的时候，可能会想到了新的解法，新的优化方式等等。

所以，算法题一遍之后遇见不会的，还可以多刷几遍，不断加深理解。

##  2.3 「写解题报告」

刷算法题，有一个十分有用的捷径，就是「写解题报告」。如果你刷完一道题，能把这道题的解题步骤，做题思路用通俗易懂的话写成解题报告，那么这道题就算是掌握了。其实就相当于「费曼学习法」的思维。这样，也可以减少刷题的遍数，遇到之前刷过的题，但一时之间没有思路的，可以看看自己之前的解题报告。这样就节省了大量重复刷题的时间。



# 3. LeetCode 题解（已解决 127 道）
 | 题号 | 标题 | 题解 | 标签 | 难度 |
| :------ | :------ | :------ | :------ | :------ |
| 0001 | [两数之和](https://leetcode-cn.com/problems/two-sum/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0001.%20%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C.md) | 数组、哈希表 | 简单 |
| 0002 | [两数相加](https://leetcode-cn.com/problems/add-two-numbers/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0002.%20%E4%B8%A4%E6%95%B0%E7%9B%B8%E5%8A%A0.md) | 递归、链表、数学 | 简单 |
| 0003 | [无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0003.%20%E6%97%A0%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E4%B8%B2.md) | 字符串、哈希表、双指针、字符串、滑动窗口 | 简单 |
| 0005 | [最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0005.%20%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.md) | 字符串、动态规划 | 简单 |
| 0007 | [整数反转](https://leetcode-cn.com/problems/reverse-integer/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0007.%20%E6%95%B4%E6%95%B0%E5%8F%8D%E8%BD%AC.md) | 数学 | 简单 |
| 0008 | [字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0008.%20%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%BD%AC%E6%8D%A2%E6%95%B4%E6%95%B0%20%28atoi%29.md) | 数学、字符串 | 简单 |
| 0009 | [回文数](https://leetcode-cn.com/problems/palindrome-number/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0009.%20%E5%9B%9E%E6%96%87%E6%95%B0.md) | 数学 | 简单 |
| 0013 | [罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0013.%20%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97%E8%BD%AC%E6%95%B4%E6%95%B0.md) | 数学、字符串 | 简单 |
| 0014 | [最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0014.%20%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%89%8D%E7%BC%80.md) | 字符串 | 简单 |
| 0015 | [三数之和](https://leetcode-cn.com/problems/3sum/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0015.%20%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.md) | 数组、双指针 | 中等 |
| 0018 | [四数之和](https://leetcode-cn.com/problems/4sum/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0018.%20%E5%9B%9B%E6%95%B0%E4%B9%8B%E5%92%8C.md) | 数组、哈希表、双指针 | 中等 |
| 0019 | [删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0019.%20%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%AC%20N%20%E4%B8%AA%E7%BB%93%E7%82%B9.md) | 链表、双指针 | 简单 |
| 0020 | [有效的括号](https://leetcode-cn.com/problems/valid-parentheses/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0020.%20%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.md) | 栈、字符串 | 简单 |
| 0024 | [两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0024.%20%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.md) | 递归、链表 | 简单 |
| 0027 | [移除元素](https://leetcode-cn.com/problems/remove-element/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0027.%20%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.md) | 数组、双指针 | 简单 |
| 0028 | [实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0028.%20%E5%AE%9E%E7%8E%B0%20strStr%28%29.md) | 字符串、双指针 | 简单 |
| 0034 | [在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0034.%20%E5%9C%A8%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E6%9F%A5%E6%89%BE%E5%85%83%E7%B4%A0%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%92%8C%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E4%BD%8D%E7%BD%AE.md) | 数组、二分查找 | 中等 |
| 0035 | [搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0035.%20%E6%90%9C%E7%B4%A2%E6%8F%92%E5%85%A5%E4%BD%8D%E7%BD%AE.md) | 数组、二分查找 | 简单 |
| 0036 | [有效的数独](https://leetcode-cn.com/problems/valid-sudoku/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0036.%20%E6%9C%89%E6%95%88%E7%9A%84%E6%95%B0%E7%8B%AC.md) | 哈希表 | 简单 |
| 0038 | [外观数列](https://leetcode-cn.com/problems/count-and-say/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0038.%20%E5%A4%96%E8%A7%82%E6%95%B0%E5%88%97.md) | 字符串 | 简单 |
| 0048 | [旋转图像](https://leetcode-cn.com/problems/rotate-image/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0048.%20%E6%97%8B%E8%BD%AC%E5%9B%BE%E5%83%8F.md) | 数组 | 简单 |
| 0049 | [字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0049.%20%E5%AD%97%E6%AF%8D%E5%BC%82%E4%BD%8D%E8%AF%8D%E5%88%86%E7%BB%84.md) | 字符串、哈希表 | 简单 |
| 0050 | [Pow(x, n)](https://leetcode-cn.com/problems/powx-n/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0050.%20Pow%28x%2C%20n%29.md) | 数学、二分查找 | 简单 |
| 0053 | [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0053.%20%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.md) | 数组、分治算法、动态规划 | 简单 |
| 0056 | [合并区间](https://leetcode-cn.com/problems/merge-intervals/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0056.%20%E5%90%88%E5%B9%B6%E5%8C%BA%E9%97%B4.md) | 数组、排序 | 简单 |
| 0061 | [旋转链表](https://leetcode-cn.com/problems/rotate-list/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0061.%20%E6%97%8B%E8%BD%AC%E9%93%BE%E8%A1%A8.md) | 链表、双指针 | 简单 |
| 0062 | [不同路径](https://leetcode-cn.com/problems/unique-paths/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0062.%20%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.md) | 数组、动态规划 | 简单 |
| 0067 | [二进制求和](https://leetcode-cn.com/problems/add-binary/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0067.%20%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%B1%82%E5%92%8C.md) | 数学、字符串、位运算 | 简单 |
| 0069 | [x 的平方根](https://leetcode-cn.com/problems/sqrtx/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0069.%20x%20%E7%9A%84%E5%B9%B3%E6%96%B9%E6%A0%B9.md) | 数学、二分查找 | 简单 |
| 0070 | [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0070.%20%E7%88%AC%E6%A5%BC%E6%A2%AF.md) | 动态规划 | 简单 |
| 0073 | [矩阵置零](https://leetcode-cn.com/problems/set-matrix-zeroes/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0073.%20%E7%9F%A9%E9%98%B5%E7%BD%AE%E9%9B%B6.md) | 数组 | 简单 |
| 0075 | [颜色分类](https://leetcode-cn.com/problems/sort-colors/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0075.%20%E9%A2%9C%E8%89%B2%E5%88%86%E7%B1%BB.md) | 数组、排序、双指针 | 简单 |
| 0080 | [删除有序数组中的重复项 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0080.%20%E5%88%A0%E9%99%A4%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E9%87%8D%E5%A4%8D%E9%A1%B9%20II.md) | 数组、双指针 | 简单 |
| 0083 | [删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0083.%20%E5%88%A0%E9%99%A4%E6%8E%92%E5%BA%8F%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0.md) | 链表 | 简单 |
| 0088 | [合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0088.%20%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84.md) | 数组、双指针 | 简单 |
| 0091 | [解码方法](https://leetcode-cn.com/problems/decode-ways/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0091.%20%E8%A7%A3%E7%A0%81%E6%96%B9%E6%B3%95.md) | 字符串、动态规划 | 简单 |
| 0098 | [验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0098.%20%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.md) | 树、深度优先搜索、递归 | 简单 |
| 0100 | [相同的树](https://leetcode-cn.com/problems/same-tree/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0100.%20%E7%9B%B8%E5%90%8C%E7%9A%84%E6%A0%91.md) | 树、深度优先搜索 | 简单 |
| 0101 | [对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0101.%20%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.md) | 树、深度优先搜索、广度优先搜索 | 简单 |
| 0102 | [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0102.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.md) | 树、广度优先搜索 | 简单 |
| 0104 | [二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0104.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.md) | 树、深度优先搜索、递归 | 简单 |
| 0107 | [二叉树的层序遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0107.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86%20II.md) | 树、广度优先搜索 | 简单 |
| 0108 | [将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0108.%20%E5%B0%86%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.md) | 树、深度优先搜索 | 简单 |
| 0110 | [平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0110.%20%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.md) | 树、深度优先搜索、递归 | 简单 |
| 0111 | [二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0111.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E6%B7%B1%E5%BA%A6.md) | 树、深度优先搜索、广度优先搜索 | 简单 |
| 0112 | [路径总和](https://leetcode-cn.com/problems/path-sum/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0112.%20%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.md) | 树、深度优先搜索 | 简单 |
| 0118 | [杨辉三角](https://leetcode-cn.com/problems/pascals-triangle/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0118.%20%E6%9D%A8%E8%BE%89%E4%B8%89%E8%A7%92.md) | 数组 | 简单 |
| 0119 | [杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0119.%20%E6%9D%A8%E8%BE%89%E4%B8%89%E8%A7%92%20II.md) | 数组 | 简单 |
| 0121 | [买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0121.%20%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA.md) | 数组、动态规划 | 简单 |
| 0125 | [验证回文串](https://leetcode-cn.com/problems/valid-palindrome/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0125.%20%E9%AA%8C%E8%AF%81%E5%9B%9E%E6%96%87%E4%B8%B2.md) | 字符串、双指针 | 简单 |
| 0133 | [克隆图](https://leetcode-cn.com/problems/clone-graph/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0133.%20%E5%85%8B%E9%9A%86%E5%9B%BE.md) | 深度优先搜索、广度优先搜索、图 | 简单 |
| 0138 | [复制带随机指针的链表](https://leetcode-cn.com/problems/copy-list-with-random-pointer/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0138.%20%E5%A4%8D%E5%88%B6%E5%B8%A6%E9%9A%8F%E6%9C%BA%E6%8C%87%E9%92%88%E7%9A%84%E9%93%BE%E8%A1%A8.md) | 链表、哈希表 | 简单 |
| 0141 | [环形链表](https://leetcode-cn.com/problems/linked-list-cycle/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0141.%20%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8.md) | 链表、双指针 | 简单 |
| 0142 | [环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0142.%20%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8%20II.md) | 链表、双指针 | 简单 |
| 0149 | [直线上最多的点数](https://leetcode-cn.com/problems/max-points-on-a-line/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0149.%20%E7%9B%B4%E7%BA%BF%E4%B8%8A%E6%9C%80%E5%A4%9A%E7%9A%84%E7%82%B9%E6%95%B0.md) | 哈希表、数学 | 困难 |
| 0150 | [逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0150.%20%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.md) | 栈 | 简单 |
| 0153 | [寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0153.%20%E5%AF%BB%E6%89%BE%E6%97%8B%E8%BD%AC%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%9C%80%E5%B0%8F%E5%80%BC.md) | 数组、二分查找 | 简单 |
| 0155 | [最小栈](https://leetcode-cn.com/problems/min-stack/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0155.%20%E6%9C%80%E5%B0%8F%E6%A0%88.md) | 栈、设计 | 简单 |
| 0160 | [相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0160.%20%E7%9B%B8%E4%BA%A4%E9%93%BE%E8%A1%A8.md) | 链表、双指针 | 简单 |
| 0167 | [两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0167.%20%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C%20II%20-%20%E8%BE%93%E5%85%A5%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84.md) | 数组、双指针、二分查找 | 简单 |
| 0169 | [多数元素](https://leetcode-cn.com/problems/majority-element/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0169.%20%E5%A4%9A%E6%95%B0%E5%85%83%E7%B4%A0.md) | 数组、哈希表 | 简单 |
| 0190 | [颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0190.%20%E9%A2%A0%E5%80%92%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%BD%8D.md) | 位运算 | 简单 |
| 0191 | [位1的个数](https://leetcode-cn.com/problems/number-of-1-bits/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0191.%20%E4%BD%8D1%E7%9A%84%E4%B8%AA%E6%95%B0.md) | 位运算 | 简单 |
| 0198 | [打家劫舍](https://leetcode-cn.com/problems/house-robber/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0198.%20%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8D.md) | 动态规划 | 简单 |
| 0199 | [二叉树的右视图](https://leetcode-cn.com/problems/binary-tree-right-side-view/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0199.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%8F%B3%E8%A7%86%E5%9B%BE.md) | 树、深度优先搜索、广度优先搜索、递归、队列 | 简单 |
| 0200 | [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0200.%20%E5%B2%9B%E5%B1%BF%E6%95%B0%E9%87%8F.md) | 搜索 | 简单 |
| 0202 | [快乐数](https://leetcode-cn.com/problems/happy-number/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0202.%20%E5%BF%AB%E4%B9%90%E6%95%B0.md) | 哈希表、数学 | 简单 |
| 0203 | [移除链表元素](https://leetcode-cn.com/problems/remove-linked-list-elements/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0203.%20%E7%A7%BB%E9%99%A4%E9%93%BE%E8%A1%A8%E5%85%83%E7%B4%A0.md) | 链表 | 简单 |
| 0204 | [计数质数](https://leetcode-cn.com/problems/count-primes/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0204.%20%E8%AE%A1%E6%95%B0%E8%B4%A8%E6%95%B0.md) | 数学、哈希表 | 简单 |
| 0205 | [同构字符串](https://leetcode-cn.com/problems/isomorphic-strings/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0205.%20%E5%90%8C%E6%9E%84%E5%AD%97%E7%AC%A6%E4%B8%B2.md) | 哈希表 | 简单 |
| 0206 | [反转链表](https://leetcode-cn.com/problems/reverse-linked-list/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0206.%20%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.md) | 链表 | 简单 |
| 0209 | [长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0209.%20%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md) | 数组、双指针、二分查找 | 简单 |
| 0215 | [数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0215.%20%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E7%AC%ACK%E4%B8%AA%E6%9C%80%E5%A4%A7%E5%85%83%E7%B4%A0.md) | 数组、堆排序 | 简单 |
| 0219 | [存在重复元素 II](https://leetcode-cn.com/problems/contains-duplicate-ii/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0219.%20%E5%AD%98%E5%9C%A8%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0%20II.md) | 数组、哈希表 | 简单 |
| 0220 | [存在重复元素 III](https://leetcode-cn.com/problems/contains-duplicate-iii/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0220.%20%E5%AD%98%E5%9C%A8%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0%20III.md) | 排序、有序集合、哈希表 | 中等 |
| 0225 | [用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0225.%20%E7%94%A8%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.md) | 栈、设计 | 简单 |
| 0226 | [翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0226.%20%E7%BF%BB%E8%BD%AC%E4%BA%8C%E5%8F%89%E6%A0%91.md) | 树、递归 | 简单 |
| 0232 | [用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0232.%20%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.md) | 栈、设计 | 简单 |
| 0234 | [回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0234.%20%E5%9B%9E%E6%96%87%E9%93%BE%E8%A1%A8.md) | 链表、双指针 | 简单 |
| 0237 | [删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0237.%20%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.md) | 链表 | 简单 |
| 0242 | [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0242.%20%E6%9C%89%E6%95%88%E7%9A%84%E5%AD%97%E6%AF%8D%E5%BC%82%E4%BD%8D%E8%AF%8D.md) | 字符串、哈希表、排序 | 简单 |
| 0268 | [丢失的数字](https://leetcode-cn.com/problems/missing-number/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0268.%20%E4%B8%A2%E5%A4%B1%E7%9A%84%E6%95%B0%E5%AD%97.md) | 位运算、数组、数学 | 简单 |
| 0278 | [第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0278.%20%E7%AC%AC%E4%B8%80%E4%B8%AA%E9%94%99%E8%AF%AF%E7%9A%84%E7%89%88%E6%9C%AC.md) | 数组、二分查找 | 简单 |
| 0283 | [移动零](https://leetcode-cn.com/problems/move-zeroes/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0283.%20%E7%A7%BB%E5%8A%A8%E9%9B%B6.md) | 数组、双指针 | 简单 |
| 0326 | [3 的幂](https://leetcode-cn.com/problems/power-of-three/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0326.%203%20%E7%9A%84%E5%B9%82.md) | 数学 | 简单 |
| 0328 | [奇偶链表](https://leetcode-cn.com/problems/odd-even-linked-list/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0328.%20%E5%A5%87%E5%81%B6%E9%93%BE%E8%A1%A8.md) | 链表 | 简单 |
| 0344 | [反转字符串](https://leetcode-cn.com/problems/reverse-string/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0344.%20%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.md) | 字符串 | 简单 |
| 0345 | [反转字符串中的元音字母](https://leetcode-cn.com/problems/reverse-vowels-of-a-string/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0345.%20%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E5%85%83%E9%9F%B3%E5%AD%97%E6%AF%8D.md) | 字符串 | 简单 |
| 0347 | [前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0347.%20%E5%89%8D%20K%20%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.md) | 堆、哈希表 | 简单 |
| 0349 | [两个数组的交集](https://leetcode-cn.com/problems/intersection-of-two-arrays/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0349.%20%E4%B8%A4%E4%B8%AA%E6%95%B0%E7%BB%84%E7%9A%84%E4%BA%A4%E9%9B%86.md) | 数组 | 简单 |
| 0350 | [两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0350.%20%E4%B8%A4%E4%B8%AA%E6%95%B0%E7%BB%84%E7%9A%84%E4%BA%A4%E9%9B%86%20II.md) | 数组 | 简单 |
| 0367 | [有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0367.%20%E6%9C%89%E6%95%88%E7%9A%84%E5%AE%8C%E5%85%A8%E5%B9%B3%E6%96%B9%E6%95%B0.md) | 数学、二分查找 | 简单 |
| 0371 | [两整数之和](https://leetcode-cn.com/problems/sum-of-two-integers/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0371.%20%E4%B8%A4%E6%95%B4%E6%95%B0%E4%B9%8B%E5%92%8C.md) | 位运算 | 简单 |
| 0374 | [猜数字大小](https://leetcode-cn.com/problems/guess-number-higher-or-lower/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0374.%20%E7%8C%9C%E6%95%B0%E5%AD%97%E5%A4%A7%E5%B0%8F.md) | 二分查找 | 简单 |
| 0380 | [常数时间插入、删除和获取随机元素](https://leetcode-cn.com/problems/insert-delete-getrandom-o1/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0380.%20%E5%B8%B8%E6%95%B0%E6%97%B6%E9%97%B4%E6%8F%92%E5%85%A5%E3%80%81%E5%88%A0%E9%99%A4%E5%92%8C%E8%8E%B7%E5%8F%96%E9%9A%8F%E6%9C%BA%E5%85%83%E7%B4%A0.md) | 数组、哈希表 | 简单 |
| 0387 | [字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0387.%20%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%94%AF%E4%B8%80%E5%AD%97%E7%AC%A6.md) | 字符串 | 简单 |
| 0412 | [Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0412.%20Fizz%20Buzz.md) |   | 简单 |
| 0415 | [字符串相加](https://leetcode-cn.com/problems/add-strings/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0415.%20%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9B%B8%E5%8A%A0.md) | 字符串 | 简单 |
| 0430 | [扁平化多级双向链表](https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0430.%20%E6%89%81%E5%B9%B3%E5%8C%96%E5%A4%9A%E7%BA%A7%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8.md) | 链表 | 简单 |
| 0447 | [回旋镖的数量](https://leetcode-cn.com/problems/number-of-boomerangs/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0447.%20%E5%9B%9E%E6%97%8B%E9%95%96%E7%9A%84%E6%95%B0%E9%87%8F.md) | 哈希表、数学 | 中等 |
| 0454 | [四数相加 II](https://leetcode-cn.com/problems/4sum-ii/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0454.%20%E5%9B%9B%E6%95%B0%E7%9B%B8%E5%8A%A0%20II.md) | 哈希表 | 中等 |
| 0461 | [汉明距离](https://leetcode-cn.com/problems/hamming-distance/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0461.%20%E6%B1%89%E6%98%8E%E8%B7%9D%E7%A6%BB.md) | 位运算 | 简单 |
| 0485 | [最大连续 1 的个数](https://leetcode-cn.com/problems/max-consecutive-ones/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0485.%20%E6%9C%80%E5%A4%A7%E8%BF%9E%E7%BB%AD%201%20%E7%9A%84%E4%B8%AA%E6%95%B0.md) | 数组 | 简单 |
| 0509 | [斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0509.%20%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.md) |   | 简单 |
| 0543 | [二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0543.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E7%9B%B4%E5%BE%84.md) | 二叉树 | 简单 |
| 0557 | [反转字符串中的单词 III](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0557.%20%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E5%8D%95%E8%AF%8D%20III.md) | 字符串 | 简单 |
| 0561 | [数组拆分 I](https://leetcode-cn.com/problems/array-partition-i/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0561.%20%E6%95%B0%E7%BB%84%E6%8B%86%E5%88%86%20I.md) | 数组 | 简单 |
| 0599 | [两个列表的最小索引总和](https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0599.%20%E4%B8%A4%E4%B8%AA%E5%88%97%E8%A1%A8%E7%9A%84%E6%9C%80%E5%B0%8F%E7%B4%A2%E5%BC%95%E6%80%BB%E5%92%8C.md) | 哈希表 | 简单 |
| 0622 | [设计循环队列](https://leetcode-cn.com/problems/design-circular-queue/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0622.%20%E8%AE%BE%E8%AE%A1%E5%BE%AA%E7%8E%AF%E9%98%9F%E5%88%97.md) | 队列 | 简单 |
| 0633 | [平方数之和](https://leetcode-cn.com/problems/sum-of-square-numbers/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0633.%20%E5%B9%B3%E6%96%B9%E6%95%B0%E4%B9%8B%E5%92%8C.md) | 双指针 | 简单 |
| 0652 | [寻找重复的子树](https://leetcode-cn.com/problems/find-duplicate-subtrees/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0652.%20%E5%AF%BB%E6%89%BE%E9%87%8D%E5%A4%8D%E7%9A%84%E5%AD%90%E6%A0%91.md) | 树、哈希表 | 简单 |
| 0658 | [找到 K 个最接近的元素](https://leetcode-cn.com/problems/find-k-closest-elements/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0658.%20%E6%89%BE%E5%88%B0%20K%20%E4%B8%AA%E6%9C%80%E6%8E%A5%E8%BF%91%E7%9A%84%E5%85%83%E7%B4%A0.md) | 二分查找 | 中等 |
| 0690 | [员工的重要性](https://leetcode-cn.com/problems/employee-importance/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0690.%20%E5%91%98%E5%B7%A5%E7%9A%84%E9%87%8D%E8%A6%81%E6%80%A7.md) | 深度优先搜索、广度优先搜索、哈希表 | 简单 |
| 0695 | [岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0695.%20%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%9C%80%E5%A4%A7%E9%9D%A2%E7%A7%AF.md) | 搜索 | 简单 |
| 0704 | [二分查找](https://leetcode-cn.com/problems/binary-search/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0704.%20%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.md) | 二分查找 | 简单 |
| 0705 | [设计哈希集合](https://leetcode-cn.com/problems/design-hashset/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0705.%20%E8%AE%BE%E8%AE%A1%E5%93%88%E5%B8%8C%E9%9B%86%E5%90%88.md) | 哈希表 | 简单 |
| 0706 | [设计哈希映射](https://leetcode-cn.com/problems/design-hashmap/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0706.%20%E8%AE%BE%E8%AE%A1%E5%93%88%E5%B8%8C%E6%98%A0%E5%B0%84.md) | 哈希表 | 简单 |
| 0707 | [设计链表](https://leetcode-cn.com/problems/design-linked-list/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0707.%20%E8%AE%BE%E8%AE%A1%E9%93%BE%E8%A1%A8.md) | 链表 | 简单 |
| 0724 | [寻找数组的中心下标](https://leetcode-cn.com/problems/find-pivot-index/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0724.%20%E5%AF%BB%E6%89%BE%E6%95%B0%E7%BB%84%E7%9A%84%E4%B8%AD%E5%BF%83%E4%B8%8B%E6%A0%87.md) | 数组 | 简单 |
| 0744 | [寻找比目标字母大的最小字母](https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0744.%20%E5%AF%BB%E6%89%BE%E6%AF%94%E7%9B%AE%E6%A0%87%E5%AD%97%E6%AF%8D%E5%A4%A7%E7%9A%84%E6%9C%80%E5%B0%8F%E5%AD%97%E6%AF%8D.md) | 二分查找 | 简单 |
| 0876 | [链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0876.%20%E9%93%BE%E8%A1%A8%E7%9A%84%E4%B8%AD%E9%97%B4%E7%BB%93%E7%82%B9.md) | 链表 | 简单 |
| 0938 | [二叉搜索树的范围和](https://leetcode-cn.com/problems/range-sum-of-bst/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0938.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E8%8C%83%E5%9B%B4%E5%92%8C.md) | 二叉树 | 简单 |
| 1011 | [在 D 天内送达包裹的能力](https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/1011.%20%E5%9C%A8%20D%20%E5%A4%A9%E5%86%85%E9%80%81%E8%BE%BE%E5%8C%85%E8%A3%B9%E7%9A%84%E8%83%BD%E5%8A%9B.md) | 数组 | 简单 |
| 1047 | [删除字符串中的所有相邻重复项](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/1047.%20%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E7%9B%B8%E9%82%BB%E9%87%8D%E5%A4%8D%E9%A1%B9.md) | 字符串 | 简单 |
| 1480 | [一维数组的动态和](https://leetcode-cn.com/problems/running-sum-of-1d-array/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/1480.%20%E4%B8%80%E7%BB%B4%E6%95%B0%E7%BB%84%E7%9A%84%E5%8A%A8%E6%80%81%E5%92%8C.md) | 数组 | 简单 |
| 1486 | [数组异或操作](https://leetcode-cn.com/problems/xor-operation-in-an-array/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/1486.%20%E6%95%B0%E7%BB%84%E5%BC%82%E6%88%96%E6%93%8D%E4%BD%9C.md) | 位运算、数组 | 简单 |
| 1720 | [解码异或后的数组](https://leetcode-cn.com/problems/decode-xored-array/) | [Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/1720.%20%E8%A7%A3%E7%A0%81%E5%BC%82%E6%88%96%E5%90%8E%E7%9A%84%E6%95%B0%E7%BB%84.md) | 位运算 | 简单 |