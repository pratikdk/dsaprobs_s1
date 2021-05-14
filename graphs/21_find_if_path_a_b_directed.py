from collections import defaultdict

class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, u, visited, e, stack):
        visited[u] = True
        print("appending:", u)
        stack.append(u)
        if u == e:
            print(stack)
            return True
        for v in self.graph[u]:
            if visited[v] == False:
                if self.dfs_util(v, visited, e, stack):
                    return True
        print('pooping:',u)
        stack.pop()
        return False

    def bfs_util(self, u, visited, e):
        queue = []
        queue.append(u)
        visited[u] = True
        while queue:
            u = queue.pop(0)
            if u == e:
                return True
            for v in self.graph[u]:
                if visited[v] == False:
                    queue.append(v)
                    visited[v] = False
        return False


    def is_path(self, a, b):
        visited = [False] * self.V
        stack = []
        if self.dfs_util(a, visited, b, stack):
            return True
        #print(stack)
        # if self.bfs_util(a, visited, b):
        #     return True
        return False

if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print(g.is_path(1, 3))
    print(g.is_path(3, 1))
