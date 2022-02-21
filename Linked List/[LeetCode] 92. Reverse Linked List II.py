# Solution 1 : 재귀 함수 이용하여 reverse 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # reverse 함수에서 노드의 값을 저장하는 큐
        values = deque()
        
        cnt = 0
        # 재귀함수
        # : 연결 리스트 끝단까지 접근하여 val을 큐에 저장하였다가, 되돌아오면서 큐에 있던 값을 꺼내 값을 변경함
        def reverse(node : ListNode, cnt):
            
            cnt += 1
            
            if cnt >= left and cnt <= right :
                values.append(node.val) # 노드의 val을 큐에 저장
            
            if node.next != None : 
                # print('node : ', node)
                reverse(node.next, cnt) # 재귀 함수 호출
            
            if cnt >= left and cnt <= right :
                node.val = values.popleft() # 큐에 저장된 값들로 노드의 val 변경
                
            return node
    
        if head != None:
            head = reverse(head, cnt)
        
        return head