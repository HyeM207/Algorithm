# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(head, nodes):
            if not head:
                return nodes
            left = []
            right = []
            if head.left:
                left = dfs(head.left, nodes+[head.left.val])
            else:
                left = dfs(head.left, nodes+['null'])
            if head.right :
                right = dfs(head.right, nodes+[head.right.val]) 
            else:
                right = dfs(head.right, nodes+['null'])
            return left+right +[head.val]
            
        result1 = dfs(p, [])
        result2 = dfs(q, [])
        return result1==result2