# Solution 1 (책 풀이)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(None)
        while head : 
            # head.val이 cur에 들어갈 위치를 찾는다.
            while cur.next and cur.next.val < head.val : 
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next
        
            cur = parent # parent는 루트를 가리킨다.
        
        return cur.next # 루트의 val은 0부터이니, next로 바꿔준다.


# 후기 : 삽입 정렬 알고리즘은 이전에 전공 수업 때 배워서 어렴풋이 기억은 했지만, 어떤 식으로 구현해야될 지 감이 잡히지 않아 책 풀이를 참고하였다.
# 풀이 : 정렬을 해야 할 대상 (head)와 정렬을 마친 대상(cur) 이렇게 두 그룹으로 나눠서 진행한다.
#       - while문으로 돌며 head의 val값을 cur에 삽입할 위치를 찾는다. (이때 비교 대상은 cur.next.val과 head.val이다.)
#       - 맞는 위치를 찾는다면, cur.next는 head의 값으로, head.next는 현재의 다음값(cur.next)으로 ,head는 다음 값인 head.next를 가리키도록 하낟. 
