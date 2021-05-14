# All pairs shortest path
class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = [[float('inf')]*self.V for _ in range(self.V)]
        for i in range(self.V): self.graph[i][i] = 0

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

    def print_graph(self):
        for row in self.graph:
            for cell in row:
                print(cell, end="\t")
            print("\n")

    def floyd_warshall(self):
        for k in range(self.V): # Paths through each k, i -> k -> j
            # For each pair of i and j
            for i in range(self.V):
                for j in range(self.V):
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])


    def detect_negative_cycle(self):
        # Obtain all pairs shortest paths using floyd warshall algorithm
        self.floyd_warshall()
        # Check if matrix(diagonal) contains any negative weight
        for i in range(self.V):
            if self.graph[i][i] < 0:
                return True

if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, -1)
    g.add_edge(2, 3, -1)
    g.add_edge(3, 0, -1)
    g.print_graph()
    if g.detect_negative_cycle() == True:
        print("Yes")
    else:
        print("No")
