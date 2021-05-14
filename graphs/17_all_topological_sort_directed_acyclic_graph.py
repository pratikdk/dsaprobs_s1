from collections import defaultdict

class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)
        self.indegree = [0]*self.V

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.indegree[v] += 1

    def topological_sort_util(self, visited, path, all_paths):
        # try all open(Indegree == 0) vertex on each layer
        for u in range(self.V):
            # if indegree == 0 and not visited
            if self.indegree[u] == 0 and visited[u] == False:
                # Detach all outgoing edges(count) from u to its adjacents
                for v in self.graph[u]:
                    self.indegree[v] -= 1
                # finally mark u as visited and add to path
                path.append(u)
                visited[u] = True
                # Recurse on next open vertex
                self.topological_sort_util(visited, path, all_paths)
                # Route exhausted, pop u from path
                for v in self.graph[u]:
                    self.indegree[v] += 1
                path.pop()
                visited[u] = False
        if len(path) == self.V:
            all_paths.append(path.copy())

    def topological_sort(self):
        visited = [False] * self.V
        path = []
        all_paths = []
        self.topological_sort_util(visited, path, all_paths)
        return all_paths


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    print(g.topological_sort())
