# Course: CS261 - Data Structures
# Author: Guru Updesh Singh
# Assignment: 6
# Description: Implementation of a direction graph class and its methods.

import heapq
from collections import deque

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
        self.adj_matrix.append([0] * self.v_count)

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
        return [vertex for vertex in range(self.v_count)]

    def get_edges(self) -> []:
        """
        This method returns a list of edges in the graph where each edge is represented as the tuple:
            (source vertex, destination vertex, weight)
        The list is in no particular order
        """
        return [(row, column, self.adj_matrix[row][column]) for row in range(self.v_count) for column in range(self.v_count) if self.adj_matrix[row][column] != 0]

    def is_valid_path(self, path: []) -> bool:
        """
        This method takes a list of vertex indices and returns True if the given list of vertices is a valid path in
        the graph. Meaning that one can travel from the first vertex to the last vertex at each step moving over and
        edge in the graph). An empty path is considered valid.
        """
        # an empty path is considered valid
        if not path: return True

        # for each vertex in the path
        for i in range(1, len(path)):
            cur, next = path[i - 1], path[i]
            # if the cur index is not in the graph return False since the path is not valid
            if not 0 <= cur < self.v_count: return False
            # if there is not an edge from the current vertex to the next vertex in the graph return False
            if self.adj_matrix[cur][next] == 0: return False

        # if we make it through the path in the list moving over and edge at each step return True
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in ascending order when presented with multiple options.
        """
        visited_vertices = []  # Initialize an empty list of visited vertices
        stack = deque()  # Initialize an empty stack

        # if the starting vertex is in the graph add it to the stack
        if 0 <= v_start < self.v_count:
            stack.append(v_start)
        # if the stack is not empty, pop a vertex
        while len(stack) > 0:
            vertex = stack.pop()

            # if the vertex is not in the list of visited vertices
            if vertex not in visited_vertices:
                visited_vertices.append(vertex)  # add the vertex to the list of visited vertices

                # if the vertex popped is the end vertex break
                if vertex == v_end:
                    break

                # push each vertex that is a direct successor of the current vertex to the stack
                for i in range(self.v_count-1, -1, -1):
                    if self.adj_matrix[vertex][i] != 0:
                        stack.append(i)
        return visited_vertices

    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        visited_vertices = []  # Initialize an empty list of visited vertices
        queue = deque()  # Initialize an empty queue

        # if the starting vertex is in the graph add it to the queue
        if 0 <= v_start < self.v_count:
            queue.append(v_start)

        # if the queue is not empty, dequeue a vertex
        while len(queue) > 0:
            vertex = queue.popleft()

            # if the vertex is not in the list of visited vertices
            if vertex not in visited_vertices:
                visited_vertices.append(vertex)  # add the vertex to the list of visited vertices

                # if the vertex dequeued is the end vertex break
                if vertex == v_end:
                    break

                # enqueue each vertex that is a direct successor of the current vertex to the queue
                for i in range(self.v_count):
                    if self.adj_matrix[vertex][i] != 0:
                        queue.append(i)
        return visited_vertices

    def has_cycle(self):
        """
        This method returns True if there is at least one cycle in the graph. If the graph is acyclic,
        the method returns False.
        """
        stack = []  # initialize an empty stack
        visited = []    # no vertices have been visited thus this list is empty

        # iterate through all the vertices in the graph
        for vertex in range(self.v_count):
            # if the vertex has yet to be visited
            if vertex not in visited:
                # Check to see if a cycle exists with helper function
                if self.has_cycle_helper(vertex, visited, stack):
                    return True

        # if we get through all the vertices and haven't found a single cycle return False
        return False

    def has_cycle_helper(self, vertex, visited, stack):
        """
        This method takes a vertex, a list of visited vertices and unvisited vertices, and a stack and returns True
        if the sub_graph with the :param vertex has a cycle. The method returns False otherwise.
        """
        stack.append(vertex)     # add the current vertex to the stack
        # for each vertex in the graph
        for vertex_i in range(self.v_count):
            # if the edge exists between that vertex and the current vertex
            if self.adj_matrix[vertex][vertex_i] != 0:
                # if the vertex we are looking at has not been visited and is in the stack return True
                if vertex_i not in visited and vertex_i in stack:
                    return True
                # if the vertex we are looking at has not been visited and the recursive call on that vertex is true
                # return True
                if vertex_i not in visited and self.has_cycle_helper(vertex_i, visited, stack):
                    return True

        stack.remove(vertex)    # remove the current vertex from the stack
        visited.append(vertex)  # we have now visited this vertex so add it to the visited list

        # if we get this far return false
        return False

    def dijkstra(self, src: int) -> []:
        """
        This method implements Dijkstra's algorithm to compute the length of the shortest path from the given parameter
        vertex src to all the other vertices in the graph. It returns a list where the first element is the distance
        between :param src to vertex 0. If a vertex is not reachable its corresponding element in the return list
        will be infinity.
        """
        # Initialize an empty map/hash table representing visited vertices
        visited_vertices = {}   # Key is the vertex v. Value is the min distance d to vertex v.

        # Initialize an empty priority queue, and insert vs into it with distance (priority) 0.
        priority_queue = []
        heapq.heapify(priority_queue)
        heapq.heappush(priority_queue, (0, src))

        # While the priority queue is not empty:
        while len(priority_queue) > 0:
            # Remove the min element in the priority queue
            distance, vertex = heapq.heappop(priority_queue)

            # if the vertex has not been visited
            if vertex not in visited_vertices:
                visited_vertices[vertex] = distance     # Add vertex to the visited map

                # For each direct successor i of vertex:
                for i in range(self.v_count):
                    if self.adj_matrix[vertex][i] != 0:
                        # insert i into the priority queue
                        heapq.heappush(priority_queue, (distance + self.adj_matrix[vertex][i], i))

        # now we must create the return list
        min_distance_list = []
        for i in range(self.v_count):
            if i in visited_vertices:   # if the index has been visited get the distance and append that
                min_distance_list.append(visited_vertices[i])
            else:   # otherwise the index cannot be visited from the given start index and thus the distance is infinity
                min_distance_list.append(float('inf'))

        return min_distance_list


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

    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')
    # #
    # #
    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)

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

    # print("\n Personal examples for has_cycle")
    # print("--------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # print(g)
    # print(g.has_cycle())