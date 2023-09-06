# Try (내 풀이 - 실패)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        root_p = len(nums)//2
        root = nums[root_p]
        print(root)
        root = node = TreeNode(root)
        makeTree(node, root_p - 1, root_p - 2) 
        
        
        def makeTree(root : TreeNode, left_p, right_p):    
            if left_p > -1 and left_p < len(nums) :  
                root.left = nums[left_p]
            
            if right_p > -1 and right_p < len(nums):
                root.right = nums[right_p]
            
            TreeNode(root.left, left_p-1, right)

        # ...

# 아이디어 : 중간 인덱스부터 접근하여 왼쪽 오른쪽의 서브트리를 만드는 재귀호출 흐름의 코드를 생각해보았다.
# 이런식으로 시도해봤지만 잘못 풀고 있다는 생각(생각한 흐름대로 코드를 못 완성함)이 들었고, 고민 끝에 아래 책 풀이를 참고하였다. 



# Solution 1 (책 풀이)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums :
            return 
        
        mid = len(nums)//2
    
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[ :mid])
        root.right = self.sortedArrayToBST(nums[mid+1: ])
        
        return root

# 핵심 :  root의 왼쪽과 오른쪽 노드를 재귀로 바로 호출하여 할당함 (+중앙 노드의 root는 TreeNode로 만들어줌)