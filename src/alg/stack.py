from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def put(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return not self.stack
