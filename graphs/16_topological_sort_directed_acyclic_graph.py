from collections import defaultdict

class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, u, visited, stack):
        visited[u] = True
        for v in self.graph[u]:
            if visited[v] == False:
                self.topological_sort_util(v, visited, stack)
        stack.append(u)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        return stack[::-1]


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    print(g.topological_sort())
