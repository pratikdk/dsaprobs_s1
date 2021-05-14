from collections import defaultdict

# uses DFS
class Graph:
    def __init__(self, v_count):
        self.graph = defaultdict(list)
        self.V = v_count

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def level_compute_util(self, u, visited, levels, lvl):
        # function uses dfs
        visited[u] = True
        levels[u] = lvl
        # Loop through adjacents
        for v in self.graph[u]:
            if visited[v] == False:
                self.level_compute_util(v, visited, levels, lvl+1)

    def get_levels(self):
        visited = [False] * self.V
        levels = [0] * self.V
        for i in range(self.V):
            if visited[i] == False:
                self.level_compute_util(i, visited, levels, 0)
        return levels

if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print(g.get_levels())

    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    print(g.get_levels())
