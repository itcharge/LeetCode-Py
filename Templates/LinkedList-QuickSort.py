class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, left: ListNode, right: ListNode):
        if left == right or left.next == right:
            return left
        pivot = left.val
        node_i, node_j = left, left.next
        
        while node_j != right:
            if node_j.val < pivot:
                node_i = node_i.next
                node_i.val, node_j.val = node_j.val, node_i.val
            node_j = node_j.next
        
        node_i.val, left.val = left.val, node_i.val
        return node_i
        
    def quickSort(self, left: ListNode, right: ListNode):
        if left == right or left.next == right:
            return left
        pi = self.partition(left, right)
        self.quickSort(left, pi)
        self.quickSort(pi.next, right)
        return left
        
    
    def sortLinkedList(self, head: ListNode):
        if not head or not head.next:
            return head
        return self.quickSort(head, None)