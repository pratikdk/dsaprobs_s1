class adjacency_list():
    def __init__(self, vertices):
        self.num_of_vertices = vertices
        self.graph_rep_list = [[] for i in range(self.num_of_vertices)]
        self.vertex_to_index_dict = {}
        self.index_to_vertex_list = [None] * self.num_of_vertices

    def set_vertex(self, index, vertex_literal):
        # Map vertex to indices for easy traversal
        if index >= 0 and index < self.num_of_vertices:
            self.vertex_to_index_dict[vertex_literal] = index
            self.index_to_vertex_list[index] = vertex_literal

    def set_edge(self, from_literal, to_literal, edge_weight):
        from_index = self.vertex_to_index_dict[from_literal]
        to_index = self.vertex_to_index_dict[to_literal]
        self.graph_rep_list[from_index].append((to_literal, edge_weight))
        self.graph_rep_list[to_index].append((from_literal, edge_weight))

    def get_vertices(self):
        return self.index_to_vertex_list

    def print_rep(self):
        for i in range(len(self.graph_rep_list)):
            print(f"{self.index_to_vertex_list[i]} -> {self.graph_rep_list[i]}")


if __name__ == "__main__":
    matrix = adjacency_list(6)
    matrix.set_vertex(0,'a')
    matrix.set_vertex(1,'b')
    matrix.set_vertex(2,'c')
    matrix.set_vertex(3,'d')
    matrix.set_vertex(4,'e')
    matrix.set_vertex(5,'f')
    matrix.set_edge('a','e',10)
    matrix.set_edge('a','c',20)
    matrix.set_edge('c','b',30)
    matrix.set_edge('b','e',40)
    matrix.set_edge('e','d',50)
    matrix.set_edge('f','e',60)
    print(matrix.get_vertices)
    matrix.print_rep()
