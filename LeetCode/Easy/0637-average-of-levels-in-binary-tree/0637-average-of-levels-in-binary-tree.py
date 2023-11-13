# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 풀이1 .이중 while문 사용
    def averageOfLevels_(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        result = []
        
        while queue:
            lv  = queue[:]
            nodes = [] # 같은 레벨의 노드만 저장
            next_nodes = [] # 다음 레벨의 노드들 저장
            while lv:
                node = lv.pop()
                nodes.append(node.val)
                
                # 다음 레벨의 큐에 저장
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            result.append(sum(nodes)/ len(nodes))    
            queue = next_nodes[:]

        return result
    
    # 풀이 2. while과 for문을 이용한 풀이. 더 가독성 높음
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        result = []
        
        while queue:
            cur_sum = 0
            cur_nodes = queue
            queue = [] # 초기화 필요
            for node in cur_nodes:
                cur_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(cur_sum/len(cur_nodes))
            
        return result