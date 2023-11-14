# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """ 
        # 분할정복
        한 그룹의 중앙값을 BST 트리에 배치
         -> 그 값을 제외한 양쪽 그룹에서 또 중앙값 찾고 배치 -> 반복
        """
        def divide(left, right):
            if left > right: # 종료 조건 기억해두기
                return None
            mid =  (left+right)//2
            node = TreeNode(nums[mid])
            node.left = divide(left, mid-1)
            node.right = divide(mid+1, right)
            return node
        
        return divide(0, len(nums)-1)