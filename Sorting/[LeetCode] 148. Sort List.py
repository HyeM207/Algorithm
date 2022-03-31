# Solution 1 - (내 풀이)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head : 
            return head
        
        nodes = deque()
        
        while head is not None :
            nodes.append(head.val)
            head =  head.next
    
        
        nodes = sorted(nodes, reverse=True)
        result = node = ListNode(nodes.pop())
        
        while nodes:
            node.next = ListNode(nodes.pop())
            node = node.next 
        
        return result 


# 풀이 : 연결리스트의 노드들을 리스트에 따로 저장하고, 노드들이 담긴 리스트를 정렬하여 연결리스트로 바꾼다.
# 후기 : 이 방식보다는 병합정렬 방식의 풀이가 더 적절해보인다. 병합 정렬 풀이는 책을 참고하였다.  

# Solution 2 (책 풀이)
class Solution:
    # 두 정렬 리스트 병합 
    def mergeTwoLists(self, l1 : ListNode, l2 : ListNode) -> ListNode: 
        if l1 and l2 :
            if l1.val > l2.val : 
                l1, l2 = l2, l1 # 큰 값이 l2로 오도록 swap
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2 
            
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next) : 
            return head
        
        # 런너 기법 (fast는 next 2개씩, slow는 next 1개씩, half는 slow의 이전 값)
        half, slow, fast = None, head, head
        while fast and fast.next :
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None # half를 기준으로 연결 리스트를 끊어버린다. 
       
 

        # 분할 재귀 호출 
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1,l2)

# 흐름 : sortlist에서 런너 기법으로 연결리스트를 반으로 자른다. 이때 재귀호출을 통해 분할 재귀 호출 형태를 띄고, 
#          마지막에 mergeTwoLists를 호출하여 쪼갰던 아이템을 크기 비교를 통해 정렬하면서 이어붙인다.

# - 런너 기법 :  (fast는 next 2개씩, slow는 next 1개씩, half는 slow의 이전 값)
#              - 구조 :  head(시작) -------- half(slow이전) - slow (중앙) ---------fast(끝)


