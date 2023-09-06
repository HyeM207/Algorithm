# Solution 1 (내 풀이)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    hap = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:       
        
        def dfs(node : TreeNode) : 
            if not node :
                return 
            
            # print("in : ", node.val, self.hap)
            dfs(node.right)
            self.hap += node.val
            node.val = self.hap
            # print("mid : ",node.val, self.hap)
            dfs(node.left)
            # print("out : ",node.val, self.hap)
            
        dfs(root)
        return root

# 후기 : 오랜만에 내 힘으로 온전히 푼 문제이다. 기분 좋다!!!
# 핵심 : 순회 순서가 (오른쪽 노드 -> 중앙노드 -> 왼쪽 노드) 이므로, 해당 방향으로 트리를 순회하며 누적 합을 노드로 바꾼다.

# 책 풀이 : 책 풀이는 따로 함수를 추가로 구현하지 않고 bstToGst를 내 코드 기준 'dfs' 함수 코드로 하여 풀이하였다. 
