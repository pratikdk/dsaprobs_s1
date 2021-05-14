from collections import defaultdict

# uses DFS
class Graph:
    def __init__(self, v_count):
        self.graph = defaultdict(list)
        self.V = v_count

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, u, visited, rec_stack):
        # function uses dfs
        visited[u] = True
        rec_stack[u] = True
        # Loop through adjacents
        for v in self.graph[u]:
            if visited[v] == False:
                if self.is_cyclic_util(v, visited, rec_stack):
                    return True
            elif rec_stack[v] == True: #belongs to current subtree(but visited uptop)
                return True
        rec_stack[u] = False
        return False


    def is_cyclic(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V
        for i in range(self.V):
            if visited[i] == False:
                if self.is_cyclic_util(i, visited, rec_stack):
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
