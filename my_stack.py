class MyStack:
    def __init__(self):
        self.stack = list()

    def put(self, element):
        self.stack.append(element)

    def get(self):
        try:
            return self.stack[-1]
        except IndexError:
            print("стек пуст!")

    def pop(self):
        try:
            del self.stack[-1]
        except IndexError:
            print("стек пуст!")

    def empty(self):
        return len(self.stack) == 0