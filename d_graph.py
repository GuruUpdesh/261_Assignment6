# Course: CS261 - Data Structures
# Author: Guru Updesh Singh
# Assignment: 6
# Description: Implementation of a direction graph class and its methods.

import heapq

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        This method adds a new vertex to the graph. The name of the vertex is not provided instead the vertex is given
        a reference index. The first vertex will have a reference index of 0 and subsequent vertices will have reference
        index values 1, 2, 3 etc. The add_vertex method returns the number of vertices in the graph after addition.
        """
        # update the number of vertices
        self.v_count += 1

        # add a column by adding an empty space to the end of each row
        for i in range(self.v_count-1):
            self.adj_matrix[i].append(0)

        # add new row to the end of the adjacency list
        row = []
        for i in range(self.v_count):
            row.append(0)
        self.adj_matrix.append(row)

        # return the number of vertices in the graph after addition
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        This method adds a new edge to the graph by connecting the two parameter vertices. If an edge already
        exists in the graph the method will update the weight of that edge.
        """
        # if the two provided index values are the same or if either or both vertex indices do not exist
        # or if the weight is not a positive integer the method does nothing
        if src == dst or weight < 0 or not (0 <= src < self.v_count and 0 <= dst < self.v_count):
            return

        # if an edge already exists in the graph the method will update the weight of that edge otherwise
        # the method adds a new edge to the graph
        self.adj_matrix[src][dst] = weight

    def is_valid_index(self, index) -> bool:
        if index < 0:
            return False
        if self.v_count - 1 < index:
            return False
        return True

    def remove_edge(self, src: int, dst: int) -> None:
        """
        This method removes the edge between the two parameter vertices.
        """
        # if the two provided index values are the same or if either or both vertex indices do not exist
        # or the edge doesnt exist the method does nothing
        if src == dst or not (0 <= src < self.v_count and 0 <= dst < self.v_count):
            return

        self.adj_matrix[src][dst] = 0


    def get_vertices(self) -> []:
        """
        This method returns a list of vertices in the graph.
        The list is in no particular order
        """
        vertices_list = []
        for i in range(self.v_count):
            vertices_list.append(i)
        return vertices_list

    def get_edges(self) -> []:
        """
        This method returns a list of edges in the graph where each edge is represented as the tuple:
            (source vertex, destination vertex, weight)
        The list is in no particular order
        """
        edges = []
        for row in range(self.v_count):
            for column in range(self.v_count):
                if self.adj_matrix[row][column] != 0:
                    edges.append((row, column, self.adj_matrix[row][column]))
        return edges

    def is_valid_path(self, path: []) -> bool:
        """
        TODO: Write this implementation
        """
        pass

    def dfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        pass

    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        pass

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
        pass

    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':
    g = DirectedGraph()
    for _ in range(5):
        g.add_vertex()
    g.add_edge(0, 1, 10)
    print(g)


    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))
    #
    #
    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for start in range(5):
    #     print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')
    #
    #
    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    #
    # edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    # for src, dst in edges_to_remove:
    #     g.remove_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    #
    # edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    # for src, dst in edges_to_add:
    #     g.add_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    # print('\n', g)
    #
    #
    # print("\nPDF - dijkstra() example 1")
    # print("--------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for i in range(5):
    #     print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    # g.remove_edge(4, 3)
    # print('\n', g)
    # for i in range(5):
    #     print(f'DIJKSTRA {i} {g.dijkstra(i)}')
