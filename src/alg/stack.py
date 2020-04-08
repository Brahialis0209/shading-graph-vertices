class Stack:
    def __init__(self):
        self.stack = list()

    def put(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop(-1)

    def empty(self):
        return not bool(self.stack)
