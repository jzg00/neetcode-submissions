# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #    2->3->None
        #       h       (if an empty head gets passed in or if we've reached 
        #                the end of the linked list return itself)
        if not head or not head.next:
            return head

        newHead = self.reverseList(head.next) # newHead = self.reverseList(2) = 3 (since the last node returns itself)
                                              # h                  v---- 
        head.next.next = head                 # 2->3->None becomes 2->3-
        head.next = None                      # which becomes  None<-2<-3

        return newHead                        
                       