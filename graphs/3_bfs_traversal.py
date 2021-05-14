from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def set_edge(self, from_vertex, to_vertex):
        self.graph[from_vertex].append(to_vertex)

    def bfs_out(self, start_vertex):
        # Keep track of which verices are visited
        visited = set()
        # queue, which stores vertices to traverse
        queue = []
        queue.append(start_vertex)
        visited.add(start_vertex)
        # traverse the graph
        while queue:
            # pop the front of queue
            current_vertex = queue.pop(0)
            print(current_vertex, end=" ")
            # get adjacent vertices to the current vertex
            # check if not visited
            # push them into queue
            for adjacent_vertex in self.graph[current_vertex]:
                if adjacent_vertex not in visited:
                    queue.append(adjacent_vertex)
                    # Mark the adjacent vertex as Visited
                    visited.add(adjacent_vertex)

if __name__ == "__main__":
    g = Graph()
    g.set_edge(0, 1)
    g.set_edge(0, 2)
    g.set_edge(1, 2)
    g.set_edge(2, 0)
    g.set_edge(2, 3)
    g.set_edge(3, 3)
    g.bfs_out(2)
