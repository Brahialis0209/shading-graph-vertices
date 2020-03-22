class Queue:
    def __init__(self):
        self.queue = list()

    def put(self, element):
        self.queue.append(element)

    def get(self):
        try:
            return self.queue[0]
        except IndexError:
            print("queue empty!")

    def pop(self):
        try:
            del self.queue[0]
        except IndexError:
            print("queue empty!")

    def empty(self):
        return len(self.queue) == 0
