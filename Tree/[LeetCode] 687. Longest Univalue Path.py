# Solution 1 (책 풀이 참고)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result : int = 0
        
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int : 
            # 노드가 없으면 상태값은 0
            if not node : 
                return 0

            # 왼쪽, 오른쪽의 각 노드 탐색 
            left = dfs(node.left)
            right = dfs(node.right)
      
            # 현재 노드와 왼쪽 노드의 값이 같은 지 확인 
            if node.left and node.val == node.left.val : 
                left +=1 
            else : 
                left = 0 
            
            # 현재 노드와 오른쪽 노드의 값이 같은 지 확인 
            if node.right and node.val == node.right.val : 
                right +=1 
            else : 
                right = 0 
            
            # 거리의 최댓값은 왼쪽과 오른쪽 자식 노드 간의 거리의 합
            self.result = max(self.result, left+right)
        
            # 상태값은 자식 노드 상태값 중 큰 값 하나만 return 
            return max(left, right)
            
            
        dfs(root)
        return self.result        


# 풀이 : 해당 문제는 543번 문제와 비슷하게 상태값을 이용한 dfs 풀이를 이용한다. 
#      - 알고리즘 : 리프노드까지 DFS로 탐색하다가 자식 노드의 값이 같으면 백트래킹으로 거리를 쌓아간다.

#      - 상태값 : 기본은 0이지만, 만약 자식노드의 값이 같으면 +1 씩 된다. 
#                   return 하는 상태값은 왼쪽과 오른쪽 상태값 중에서 큰 값만을 이용한다. 
                    return max(left, right)

#      - 결과값 : 왼쪽과 오른쪽 노드 간의 거리의 합 최대값        
                self.result = max(self.result, left+right)
