# Solution 1 (내 풀이)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    hap : int = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        
        def dfs(node : TreeNode) :
            if not node : 
                return 

            dfs(node.left)
            
            if node.val >= low and node.val <= high :
                self.hap += node.val
            
            # print("mid : ",node.val, self.hap)
            
            dfs(node.right)
            
        dfs(root)
        return self.hap


# 후기 : 이 문제도 혼자 힘으로 풀었다! 1038 문제와 비슷한 문제로 순회 방향만 잘 캐치하면 풀 수 있었다
# 풀이 : 순회방향은 (왼쪽 자식 노드 -> 중앙 노드 -> 오른쪽 자식 노드) 순으로 하여 재귀호출 구조로 풀었다.


# Solution 2 (책 풀이)
class Solution:
    hap : int = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node : TreeNode) :
            if not node : 
                return 0

            # 현재 노드의 값을 LOW와 HIGH와 비교하여 재귀호출 함. 이는 불필요한 노드는 탐색하지 않는 방법이다. 
            if node.val < low : 
                return dfs(node.right)
            elif node.val > high : 
                return dfs(node.left)
            
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)


# 책 풀이 : 해당 풀이는 현재 노드의 값을 low와 high와 비굑하여 재귀호출하는 구조로, 이는 불필요한 호출을 막을 수 있다. 
#       주목할 부분은 dfs함수의 마지막 줄의 return 문으로 현재 노드 값 + 왼쪽과 오른쪽 노드를 재귀호출 한 return값을 더하는 것을 확인할 수 있다. 
