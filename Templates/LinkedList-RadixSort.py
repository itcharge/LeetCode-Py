class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def radixSort(self, head: ListNode):
        size = 0
        cur = head
        while cur:
            val_len = len(str(cur.val))
            if val_len > size:
                size = val_len
            cur = cur.next
            
        for i in range(size):
            buckets = [[] for _ in range(10)]
            cur = head
            while cur:
                buckets[cur.val // (10 ** i) % 10].append(cur.val)
                cur = cur.next
                
            dummy_head = ListNode(-1)
            cur = dummy_head
            for bucket in buckets:
                for num in bucket:
                    cur.next = ListNode(num)
                    cur = cur.next
            head = dummy_head.next
            
        return head
            
    def sortLinkedList(self, head: ListNode):
        return self.radixSort(head)