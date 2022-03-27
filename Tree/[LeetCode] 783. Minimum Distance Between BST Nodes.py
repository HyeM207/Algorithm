# Solution 1 - (내 풀이)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    
        # 순회를 통해 노드들 저장
        def dfs(node : TreeNode) : 
            if not node :
                return
            
            dfs(node.left)
            nodes.add(node.val)
            dfs(node.right)
          
            return 
        
        nodes = set() # 트리의 노드를 저장하는 집합
        dfs(root)
        
        min_dst = sys.maxsize
        nodes = sorted(list(nodes))
  
        # 노드들 중에서 가장 차이가 작은 값 찾기
        for n in range(len(nodes)-1):
            if nodes[n+1] - nodes[n] < min_dst:
                min_dst = nodes[n+1] - nodes[n]
        
        return min_dst

'''
[TEST CASE]
[90,69,null,49,89,null,52]
[96,12,null,null,13,null,52,29]
''';

# 풀이 방법 : 순회를 통해 모든 노드를 집합에 저장 -> 노드 집합을 순회하며 차가 가장 작은 값 추출 후 return
# 후기 : 생각보다 간단한 문제여서 좋았다. 하지만 책 풀이를 보니 내 풀이는 효율적이지 않은 것을 깨닫고 책 풀이를 익혔다.

# Solution 2 (책 풀이)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        if root.left : 
            self.minDiffInBST(root.left)
            
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val # self.prev는 재귀 구조에서 이전 노드의 값이 됨
        
        if root.right : 
            self.minDiffInBST(root.right)
        
        return self.result
        
# 풀이 : 제시된 함수를 아예 재귀 함수로 만든 풀이이다. 왼쪽과 오른쪽 노드가 있다면 그 노드를 중앙 노드로 하여 재귀 호출을 한다. 
#       함수의 메인쪽에는 최소값으로 result를 할당하고 재귀호출의 흐름을 이용하여 이전 노드의 값을 self.prev에 저장한다. 

