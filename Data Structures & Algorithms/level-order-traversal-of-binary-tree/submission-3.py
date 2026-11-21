# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = collections.deque([root]) # initialize a queue with the root added in

        while q:
            level = []  # subarray that will be added to res, representing the nodes at each level
            lenQ = len(q) # the current len of q represents how many nodes are in that level
            for _ in range(lenQ):
                node = q.popleft()
                level.append(node.val)  # append the node val to the subarray

                # add the children nodes to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(level)

        return res

