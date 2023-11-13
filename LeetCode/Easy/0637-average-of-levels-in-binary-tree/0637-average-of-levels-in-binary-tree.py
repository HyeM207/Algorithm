# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        result = []
        
        while queue:
            lv  = queue[:]
            nodes = [] # 같은 레벨의 노드만 저장
            next_nodes = [] # 다음 레벨의 큐
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