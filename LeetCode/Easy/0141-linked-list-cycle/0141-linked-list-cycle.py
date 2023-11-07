# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
중복된 값이 노드 값으로 들어갈 수 있음
사이클인지 확인 방법은?
    - 끝까지 가본다 (순회 횟수 넘어가면 True)
    - node의 주소값  X 
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p = head
        nodes = []
        while p:
            if p in nodes:
                return True
            nodes.append(p)
            if not p.next:
                return False
            p = p.next
        return True