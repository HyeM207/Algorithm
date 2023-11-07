# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        # 풀이 1: 새로 이어붙이기
        newList = ListNode(0) # 첫번째 노드는 빈 노드로 시작
        head = newList
        
        node1 = list1
        node2 = list2
        while node1 and node2:
            # "다음" node에 작은 값의 노드를 추가함
            if node1.val <= node2.val: 
                head.next = node1 
                head = head.next
                node1 = node1.next
            else:
                head.next = node2
                head = head.next
                node2 = node2.next
        if node2:
            head.next = node2
        elif node1:
            head.next = node1
        return newList.next