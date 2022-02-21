# Solution 1 : 연결리스트 값을  리스트로 저장 후, 연결리스트로 변환

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        root = result = ListNode() 
        
        odd = [] # 홀수 
        even = []  # 짝수
        
        cnt = 1
        
        if head is None :
            return head
        
        # 연결리스트를 순회하며 홀수번째와 짝수번째인지에 따라 값을 저장한다. 
        while head :
            if cnt %2 == 1 :
                odd.append(head.val)
            else :
                even.append(head.val)
                
            head = head.next
            cnt +=1 
        
        # 홀수와 짝수값 리스트를 합친다.
        odd += even
    
        # 리스트를 연결리스트로 변환
        for idx in range(0, cnt-1) :
            result.val = odd[idx] 
            if idx != cnt-2 :
                result.next = ListNode()
                result = result.next
            
        return root