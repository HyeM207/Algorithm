class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        root = result = ListNode()
        carry = 0
        
        while l1 or l2 :      
            
            if l1 is not None : 
                result.val += l1.val
                l1 = l1.next
            
            if l2 is not None :
                result.val += l2.val
                l2 = l2.next
            
            if result.val > 9 :
                carry = 1
                result.val -= 10
            
            if l1 is None and l2 is None and carry == 0:
                break
            
            # 올림 값 다음 노드에 추가
            result.next = ListNode(carry)
            result = result.next 
            carry = 0
         
            
        return root
            