# Solution 1
class MyCircularQueue:

    def __init__(self, k: int):
        # print("init")
        self.q = [None] * k
        self.q_len = k
        self.front_p = 0
        self.rear_p = 0
        
    def enQueue(self, value: int) -> bool:
        # print("enQueue : ", self.front_p, self.rear_p, self.q)
        if self.q[self.rear_p] is None : 
            self.q[self.rear_p] = value 
            self.rear_p = (self.rear_p + 1) % self.q_len
           
            return True
        else : 
            return False

    def deQueue(self) -> bool:
        # print("deQueue : ", self.front_p, self.rear_p, self.q)
        if self.q[self.front_p] is not None : 
            self.q[self.front_p] = None
            self.front_p = (self.front_p + 1) % self.q_len
            
            return True
        else : 
            return False

    def Front(self) -> int:
        # print("Front : ", self.front_p, self.rear_p, self.q)
        if self.q[self.front_p] is None:
            return -1
        else : 
            return self.q[self.front_p]

    def Rear(self) -> int:
        # print("Rear : ", self.front_p, self.rear_p, self.q)
        if self.q[self.rear_p-1] is None :
            return -1
        else : 
            return self.q[self.rear_p-1]

    def isEmpty(self) -> bool:
        # print("isEmpty : ", self.front_p, self.rear_p, self.q)
        if self.front_p == self.rear_p and self.q[self.front_p] is None :
            return True
        else : 
            return False

    def isFull(self) -> bool:
        # print("isFull : ", self.front_p, self.rear_p, self.q)
        if self.front_p == self.rear_p and self.q[self.front_p] is not None  :
            return True
        else :
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()