class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, a, b):
        if a not in self.edges:
            self.edges[a] = []
        if b not in self.edges:
            self.edges[b] = []
        self.edges[a].append(b)
        self.edges[b].append(a)

    def print_graph(self):
        for node in self.edges:
            print(f"{node} -> {self.edges[node]}")
