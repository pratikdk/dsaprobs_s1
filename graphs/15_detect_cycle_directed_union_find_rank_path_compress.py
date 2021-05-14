from collections import defaultdict

class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def union(self, parent, x, y):
        if parent[x].rank > parent[y].rank:
            parent[y].parent = x
        elif parent[x].rank < parent[y].rank:
            parent[x].parent = y
        else:
            parent[y].parent = x
            parent[x].rank += 1

    def find_parent(self, parent, x): # Path compression
        if parent[x].parent == x:
            return x # parent[x].parent
        parent[x].parent = self.find_parent(parent, parent[x].parent)
        return parent[x].parent

    def is_cyclic(self):
        parent = [Subset(i, 0) for i in range(self.V)]

        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)

if __name__ == "__main__":
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    if g.is_cyclic():
        print("Yes")
    else:
        print("No")
