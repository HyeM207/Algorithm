# Solution 1 - (편법)
class MyHashMap:

    def __init__(self):
        self.hashmap = defaultdict(int)
        

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value
        print(self.hashmap[key])
                           
    def get(self, key: int) -> int:
        return self.hashmap[key] if key in self.hashmap else -1

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            self.hashmap.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


#################################################################
# Solution 2 - (정석풀이_ 책 참고)
# (새로 정의) ListNode
class ListNode : 
    def __init__(self, key=None, value=None) :
        self.key = key
        self.value =value 
        self.next = None 
        
class MyHashMap:

    def __init__(self):
        self.table = defaultdict(ListNode)
        # size가 있고, table에 저장되는 key값은 key % size 즉, index 값이다
        self.size = 1000
        

    def put(self, key: int, value: int) -> None:
        index = key % self.size 
        
        # key가 테이블에 없다면 삽입 후 종료
        if self.table[index].key is None : # <---주의! (defaultdict이라 key값이 없으면 바로 생성하기 때문에 다음과 같이 쓸 것!)
            self.table[index] = ListNode(key, value) # ListNode(val, next)
            return 
        
        # key가 테이블에 있다면 연결리스트로 연결 후 종료
        node = self.table[index]
        while node :
            if node.key == key :  
                node.value = value 
                return 
            if node.next == None :
                node.next = ListNode(key, value)
                break
            node = node.next  
        

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].key is None :
            return -1
        
        node = self.table[index]
        while node : 
            if node.key == key :
                return node.value
            node = node.next
        return -1

    
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].key is None :
            return
        
        node = self.table[index]
        # case 1 - 삭제할 노드가 첫번째 노드일 경우
        if node.key == key :
            self.table[index] = ListNode() if node.next is None else node.next # <---주의!
            return     

        
        # case 2 - 연결리스트 노드 삭제
        prev = node
        while node :
            if node.key == key :
                prev.next = node.next
                return
            prev, node = node, node.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)