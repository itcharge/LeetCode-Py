class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def bubbleSort(self, head: ListNode):
        node_i = head
        while node_i:
            node_j = head
            while node_j and node_j.next:
                if node_j.val > node_j.next.val:
                    node_j.val, node_j.next.val = node_j.next.val, node_j.val
                node_j = node_j.next
            node_i = node_i.next
        
        return head
    
    def sortLinkedList(self, head: ListNode):
        return self.bubbleSort(head)