class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # Make another stack to keep track with the min, if the current value > than the min => append the new min to the stack else append the old min to the same stack
        # Append and pop are O(1)

        if self.min_stack == [] or val < self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[len(self.min_stack) - 1])


    def pop(self):
        """
        :rtype: None
        """
        # Pop both of the stack cuz the min_stack act like the min history of the main stack
        self.min_stack.pop()
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]
    # Might faster than self.stack[-1] cuz the later one have to iterate thru the whole list
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[len(self.min_stack) - 1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())

print(obj.pop())
print(obj.top() )

print(obj.getMin())