class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = [[0]*self.V for _ in range(self.V)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

    def bfs_util(self, source, sink, parent):
        visited = [False] * self.V
        # BFS setup
        queue = []
        queue.append(source)
        visited[source] = True
        # BFS Loop
        while queue:
            u = queue.pop(0)
            for idx, value in enumerate(self.graph[u]):
                if visited[idx] == False and value > 0:
                    visited[idx] = True
                    parent[idx] = u
                    if idx == sink:
                        return True
                    queue.append(idx)
        return False # if queue runs out empty, it means there is no find


    def ford_fulkerson(self, source, sink):
        # parent array to backtrack the path to source
        parent = [-1] * self.V
        max_flow = 0
        while self.bfs_util(source, sink, parent):
            path_min_flow = float('inf')
            s = sink
            while s != source:
                path_min_flow = min(path_min_flow, self.graph[parent[s]][s])
                s = parent[s]
            # add path_min_flow to max_flow
            max_flow += path_min_flow
            # update residual capacities of the edges and reverse edges
            # along the path
            s = sink
            while s != source:
                u = parent[s]
                self.graph[u][s] -= path_min_flow
                self.graph[s][u] += path_min_flow
                s = parent[s]
        return max_flow


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1, 16)
    g.add_edge(0, 2, 13)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 12)
    g.add_edge(2, 1, 4)
    g.add_edge(2, 4, 14)
    g.add_edge(3, 2, 9)
    g.add_edge(3, 5, 20)
    g.add_edge(4, 3, 7)
    g.add_edge(4, 5, 4)
    max_flow = g.ford_fulkerson(0, 5)
    print("Max flow:", max_flow)
