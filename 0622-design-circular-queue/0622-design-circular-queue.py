class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.mlen = k
        self.f = 0
        self.r = 0

    def enQueue(self, value: int) -> bool:        
        if self.q[self.r] is None: 
            self.q[self.r] = value
            if self.r == self.mlen-1:
                self.r = 0
            else: 
                self.r += 1
            return True

        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.f] is None: 
            return False
        else:
            self.q[self.f] = None
            if self.f == self.mlen-1:
                self.f = 0
            else: 
                self.f += 1
            return True
        

    def Front(self) -> int:
        if self.q[self.f] is None: 
            return -1
        return self.q[self.f]

    def Rear(self) -> int:
        if self.q[self.r-1] is None: 
            return -1
        if self.r == 0:
            return self.q[self.mlen-1]
        else:
            return self.q[self.r-1]      
        

    def isEmpty(self) -> bool:
        return self.f == self.r and self.q[self.f] is None
        

    def isFull(self) -> bool:
        return self.f == self.r and self.q[self.f] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()