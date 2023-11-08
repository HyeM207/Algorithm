# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 풀이1. dfs 와 전역 변수 이용 
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         def dfs(depth,  node):
#             global max_depth
#             max_depth = max(max_depth, depth)
#             if node.left :
#                 dfs(depth+1, node.left)
#             if node.right :
#                 dfs(depth+1, node.right)        

#         if not root:
#             return 0
#         global max_depth
#         max_depth = 1
#         dfs(1, root)
#         return max_depth

    # 풀이2. 본 함수를 재귀 함수 이용
    # dfs로 leaf 노드에 도달했다가 올라오면서 최종적으로 depth 계산이 됨 
    # 잎(leaf) 노드에 도달하면 깊이 1로 시작하고, 이를 상위 노드로 전달하며 계산합니다.
    # def maxDepth1(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    
    # 풀이3. 풀이2 변형 (더 효율적임)
    # dfs로  leaf 노드에 도달했을 때 depth가 도출됨. 그리고 재귀 함수 종료  
    # 잎(leaf) 노드에서 최대 깊이를 계산한 후, 상위 노드로 올라가며 가장 큰 깊이를 선택합니다.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: 
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        return dfs(root, 0)