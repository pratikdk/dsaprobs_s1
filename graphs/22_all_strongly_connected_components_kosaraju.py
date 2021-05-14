from collections import defaultdict

class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        #self.graph[v].append(u)

    def dfs_util(self, u, visited, stack):
        visited[u] = True
        for v in self.graph[u]:
            if visited[v] == False:
                self.dfs_util(v, visited, stack)
        stack = stack.append(u)

    def dfs_util_print(self, u, visited, scc):
        visited[u] = True
        #print(u, end=" ")
        scc.append(u)
        for v in self.graph[u]:
            if visited[v] == False:
                self.dfs_util_print(v, visited, scc)

    def transpose_graph(self):
        g = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                g.add_edge(v, u)
        return g

    def print_SCCs(self):
        stack = []
        visited = [False] * self.V
        # Run DFS to check forward connectivity
        for i in range(self.V):
            if visited[i] == False:
                self.dfs_util(i, visited, stack)
        # reverse the graph
        gr = self.transpose_graph()
        # Pop from stack and run DFs to check backward connectivity
        visited = [False] * self.V
        all_scc = []
        while stack:
            u = stack.pop()
            if visited[u] == False:
                scc = []
                gr.dfs_util_print(u, visited, scc)
                all_scc.append(scc)
                #print("")
        return all_scc

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    print(g.print_SCCs())
    # g = Graph(11)
    # g.add_edge(1, 2)
    # g.add_edge(1, 10)
    # g.add_edge(10, 9)
    # g.add_edge(3, 4)
    # g.add_edge(3, 5)
    # g.add_edge(5, 6)
    # g.add_edge(7, 8)
    # g.print_SCCs()
