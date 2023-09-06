# Solution 1 (책 풀이 참고)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # 빈 트리일 경우, return 0
        if root is None : 
            return 0
        
        queue = deque([root]) # deque로 이용 (해당 큐는 후에 자식 노드들을 담고 있는다)
        depth = 0
        
        
        while queue :
            depth += 1
            
            # 큐에서 popleft()한 노드의 자식 노드들을 큐에 append
            # 깊이마다 실행되는 아래 코드들  
            for _ in range(len(queue)) :
                cur_root = queue.popleft()    
                
                if cur_root.left : 
                    queue.append(cur_root.left)
                    
                if cur_root.right : 
                    queue.append(cur_root.right)
                    
        return depth

# 풀이 :
#       - 트리는 bfs (반복)을 통해 풀이한다. deque를 이용하여 깊이마다 있는 자식 노드들을 append한 후, 
#       반복문을 돌며, append했던 노드들을 popleft()하여 다음 자식 노드들을 append 하는 방식이다. 
#       - while 반복문 한 번 돌 때마다 depth가 증가함

# 후기 : 트리 알고리즘 풀이는 처음이라 혼자 풀어보려고 하였지만, 트리의 접근법을 알기위해 책 풀이를 참고하였다. 

# 핵심 :
    queue = deque([root]) 
        while queue :
            for _ in range(len(queue)) :
                cur_root = queue.popleft()    
            
                if cur_root.left : 
                    queue.append(cur_root.left)
                if cur_root.right : 
                    queue.append(cur_root.right)