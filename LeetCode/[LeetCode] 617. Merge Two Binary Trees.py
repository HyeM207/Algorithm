# Solution 1 (책 풀이 참고)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 and root2 :
            node = TreeNode(root1.val + root2.val) # 단순 덧셈하면 재귀호출을 못하므로 TreeNode로 바꾼다. 
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            
            return node
        else : 
            return root1 or root2

# 풀이 : 상위 노드부터 리프노드까지 재귀를 통해 값을 더해간다. 

# 후기 : 큐를 이용하여 값을 더하고 TreeNode를 이용하려고 하였지만, 풀이를 보니 바로 노드끼리 덧셈가능한 것을 보고 이후 풀이는 책 풀이를 참고하였ㄷ다. 

# 핵심 : 
    if root1 and root2 :
        node = TreeNode(root1.val + root2.val) # 단순 덧셈하면 재귀호출을 못하므로 TreeNode로 바꾼다. 
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)