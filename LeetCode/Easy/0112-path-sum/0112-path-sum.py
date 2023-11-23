# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 풀이 1: dfs. "root" ~ "leaf" 임
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, hap):
            if not node:
                return False
            
            hap += node.val
            # 동일한 코드지만 가독성 높임
            # if hap == targetSum and (node.right is None and node.left is None):
            #     return True
            if not node.left and not node.right:
                return hap == targetSum

            right = dfs(node.right, hap)
            left = dfs(node.left, hap)
        
            return right or left
            
        return dfs(root, 0)    