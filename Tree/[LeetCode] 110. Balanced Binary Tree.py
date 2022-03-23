# Solution 1 (책 풀이 참고)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: TreeNode) -> int : 
            # 노드가 없으면 상태값은 0
            if not node : 
                return 0

            # 왼쪽, 오른쪽의 각 노드 탐색 
            left = dfs(node.left)
            right = dfs(node.right)
      
            # 거리 차가 1 이상인 경우에는 -1이 되는데, 그렇게 되면 그 이후로 계속 -1을 return 하게 된다.
            if left == -1 or right == -1 or abs(left - right) > 1 :
                return -1
        
            # 현재 노드의 상태값은 자식 노드(left, right)의 최대값보다 무조건 +1 이다
            return max(left, right) + 1
            
            
        return dfs(root) != -1    

# 풀이 : 해당 풀이 역시 상태값을 이용하였다. 상태값은 리프노드에서 상위 노드로 올라올 때 마다 +1 된다. 
#       - 상태값 (return 값) : 현재 노드의 상태값은 자식 노드(left, right)의 최대값보다 무조건 +1 이다
                return max(left, right) + 1 

#       - return -1  : 거리 차가 1 이상인 경우에는 -1이 되는데, 그렇게 되면 그 이후로 계속 -1을 return 하게 된다.
                if left == -1 or right == -1 or abs(left - right) > 1 :
                    return -1