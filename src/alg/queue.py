class Queue:
    def __init__(self):
        self.queue = list()

    def put(self, element):
        self.queue.append(element)

    def pop(self):
        return self.queue.pop(0)

    def empty(self):
        return not bool(self.queue)
