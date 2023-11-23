# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #  풀이 1: bfs로 deque를 활용하여 풀기
    def countNodes(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        
        if not root:
            return 0
        
        answer = 0
        queue = deque([root])
        while queue:
            current_node = queue.popleft()
            answer += 1
            
            if current_node.left: # 왼쪽부터~
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
        return answer