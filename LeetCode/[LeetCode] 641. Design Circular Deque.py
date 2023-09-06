# Solution 1 (정석 풀이 - 연결리스트 ListNode 이용)
class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.maxlen, self.len = k, 0
        self.head.left, self.tail.right = self.tail, self.head # 왼쪽이 head, 오른쪽이 right
    
    
    # (추가) 연결리스트 새 노드 추가 
    def _add (self, node: ListNode, new : ListNode) :
        # 1-- 기존 node의 왼쪽은 n에 넣어두고, node의 왼쪽을 새로운 노드 new를 추가
        # 2-- 새로운 노드 new의 왼쪽과 오른쪽을 원래 노드와 연결
        # 3-- 기존 node의 왼쪽을 new와 연결 
        n = node.left #1
        node.left = new #2
        new.left, new.right = n, node #2
        n.right = new #3
        
    # (삭제) 연결리스트 노드 삭제
    def _del(self, node : ListNode) :
        n = node.left.left # 삭제할 노드에 연결된 노드(왼쪽왼쪽 노드) n에 저장 
        node.left = n # 왼쪽왼쪽 노드를 node의 왼쪽에 연결
        n.right = node # 왼쪽왼쪽 노드의 오른쪽을 node로 연결
    
        
    def insertFront(self, value: int) -> bool:
        if self.len == self.maxlen :
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.len == self.maxlen :
            return False
        self.len += 1
        self._add(self.tail.right, ListNode(value)) # 주의~ self.tail.right (_add함수에서는 left로 접근하므로, right로 넘겨주기)
        return True
        
    def deleteFront(self) -> bool:
        if self.len == 0 : 
            return False
        self.len -= 1
        self._del(self.head)
        return True
    
    def deleteLast(self) -> bool:
        if self.len == 0 : 
            return False
        self.len -= 1
        self._del(self.tail.right.right)  # 주의~ self.tail.right.right
        return True

    def getFront(self) -> int:
        return self.head.left.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.right.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.maxlen


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()




##################################################################
# Solution 2 (편법 풀이 - list 이용)
class MyCircularDeque:

    def __init__(self, k: int):
        self.q = []
        self.k, self.len = k, 0

    def insertFront(self, value: int) -> bool:
        if self.len == self.k :
            return False
        self.len += 1
        self.q.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k :
            return False
        self.len += 1
        self.q.append(value)
        return True
    
    def deleteFront(self) -> bool:
        if self.len == 0 :
            return False
        self.len -= 1
        del self.q[0]
        return True

    def deleteLast(self) -> bool:
        if self.len == 0 :
            return False
        self.len -= 1
        self.q.pop()
        return True

    def getFront(self) -> int:
        return self.q[0] if self.len > 0 else -1

    def getRear(self) -> int:
        return self.q[-1] if self.len > 0 else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()