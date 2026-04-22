class Packet:
    def __init__(self, source, destination, size=1):
        self.source = source
        self.destination = destination
        self.path = []

    def add_hop(self, node_id):
        self.path.append(node_id)