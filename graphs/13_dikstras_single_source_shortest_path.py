from collections import defaultdict

class distance:
    def __init__(self, i=None):
        self.i = i
        self.val = float('inf')

class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def dijkstra(self, start): #####  find smallest, then relax ###
        #dist = [(i, float('inf')) for i in range(self.V)]
        dist = [distance(i) for i in range(self.V)]
        dist[start].val = 0
        for v, weight in self.graph[start]:
            dist[v].val = weight
        visited = [False] * self.V
        # for d in dist: print(d.val, end="\t")
        # print("")
        visited[start] = True
        while not all(visited):
            u = min({d for idx, d in enumerate(dist) if visited[idx] == False}, key=lambda x: x.val)
            visited[u.i] = True
            for v, weight in self.graph[u.i]:
                # Relax
                if dist[v].val > (dist[u.i].val + weight):
                    dist[v].val = dist[u.i].val + weight
        # for d in dist: print(d.val, end="\t")
        # print("")
        return [d.val for d in dist]


    def print_graph(self):
        # Construct
        print_matrix = [[None]*self.V for _ in range(self.V)]
        for key in self.graph.keys():
            for v, value in self.graph[key]:
                print_matrix[key][v] = value
        # Print constructed matrix
        for row in print_matrix:
            for cell in row:
                print(cell, end="\t")
            print("\n")



if __name__ == "__main__":
    graph = Graph(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 0, 4)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 1, 8)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 5, 4)
    graph.add_edge(2, 8, 2)
    graph.add_edge(3, 2, 7)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 3, 9)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 2, 4)
    graph.add_edge(5, 3, 14)
    graph.add_edge(5, 4, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 5, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 0, 8)
    graph.add_edge(7, 1, 11)
    graph.add_edge(7, 6, 1)
    graph.add_edge(7, 8, 7)
    graph.add_edge(8, 2, 2)
    graph.add_edge(8, 6, 6)
    graph.add_edge(8, 7, 7)
    graph.print_graph()
    print(graph.dijkstra(0))
