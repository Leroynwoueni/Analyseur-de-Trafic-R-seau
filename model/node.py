from queue import Queue

class Node:
    def __init__(self, node_id, capacity):
        self.id = node_id
        self.capacity = capacity
        self.queue = Queue()
        self.neighbors = []

    def receive_packet(self, packet):
        self.queue.put(packet)

    def process_packets(self):
        processed = []
        for _ in range(min(self.capacity, self.queue.qsize())):
            processed.append(self.queue.get())
        return processed