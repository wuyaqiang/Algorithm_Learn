'''
剑指 Offer 第30题 包含 min 函数的栈
leetcode 155. Min Stack
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        self.min_stack.append(min(x, self.getMin()))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return float('inf')