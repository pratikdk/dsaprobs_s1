class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.front = 0
        self.rear = -1
        self.len = 0
        self.values = [None] * k


    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.rear = (self.rear+1) % len(self.values)
            self.values[self.rear] = value
            self.len += 1
            return True
        return False


    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.front = (self.front+1) % len(self.values)
            self.len -= 1
            return True
        return False


    def Front(self):
        """
        :rtype: int
        """
        return -1 if self.isEmpty() else self.values[self.front]


    def Rear(self):
        """
        :rtype: int
        """
        return -1 if self.isEmpty() else self.values[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.len == 0


    def isFull(self):
        """
        :rtype: bool
        """
        return self.len == len(self.values)


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.Rear())
print(obj.isFull())
print(obj.deQueue())
print(obj.enQueue(4))
print(obj.Rear())
