# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []
        
        # 연결 리스트의 루트를 heapq에 저장 (루트, 연결리스트 idx, 연결리스트)
        for i in range(len(lists)) :
            if lists[i] : 
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                
        
        # 힙 추출 후 다음 노드는 다시 저장 
        while heap : 
            node = heapq.heappop(heap) # 가장 작은 원소를 가진 연결리스트 pop
            idx = node[1] # 연결리스트 idx
            result.next = node[2] # 연결리스트 
            
            result = result.next # 다음 노드로 이동 
            
            if result.next : 
                # 가장 작은 원소 하나를 뺀 상태의 연결리스트를 다시 push
                heapq.heappush(heap, (result.next.val, idx, result.next)) 
            
        return root.next