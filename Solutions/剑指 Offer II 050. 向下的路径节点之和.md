# [剑指 Offer II 050. 向下的路径节点之和](https://leetcode.cn/problems/6eUYwP/)

- 标签：树、深度优先搜索、二叉树
- 难度：中等

## 题目大意



## 解题思路



## 代码

```Python
class Solution:
    prefixsum_count = dict()
    def dfs(self, root, prefixsum_count, target_sum, cur_sum):
        if not root:
            return 0
        res = 0
        cur_sum += root.val
        res += prefixsum_count.get(cur_sum - target_sum, 0)
        prefixsum_count[cur_sum] = prefixsum_count.get(cur_sum, 0) + 1

        res += self.dfs(root.left, prefixsum_count, target_sum, cur_sum)
        res += self.dfs(root.right, prefixsum_count, target_sum, cur_sum)

        prefixsum_count[cur_sum] -= 1
        return res

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        prefixsum_count = dict()
        prefixsum_count[0] = 1
        return self.dfs(root, prefixsum_count, targetSum, 0)
```

