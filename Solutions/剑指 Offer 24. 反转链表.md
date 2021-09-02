## [剑指 Offer 24. 反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)

- 标签：递归、链表
- 难度：简单

## 题目大意

给定一个链表的头结点。

要求：将该链表反转并输出反转后链表的头节点。

## 解题思路

1. 思路一：递归

- 如果 `head` 为空 或 `head.next` 为空，直接返回 `head`。
- 新的头节点 `new_head` 通过递归指向尾节点。
- 每一层递归，将当前 `head` 下一个节点指向 `head`，即 `head.next.next = head`，再将 `head` 指向空。
- 最后返回 `new_head` 节点。

2. 思路二：迭代

- 使用三个指针`pre`、`cur`、`next`，分别指向当前节点的前一节点、当前节点、当前节点的下一个节点。
- 迭代过程中：
  - 下一节点移动到当前节点的下一节点，即 `next = cur.next`。
  - 将当前节点指向前一节点，即 `cur.next = pre`。
  - 前一节点移动到当前节点，即 `pre = cur`。
  - 当前节点移动到下一节点，即 `cur = next`。
- 直到当前节点为空时，返回上一节点，即返回 `pre`。

## 代码

1. 递归

```Python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
```

2. 迭代

```Python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
```

