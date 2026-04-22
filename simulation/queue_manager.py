from collections import deque

class QueueManager:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, packet):
        self.queue.append(packet)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return None