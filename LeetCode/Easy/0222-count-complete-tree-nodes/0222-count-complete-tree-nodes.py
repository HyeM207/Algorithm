# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #  풀이 1: bfs로 deque를 활용하여 풀기 => O(N)
    def countNodes_(self, root: Optional[TreeNode]) -> int:
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
    
    # 풀이 2 :  완전이진트리 특성 이용  => O(log^2 N)
    # 참고: https://leetcode.com/problems/count-complete-tree-nodes/discuss/2815567/python3-general-Binary-Search-using-template
    def countNodes_(self, root: Optional[TreeNode]) -> int:
        """
        1. 깊이 구함 (맨 왼쪽 기준) - root부터 leaf노드 위치한 그 위의 높이까지 노드 개수 계산 가능
        2. 마지막 leaf 노드 개수 확인 
        """
        if not root: return 0
        
        def findDepth(node):
            if not node.left:
                return 0
            return findDepth(node.left)+1

        def check(node,mid,curDepth,left,right):
            # 찾고자 하는 depth의 노드라면 return True
            if curDepth == depth: return True if node else False 
            # 그게 아니면 mid값 조정해서 탐색 범위 변경함
            if mid <= (left+right)//2:
                return check(node.left,mid,curDepth+1,left,(left+right)//2)
            else:
                return check(node.right,mid,curDepth+1,(left+right)//2,right)
        
        depth = findDepth(root)
        lastLevelLength = 2**depth
        
        # s와 e는 마지막 depth의 노드 시작&끝 인덱스 
        s, e = 1, lastLevelLength+1
        while s+1 < e:
            mid = (s+e)//2
            if check(root,mid,0,1,lastLevelLength):
                s = mid
            else:
                e = mid

        return lastLevelLength - 1 + s
    
    # 참고 3 :
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth_left = self.left_depth(root)
        depth_right = self.right_depth(root)

        if depth_left == depth_right:
            # If the left and right depths are equal, the tree is a perfect binary tree.
            return 2**depth_left - 1
        else:
            # If the depths are not equal, the tree is not perfect.
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def left_depth(self, node: TreeNode) -> int:
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth

    def right_depth(self, node: TreeNode) -> int:
        depth = 0
        while node:
            depth += 1
            node = node.right
        return depth