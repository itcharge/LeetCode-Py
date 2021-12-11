class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i
            while j > 0 and arr[j - 1] > temp:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = temp
            
        return arr
    
    def bucketSort(self, head: ListNode, bucket_size=5):
        if not head:
            return head
        
        # 找出链表中最大值 list_max 和最小值 list_min
        list_min, list_max = float('inf'), float('-inf')
        cur = head
        while cur:
            if cur.val < list_min:
                list_min = cur.val
            if cur.val > list_max:
                list_max = cur.val
            cur = cur.next
            
        # 计算桶的个数，并定义桶
        bucket_count = (list_max - list_min) // bucket_size + 1
        buckets = [[] for _ in range(bucket_count)]
        
        # 将链表节点值依次添加到对应桶中
        cur = head
        while cur:
            buckets[(cur.val - list_min) // bucket_size].append(cur.val)
            cur = cur.next
        
        dummy_head = ListNode(-1)
        cur = dummy_head
        for bucket in buckets:
            # 对桶中元素单独排序
            self.sortLinkedList(bucket)
            for num in bucket:
                cur.next = ListNode(num)
                cur = cur.next
        
        return dummy_head.next
        
    def sortLinkedList(self, head: ListNode):
        return self.bucketSort(head)