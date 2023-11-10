# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def invertTree_(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        풀이 1. dfs 함수를 이용하여 노드를 탐색하며 left와 right을 바꿔준다.
        """
        def dfs(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
            return node
        root = dfs(root)
        return root
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        풀이 2. 원래함수를 재귀함수로 만들어 풀이함
        """
        if not root:
            return
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root