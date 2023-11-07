# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 풀이1. node를 리스트 저장하여 확인  
#         if not head:
#             return False
#         p = head
#         nodes = []
#         while p:
#             print(nodes)
#             if p in nodes:
#                 return True
#             nodes.append(p)
#             if not p.next:
#                 return False
#             p = p.next
#         return True
    
        # 풀이2. Floyd's tortoise and hare - 투포인터 이용
        """
        fast는 2개씩 앞섬
        slow는 1개씩 앞섬
        """
        fast = slow = head
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False