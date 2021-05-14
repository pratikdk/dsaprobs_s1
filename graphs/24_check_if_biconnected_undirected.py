from collections import defaultdict

class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def ap_util(self, u, visited, disc, low, parent):
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
                if self.ap_util(v, visited, disc, low, parent):
                    return True
                # update low based on lowest in subtree
                low[u] = min(low[v], low[u])
                # if its a root node with 1+ childrens, its ap
                if parent[u] == -1 and children > 1:
                    return True
                # if its not a root node, with no backedge, its ap
                if parent[u] != -1 and low[v] >= disc[u]:
                    return True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
        return False

    def is_bcg(self):
        visited = [False] * self.V
        disc = [float('inf')] * self.V
        low = [float('inf')] * self.V
        parent = [-1] * self.V

        # check for two conditions, if true its not biconnected
        # articulation point
        # connectivity
        if self.ap_util(0, visited, disc, low, parent):
            return False

        for i in range(self.V):
            if visited[i] == False:
                return False
        return True



if __name__ == "__main__":
    g1 = Graph(5)
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)
    g1.add_edge(2, 4)
    print(g1.is_bcg())
    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    print(g2.is_bcg())
