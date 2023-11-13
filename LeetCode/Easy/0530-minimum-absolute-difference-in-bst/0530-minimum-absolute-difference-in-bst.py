# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 풀이 1. BFS로 노드 값 저장 후 최소값 차이 구하기
    """
     이진탐색트리 : 부모 노드 기준, 왼쪽 노드엔 작은 값, 오른쪽 노드엔 큰 값
     ==> 값의 차이를 자식-부모 로만 두면 안됨. 모든 노드들을 저장하자
    """
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        
        q = deque([root])
        nodes = []
        
        # 1. BFS로 노드 조회 및 노드값 저장
        while q:
            node = q.popleft()
            nodes.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        # 2. 최소 차 구하기
        min_diff = 10**5 +1  # 최소값
        nodes.sort()
        for i in range(len(nodes)-1):
            diff = nodes[i+1] - nodes[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff