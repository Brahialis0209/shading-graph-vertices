class MyQueue:
    def __init__(self):
        self.queue = list()

    def put(self, element):
        self.queue.append(element)

    def get(self):
        try:
            return self.queue[0]
        except IndexError:
            print("очередь пуста!")

    def pop(self):
        try:
            del self.queue[0]
        except IndexError:
            print("очередь пуста!")

    def empty(self):
        return len(self.queue) == 0