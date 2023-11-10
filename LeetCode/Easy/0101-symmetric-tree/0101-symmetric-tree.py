# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        풀이1: 트리의 좌우 동시 탐색
        """
        def _isSymmetric(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val == node2.val:
                return _isSymmetric(node1.left, node2.right) and _isSymmetric(node1.right, node2.left)
            else:
                return False
        return _isSymmetric(root.left, root.right)