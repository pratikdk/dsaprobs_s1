class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min_s = []


    def push(self, value):
        """
        :type x: int
        :rtype: None
        """
        if value <= self.getMin():
            self.min_s.append(value)
        self.s.append(value)


    def pop(self):
        """
        :rtype: None
        """
        value = self.s.pop()
        if value == self.min_s[-1]:
            self.min_s.pop()
        return value


    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_s:
            return float('inf')
        else:
            return self.min_s[-1]


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack()
    minStack.push(-2) #;
    minStack.push(0) #;
    minStack.push(-3) #;
    print(minStack.getMin()) #; // return -3
    minStack.pop() #;
    print(minStack.top()) #;    // return 0
    print(minStack.getMin()) #; // return -2
