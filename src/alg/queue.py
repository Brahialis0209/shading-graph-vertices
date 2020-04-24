from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def put(self, element):
        self.queue.append(element)

    def pop(self):
        return self.queue.popleft()

    def empty(self):
        return not self.queue
