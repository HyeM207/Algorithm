# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(depth,  node):
            global max_depth
            max_depth = max(max_depth, depth)
            if node.left :
                dfs(depth+1, node.left)
            if node.right :
                dfs(depth+1, node.right)        

        if not root:
            return 0
        global max_depth
        max_depth = 1
        dfs(1, root)
        return max_depth