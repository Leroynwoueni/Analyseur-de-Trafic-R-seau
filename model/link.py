class Link:
    def __init__(self, node_a, node_b, bandwidth, latency=1):
        self.node_a = node_a
        self.node_b = node_b
        self.bandwidth = bandwidth
        self.latency = latency
        self.current_load = 0