# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    ! 풀이 정리 !
    - 풀이1, 2는 재귀함수라, 중복 탐색이 있음. 그러나 풀이3은 stack과 while문을 활용하여 중복 탐색 X
    - 풀이 1과 2의 차이는 개발자 스타일에 따름. 특히 풀이2는 targetSum이 오염된다는 문제가 있음
    """
    # 풀이 1: dfs. "root" ~ "leaf" 임
    def hasPathSum_(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, hap):
            if not node:
                return False
            
            hap += node.val
            if not node.left and not node.right:
                return hap == targetSum

            right = dfs(node.right, hap)
            left = dfs(node.left, hap)
        
            return right or left
            
        return dfs(root, 0)   
    
    
    # 풀이2 : 본 함수 이용하기
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return 
        
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
    
    # 풀이 3:  재귀 없이 while문 stack으로
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False 
        
        stack = [(root, targetSum-root.val)]

        while(stack):
            # 탐색할 노드 pop하고 append
            current_node,current_sum = stack.pop() 

            if not current_node.right and not current_node.left and current_sum == 0:
                return True
            if current_node.left:
                stack.append((current_node.left, current_sum - current_node.left.val))
            if current_node.right:
                stack.append((current_node.right, current_sum - current_node.right.val))

        return False 