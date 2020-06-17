from collections import deque


class Container:
    def __init__(self):
        self.container = deque()

    def put(self, element):
        self.container.append(element)

    def empty(self):
        return not self.container
