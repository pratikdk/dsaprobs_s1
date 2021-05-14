from collections import defaultdict

# uses DFS
class Graph:
    def __init__(self, v_count):
        self.graph = defaultdict(list)
        self.V = v_count

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, u, colors):
        """
        white: unvisited
        gray: visiting itself/subtree
        black: visited itself/subtree
        """
        # function uses dfs
        colors[u] = "gray"
        # Loop through adjacents
        for v in self.graph[u]:
            if colors[v] == "white":
                if self.is_cyclic_util(v, colors):
                    return True
            elif colors[v] == "gray": #belongs to current subtree
                return True
        colors[u] = "black"
        return False


    def is_cyclic(self):
        colors = ["white"] * self.V
        for i in range(self.V):
            if colors[i] == "white": # if unvisited
                if self.is_cyclic_util(i, colors):
                    return True
        return False

if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    if g.is_cyclic():
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")
