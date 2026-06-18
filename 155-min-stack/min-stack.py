class MinStack(object):

    def __init__(self):
        self.min_stack = []
        self.values = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.values.append(value)
        if len(self.min_stack) < 1 or len(self.min_stack) > 0 and value <= self.min_stack[-1]:
            self.min_stack.append(value)

        

    def pop(self):
        """
        :rtype: None
        """
        val = self.values.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.values[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()