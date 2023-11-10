# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def invertTree_(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        풀이 1. dfs 함수를 이용하여 노드를 탐색하며 left와 right을 바꿔준다.
        """
        def dfs(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
            return node
        root = dfs(root)
        return root
    
    def invertTree_(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        풀이 2. 원래함수를 재귀함수로 만들어 풀이함
        """
        if not root:
            return
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        풀이 3. while문으로 노드 탐색 후 swap
            - 탐색할 노드는 deque에 저장 (큐)
        """
        from collections import deque
        todo = deque([root]) # 탐색할 노드 append
        node = root
        while len(todo):
            node = todo.popleft()
            if (node == None):
                continue

            todo.append(node.left)
            todo.append(node.right)

            node.left, node.right = node.right, node.left

        return root