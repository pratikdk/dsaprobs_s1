class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.prepare_next(nestedList)


    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return None
        return self.stack.pop().getInteger()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.stack) > 0 and not self.stack[-1].isInteger():
            self.prepare_stack(self.stack.pop().getList())
        return len(self.stack) > 0


    def prepare_stack(self, array):
        for i in range(len(array)-1, -1, -1):
            self.stack.push(array[i])
