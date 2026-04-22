from models.node import Node
from models.link import Link

class Network:
    def __init__(self):
        self.nodes = {}
        self.links = []

    def add_node(self, node_id):
        self.nodes[node_id] = Node(node_id, capacity=2)

    def connect_nodes(self, id1, id2):
        node1 = self.nodes[id1]
        node2 = self.nodes[id2]

        link = Link(node1, node2, bandwidth=5)
        self.links.append(link)

        node1.neighbors.append(node2)
        node2.neighbors.append(node1)