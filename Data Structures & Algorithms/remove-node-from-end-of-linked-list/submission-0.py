# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return

        # get the size of the linked list
        size = 0
        cur = head
        while cur:
            size +=1
            cur = cur.next
        
        # if we are removing the head node, return head.next as the new head
        if size - n == 0:
            return head.next
        
        # find the stopping point (we want to stop right before the node that is getting removed)
        stop = size - n
        curr = head
        for i in range(1, stop+1):
            if i == stop:
                curr.next = curr.next.next
            curr = curr.next
        
        return head