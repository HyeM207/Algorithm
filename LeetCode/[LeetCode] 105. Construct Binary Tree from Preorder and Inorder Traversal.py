# Solution1 (책 풀이)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
          if inorder : 
                # 전위 순회 결과는 중위 순회 분할 인덱스
                index = inorder.index(preorder.pop(0))
                
                # 중위 순회 결과 분할 정복
                node = TreeNode(inorder[index])
                node.left = self.buildTree(preorder, inorder[0:index])
                node.right = self.buildTree(preorder, inorder[index+1:])
                
                return node



# 후기 : 전위순회와 중위 순회 결과가 어떻게 이진트리를 구축할 수 있는건지 감이 잡히지 않아 책 풀이를 보고 익혔다. 

# 풀이 : 
#       - 전위 순회의 첫 번째 결과 : 중위 순회의 왼쪽과 오른쪽을 분할시키는 역할 
#       - 중위 순회를 왼쪽과 오른쪽으로 분할 후, '분할 정복 구조'로 재귀호출 실행  