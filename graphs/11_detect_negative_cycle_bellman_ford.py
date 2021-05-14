# Single source shortest path
from collections import defaultdict

class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def is_negative_cycle(self):
        dist = [float('inf')]*self.V
        dist[0] = 0

        # Loop atmost V-1 times, V-1 edges for a simple path in a graph
        for _ in range(self.V-1):
            # Relax all edges
            for u in range(self.V):
                for v, weight in self.graph[u]:
                    if dist[u] != float('inf'):
                        if dist[v] > (dist[u] + weight):
                            dist[v] = dist[u] + weight
        print(dist)
        # Detect negative cycle
        for u in range(self.V):
            for v, weight in self.graph[u]:
                if dist[u] != float('inf'):
                    if dist[v] > (dist[u] + weight):
                        print(dist)
                        return True
        return False


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)
    if g.is_negative_cycle() == True:
        print("Yes")
    else:
        print("No")

    g = Graph(4)
    g.add_edge(0, 1, 4)
    g.add_edge(1, 2, -2)
    g.add_edge(2, 0, -4)
    g.add_edge(1, 3, 2)
    if g.is_negative_cycle() == True:
        print("Yes")
    else:
        print("No")
