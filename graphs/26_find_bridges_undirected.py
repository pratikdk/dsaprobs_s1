from collections import defaultdict

class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridge_util(self, u, visited, disc, low, parent): # similar to ap
        # Perform normal dfs
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        children = 0
        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                children += 1
                self.bridge_util(v, visited, disc, low, parent)
                # update low based on lowest in subtree
                low[u] = min(low[v], low[u])
                # if its not a root node, with no backedge, its ap
                if low[v] > disc[u]:
                    print((u,v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def find_bridges(self):
        visited = [False] * self.V
        disc = [float('inf')] * self.V
        low = [float('inf')] * self.V
        parent = [-1] * self.V
        for i in range(self.V):
            if visited[i] == False:
                self.bridge_util(i, visited, disc, low, parent)
        print()


if __name__ == "__main__":
    g1 = Graph(5)
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)
    g1.find_bridges()
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.find_bridges()
