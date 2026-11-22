# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we know that we are given a BST, root, p, and q
        # since it's a BST, we know that a nodes left and right subtree have to be less than and greater than that node respectively
        # if p < node <=q or q node <= p, then we know that the LCA is that node. 
        # if p and q < node, then we know that the LCA is somewhere down the left subtree of that node
        # if node < p and q, then we know that the LCA is somewhere down the right subtree of that node

        if not root:
            return
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return root