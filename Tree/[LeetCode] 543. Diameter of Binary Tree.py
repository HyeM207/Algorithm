# Solution 1 (책 풀이 참고)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest : int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int : 
            # 리프 노드의 상태값은 -1
            if not node : 
                return -1 

            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색 
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로  
            # 거리 : (왼쪽 상태값) + (오른쪽 상태값) + 2
            self.longest = max(self.longest, left+right+2)

            # 상태 값
            return max(left, right) + 1
            
        dfs(root)
        return self.longest

# 풀이  : 상태값을 이용한 트리의 dfs 풀이이다. 
#       - 현재 노드의 상태값 = max((왼쪽 상태값),(오른쪽 상태값)) + 1 
#          (리프 노드의 상태값은 -1)
#
#       - 거리 : (왼쪽 상태값) + (오른쪽 상태값) + 2

# 후기 : 해당 문제 역시 책 풀이를 참고하였다. '상태값'을 이용한 풀이를 이번 문제를 풀이하며 처음 알게 되었는데,
#       거리를 계산할 때 상태값을 이용한다고 하니, 해당 풀이 방법을 암기해서 다른 문제에 응용할 수 있도록 해야겠다.