from collections import defaultdict

class Graph:
    def __init__(self, v_count):
        self.V = v_count
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    # def dfs_length_util(self, u, visited, parent_length, max_length):
    #     print(parent_length, max_length)
    #     visited[u] = True
    #     for v, weight in self.graph[u]:
    #         if visited[v] == False:
    #             self.dfs_length_util(v, visited, (parent_length+weight), max_length)
    #     if max_length < parent_length:
    #         print("this->",u, max_length ,parent_length)
    #         max_length = parent_length
    #         print("max now:", max_length)

    def dfs_length_util(self, u, visited, parent_length, max_length):
        visited[u] = True
        for v, weight in self.graph[u]:
            if visited[v] == False:
                self.dfs_length_util(v, visited, (parent_length+weight), max_length)
        if max_length[0] < parent_length:
            max_length[0] = parent_length

    # def dfs_length_util(self, u, visited, parent_length, max_length):
    #     print(parent_length, max_length)
    #     visited[u] = True
    #     for v, weight in self.graph[u]:
    #         if visited[v] == False:
    #             self.dfs_length_util(v, visited, (parent_length+weight), max_length)
    #         if max_length[0] < (parent_length+weight):
    #             max_length[0] = (parent_length+weight)
    #     # if max_length < parent_length:
    #     #     print("this->",u, max_length ,parent_length)
    #     #     max_length = parent_length
    #     #     print("max now:", max_length)

    def longest_cable(self):
        max_length = [float('-inf')]
        for i in range(self.V):
            visited = [False]*self.V
            self.dfs_length_util(i, visited, 0, max_length)
        return max_length[0]

if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1, 3)
    g.add_edge(1, 0, 3)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 1, 4)
    g.add_edge(1, 5, 2)
    g.add_edge(5, 1, 2)
    g.add_edge(3, 5, 6)
    g.add_edge(5, 3, 6)
    g.add_edge(4, 5, 5)
    g.add_edge(5, 4, 5)
    print("Longest cable:", g.longest_cable())
    g = Graph(4)
    g.add_edge(0, 1, 2)
    g.add_edge(1, 2, 2)
    g.add_edge(0, 3, 2)
    print("Longest cable:", g.longest_cable())
