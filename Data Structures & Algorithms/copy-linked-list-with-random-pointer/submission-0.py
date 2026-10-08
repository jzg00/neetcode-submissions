"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        # use a hashmap to help us map the copied nodes pointers (.next and .random) to actual copies instead of referencing the originals
        copies = {None : None} # pre-seed the hashmap to handle None nodes. This helps perserve the random and next pointers that point to None

        # create new copies of the original nodes
        curr = head
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        # set the copies' .next and .random pointers to other copied nodes
        curr = head
        while curr:
            copy = copies[curr]
            copy.next = copies[curr.next]
            copy.random = copies[curr.random]
            curr = curr.next
            
        return copies[head]