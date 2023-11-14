# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """ 
    # 분할정복
    한 그룹의 중앙값을 BST 트리에 배치
     -> 그 값을 제외한 양쪽 그룹에서 또 중앙값 찾고 배치 -> 반복
    """
    # 풀이 1: 만든 재귀함수 이용
    def sortedArrayToBST_(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(left, right):
            if left > right: # 종료 조건 기억해두기
                return None
            mid =  (left+right)//2
            node = TreeNode(nums[mid])
            node.left = divide(left, mid-1)
            node.right = divide(mid+1, right)
            return node
        
        return divide(0, len(nums)-1)

    # 풀이 2: 주어진 함수를 재귀함수로 이용
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root