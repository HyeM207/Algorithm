# Solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
 
        values = []
    
        node = head 
        # 1. 연결리스트를 순회하며 노드의 값들을 리스트에 저장한다.
        while node is not None :
            values.append(node.val)
            node = node.next
        
		# 2. 노드를 저장한 리스트를 거꾸로 뒤집어 펠린드롬인지 확인한다.
        if values == values[::-1]:
            return True
        else :
            return False


# Solution 2
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
 
        rev = None
        slow = fast = head
        
        # 런너 이용 
        while fast and fast.next : 
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast : 
            slow = slow.next
            
        # 펠린드롬 판별
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
            
        return not rev