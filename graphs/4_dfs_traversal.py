from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def set_edge(self, from_vertex, to_vertex):
        self.graph[from_vertex].append(to_vertex)

    def dfs_recursive(self, vertex, visited):
        # mark vertex as Visited
        visited.add(vertex)
        print(vertex, end = " ")
        # Loop over the adjacent vertices of current vertex
        for adjacent_vertex in self.graph[vertex]:
            # only visit the ones what arent visited
            if adjacent_vertex not in visited:
                self.dfs_recursive(adjacent_vertex, visited)

    def dfs_out(self, start_vertex):
        visited = set()
        self.dfs_recursive(start_vertex, visited)

if __name__ == "__main__":
    g = Graph()
    g.set_edge(0, 1)
    g.set_edge(0, 2)
    g.set_edge(1, 2)
    g.set_edge(2, 0)
    g.set_edge(2, 3)
    g.set_edge(3, 3)
    g.dfs_out(2)
