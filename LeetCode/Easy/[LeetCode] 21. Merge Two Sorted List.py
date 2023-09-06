# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (not l1) or (l2 and l1.val > l2.val) :
            l1, l2 = l2, l1
            
        if l1: 
            l1.next = self.mergeTwoLists(l1.next, l2)
            
        return l1


'''
해당 문제는 책 풀이를 참고하여 풀었다.  
'''