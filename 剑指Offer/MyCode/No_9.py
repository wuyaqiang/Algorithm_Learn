'''
剑指 Offer 第9题 及其相似题
leetcode 225. Implement Stack using Queues
leetcode 232. Implement Queue using Stacks
'''

import collections

class MyStack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return len(self._queue) == 0


class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.move()
        return self.out_stack.pop()

    def peek(self):
        self.move()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

    def move(self):
        '''
        Move all elements of in_stack to out_stack when out_stack is empty.
        '''
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())





















