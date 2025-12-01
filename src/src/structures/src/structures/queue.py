class TestimonyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, testimony):
        self.queue.append(testimony)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def print_all(self):
        for t in self.queue:
            print("- " + t)
