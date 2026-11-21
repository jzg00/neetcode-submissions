# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:   # if we reach a depth for the first time, create a new subarray
                res.append([])
            
            res[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
    
        dfs(root, 0)

        return res
