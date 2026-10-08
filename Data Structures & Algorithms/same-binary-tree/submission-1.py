# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive DFS solution O(n)

        # base cases:
        if not p and not q: # if both nodes are None, then they are the same
            return True

        if not p or not q: # if one of the nodes are None, return False
            return False
        
        if p.val != q.val: # if their values are different, return False
            return False
        
        # recursively call the left nodes and right nodes in both trees
        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))