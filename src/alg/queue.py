from src.alg.container import Container


class Queue(Container):
    def pop(self):
        return self.container.popleft()

