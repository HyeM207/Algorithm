# Solution 1 : 책 풀이 참고하여 품 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        root = prev = ListNode(None)
        prev.next = head
        
        while head and head.next :
            
            # b가 현재 노드 head를 가리키도록 함 - 과정 1
            b= head.next
            head.next = b.next
            b.next = head
            
            # 이전 노드 prev가 b를 가리키도록 함 - 과정 2
            prev.next = b
            
            # 다음 반복문을 위해 이동 
            head = head.next
            prev = prev.next.next
        
        return root.next