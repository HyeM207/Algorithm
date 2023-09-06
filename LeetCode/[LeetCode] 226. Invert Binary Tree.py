# Solution 1 (내 풀이)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root]) 
        
        if root is None :
            return root
        
        while queue :            
                cur_root = queue.popleft()    
                
                if cur_root :
                    # swap 
                    cur_root.right, cur_root.left = cur_root.left, cur_root.right 
             
                    # 왼쪽, 오른쪽 자식 노드 append
                    queue.append(cur_root.left)
                    queue.append(cur_root.right)
                    
        return root        

# 풀이  : BFS 풀이로 풀었다. (탑 다운 방식) 
#       큐를 통해 노드에 접근 -> 왼쪽과 오른쪽 자식 노드 값 swap -> 왼쪽과 오른쪽 자식 노드를 큐에 append -> (큐에 노드가 있을 때까지 반복)


# Solution 2 (책 풀이)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        if root :
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root 
# 