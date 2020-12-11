class Stack:
    def __init__(self, capacity=None):
        if capacity and capacity < 1:
            raise ValueError("Capacity cannot be <= 0")
        self.capacity = capacity
        self.size = 0
        self.values = []
        if capacity:
            self.values = [None] * self.capacity

    def push(self, value):
        if self.capacity:
            if self.size == self.capacity:
                raise Exception("Stack full!!")
            else:
                self.values[self.size] = value
                self.size += 1
        else:
            self.values.append(value)
            self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        value = None
        if self.capacity:
            value = self.values[self.size-1]
            self.values[self.size-1] = None
        else:
            value = self.values.pop()
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.values[self.size-1]

    def is_full(self):
        if not self.capacity:
            raise Exception("This is a flexible stack")
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def __repr__(self):
        return f"{self.values}" #'%s' % (self.values)


if __name__ == "__main__":
    s1 = Stack()
    for i in range(1, 11):
        s1.push(i)
    for i in range(1, 6):
        s1.pop()
    s1.pop()
    print(s1.peek())
    print(s1)
    print()

    s2 = Stack(10)
    for i in range(1, 11):
        s2.push(i)
    #s2.push(11)
    print(s2.peek())
    for i in range(1, 11):
        s2.pop()
    #s2.pop()
    #s2.peek()
    print(s2)
