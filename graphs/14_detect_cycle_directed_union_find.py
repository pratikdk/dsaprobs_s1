from collections import defaultdict

class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def union(self, parent, x, y):
        parent[x] = y

    def find_parent(self, parent, x):
        if parent[x] == -1:
            return x
        return self.find_parent(parent, parent[x])

    def is_cyclic(self):
        parent = [-1]*self.V

        for i in self.graph:
            x = self.find_parent(parent, i)
            for j in self.graph[i]:
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, y, x) # Broadcast from parent to child / u to v
                print(parent[x])

if __name__ == "__main__":
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    if g.is_cyclic():
        print("Yes")
    else:
        print("No")
