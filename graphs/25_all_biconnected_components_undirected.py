from collections import defaultdict

class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)
        self.time = 0
        self.count = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def all_bcc_util(self, u, visited, disc, low, parent, stack):
        # Perform normal dfs
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        children = 0
        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                children += 1
                stack.append((u, v))
                self.all_bcc_util(v, visited, disc, low, parent, stack)
                # update low for u based on lowest in subtree of u
                low[u] = min(low[v], low[u])
                # if its a root node with 1+ childrens, its ap
                # if its not a root node, with no backedge, its ap
                if (parent[u] == -1 and children > 1) or (parent[u] != -1 and low[v] >= disc[u]):
                    self.count += 1
                    w = -1
                    while w != (u, v):
                        w = stack.pop()
                        print(w, end=" ")
                    print("\n")
            elif v != parent[u] and low[u] > disc[v]:
                low[u] = min(low[u], disc[v])
                stack.append((u, v))
        return False

    def all_bcc(self):
        visited = [False] * self.V
        disc = [float('inf')] * self.V
        low = [float('inf')] * self.V
        parent = [-1] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.all_bcc_util(i, visited, disc, low, parent, stack)
            if stack:
                self.count += 1
                while stack:
                    w = stack.pop()
                    print(w, end=" ")
                print("\n")

if __name__ == "__main__":
    g = Graph(12)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(1, 5)
    g.add_edge(0, 6)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(5, 8)
    g.add_edge(7, 8)
    g.add_edge(8, 9)
    g.add_edge(10, 11)
    g.all_bcc()
