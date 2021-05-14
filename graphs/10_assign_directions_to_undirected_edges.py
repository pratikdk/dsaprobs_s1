# uses DFS
class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = [[None]*self.V for _ in range(self.V)]


    def print_graph(self):
        for row in self.graph:
            for cell in row:
                print(cell, end="\t")
            print("\n")


    def add_edge(self, u, v):
        self.graph[u][v] = 1


    def topological_sort_util(self, u, visited, stack):
        visited[u] = True

        for v, val in enumerate(self.graph[u]):
            if val and visited[v] == False:
                if self.graph[v][u] is None:
                    self.topological_sort_util(v, visited, stack)
        # insert u into stack
        stack.append(u)


    def assign_directions(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        # Reverse the stack, increasing dependency order
        stack = stack[::-1]
        print(stack)
        # Iterate through graph, assign directions to undirected edges based on position in stack
        for i in range(self.V):
            for j in range(i, self.V):
                if self.graph[i][j] and self.graph[j][i]:
                    if stack.index(i) < stack.index(j):
                        # keep edge from i -> j, because i comes before j, that means shutdown j -> i
                        self.graph[j][i] = None
                    else: # keep edge from j -> i, because j comes before i, that means shutdown i -> j
                        self.graph[i][j] = None


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(5, 2)
    g.add_edge(5, 4) #
    g.add_edge(4, 5) #
    g.add_edge(3, 4)
    g.add_edge(3, 0) #
    g.add_edge(0, 3) #
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(0, 5)
    g.add_edge(5, 1)
    g.add_edge(0, 2) #
    g.add_edge(2, 0) #
    g.add_edge(0, 5)
    g.add_edge(2, 4)
    g.add_edge(1, 4)
    g.print_graph()
    g.assign_directions()
    print()
    g.print_graph()
