# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 풀이1: dfs 함수로 각 트리를 순회하여 노드들을 리스트에 담고, 둘의 리스트를 비교함
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         def dfs(head, nodes):
#             if not head:
#                 return nodes
#             left = []
#             right = []
#             if head.left:
#                 left = dfs(head.left, nodes+[head.left.val])
#             else:
#                 left = dfs(head.left, nodes+['null'])
#             if head.right :
#                 right = dfs(head.right, nodes+[head.right.val]) 
#             else:
#                 right = dfs(head.right, nodes+['null'])
#             return left+right +[head.val]
            
#         result1 = dfs(p, [])
#         result2 = dfs(q, [])
#         return result1==result2

    # 풀이2: 재귀함수 (더 효율적임)
    # 동시에 p와 q의 left와 right을 비교해나감
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None :
            return True

        if p == None or q == None or p.val != q.val :
            return False

        return (self.isSameTree(p.left , q.left) and self.isSameTree(p.right , q.right))    