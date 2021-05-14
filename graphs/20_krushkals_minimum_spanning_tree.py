from collections import defaultdict
from functools import total_ordering
import heapq

@total_ordering
class Edge:
    def __init__(self, val=None, a_vertex=None, b_vertex=None):
        self.weight = val
        self.a = a_vertex
        self.b = b_vertex
    def __lt__(self, other):
        return self.weight < other.weight
    def __eq__(self, other):
	    return self.weight == other.weight


class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def union(self, parent, x, y):
        parent[y] = x

    def find_parent(self, parent, x):
        if parent[x] == x:
            return x
        return self.find_parent(parent, parent[x])

    def krushkals_mst_util(self, visited):
        min_heap = []
        # Build(populate) the minheap by inserting edges into it
        for u in self.graph:
            visited[u] = True
            for v, weight in self.graph[u]:
                if visited[v] == False:
                    heapq.heappush(min_heap, Edge(weight, u, v))
        edge_count = 0
        cost = 0
        # Initialize parent array for union-find and to detect cycles
        parent = [u for u in self.graph]
        # keep popping edges until v-1 edges are discoverd and only if pop if heap is nonempty
        while min_heap and edge_count < self.V-1:
            e = heapq.heappop(min_heap)
            a_parent = self.find_parent(parent, e.a)
            b_parent = self.find_parent(parent, e.b)
            if a_parent != b_parent: # non cyclic edge
                edge_count += 1
                cost += e.weight
                # union both ends to have one parent
                self.union(parent, a_parent, b_parent)
        return cost

    def mst_cost(self):
        visited = [False]*self.V
        cost = self.krushkals_mst_util(visited)
        return cost

if __name__ == "__main__":
    g = Graph(7)
    g.add_edge(0, 1, 28)
    g.add_edge(1, 2, 16)
    g.add_edge(2, 3, 12)
    g.add_edge(3, 4, 22)
    g.add_edge(4, 5, 25)
    g.add_edge(5, 0, 10)
    g.add_edge(3, 6, 18)
    g.add_edge(4, 6, 24)
    g.add_edge(1, 6, 14)
    print("MST Cost:", g.mst_cost())
