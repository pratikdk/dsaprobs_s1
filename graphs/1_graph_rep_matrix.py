class adjacency_matrix():
    def __init__(self, vertices):
        self.num_of_vertices = vertices
        self.graph_rep_matrix = [[None for _ in range(self.num_of_vertices)] for _ in range(self.num_of_vertices)]
        self.vertex_to_index_dict = {}
        self.index_to_vertex_list = [None] * self.num_of_vertices

    def set_vertex(self, index, vertex_literal):
        # Map vertex to indices for easy traversal
        if index >= 0 and index < self.num_of_vertices:
            self.vertex_to_index_dict[vertex_literal] = index
            self.index_to_vertex_list[index] = vertex_literal

    def set_edge(self, from_literal, to_literal, edge_weight):
        # First get the index of literal
        from_index = self.vertex_to_index_dict[from_literal]
        to_index = self.vertex_to_index_dict[to_literal]
        self.graph_rep_matrix[from_index][to_index] = edge_weight
        self.graph_rep_matrix[to_index][from_index] = edge_weight

    def get_vertices(self):
        return self.index_to_vertex_list

    def get_edges(self):
        edges = []
        for i in range(len(self.graph_rep_matrix)):
            for j in range(len(self.graph_rep_matrix[0])):
                if self.graph_rep_matrix[i][j]:
                    edges.append((self.index_to_vertex_list[i], self.index_to_vertex_list[j], self.graph_rep_matrix[i][j]))
        return edges

    def get_rep(self):
        return self.graph_rep_matrix

if __name__ == "__main__":
    matrix = adjacency_matrix(6)
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
    print(matrix.get_rep())
    print(matrix.get_edges())
    print(matrix.get_vertices())
