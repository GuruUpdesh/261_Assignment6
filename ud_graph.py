# Course: Data Structures 261_401
# Author: Guru Updesh Singh
# Assignment: 6
# Description: Implementation of an undirected graph class.

import heapq
from collections import deque


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph
        """
        # if a vertex with the same name as the parameter string already exists in the graph the method will do nothing
        if v in self.adj_list:
            return

        # otherwise add the value to the adjacency list
        self.adj_list[v] = []
        
    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        """
        # if u and v refer to the same vertex the method does nothing
        if u == v:
            return

        # if either or both vertex names do not exist in the graph create them
        if not (u in self.adj_list and v in self.adj_list):
            # if u is not in the graph then create it
            if u not in self.adj_list:
                self.add_vertex(u)
            # if v is not in the graph then create it
            if v not in self.adj_list:
                self.add_vertex(v)

        # if an edge already exists in the graph the method does nothing (we only check for this
        elif v in self.adj_list[u] and u in self.adj_list[v]:
            return

        # otherwise update the list of vertices connected to the key (either u or v)
        self.adj_list[v].append(u)
        self.adj_list[u].append(v)

    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        # if u or/and v do not exist in the graph the method does nothing
        if v not in self.adj_list or u not in self.adj_list:
            return
        # if there is no edge between u and v the method doesnt does nothing
        if not (v in self.adj_list[u] and u in self.adj_list[v]):
            return

        # otherwise remove the edge between the two parameter vertices (u and v)
        self.adj_list[v].remove(u)
        self.adj_list[u].remove(v)

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """
        # if the given vertex does not exist the method does nothing
        if v not in self.adj_list:
            return

        for successor in self.adj_list[v]:
            self.adj_list[successor].remove(v)

        self.adj_list.pop(v)

    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        vertices_list = []

        # for every vertex in the adjacency list add it to the return list
        for i in self.adj_list:
            vertices_list.append(i)

        return vertices_list

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        vertices_list = self.get_vertices()
        edges = []
        # for each vertex
        for cur_vertex in vertices_list:
            # for each successor of the current vertex
            for successor in self.adj_list[cur_vertex]:
                # if the edge between the two vertices isn't already in the edges list append the current edge to
                # the edges list
                if (successor, cur_vertex) not in edges:
                    edges.append((cur_vertex, successor))
        return edges

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        # if the path is empty that path is considered valid
        if len(path) == 0:
            return True

        if path[0] not in self.adj_list:
            return False

        # look through the path ensuring that the paths order vertex to vertex is an edge in the graph
        for index in range(1, len(path)):
            # if the previous index does not have an edge to the next index return False
            if path[index] not in self.adj_list[path[index - 1]] or path[index] not in self.adj_list:
                return False
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """
        visited_vertices = []   # Initialize an empty list of visited vertices
        stack = deque() # Initialize an empty stack

        # if the starting vertex is in the graph add it to the stack
        if v_start in self.adj_list:
            stack.append(v_start)

        # if the stack is not empty, pop a vertex
        while len(stack) > 0:
            vertex = stack.pop()

            # if the vertex is not in the list of visited vertices
            if vertex not in visited_vertices:
                visited_vertices.append(vertex)     # add the vertex to the list of visited vertices

                # if the vertex popped is the end vertex break
                if vertex == v_end:
                    break

                # push each vertex that is a direct successor of the current vertex to the stack

                # to get a list of vertices to add to the stack sort the list adjacency list for the vertex
                successors = self.adj_list[vertex]
                successors.sort()
                # reverse the order of the list so that when we continue the search the stack will pop the vertices
                # in ascending lexicographical order
                successors.reverse()
                for successor in successors:
                    stack.append(successor)

        return visited_vertices

    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        visited_vertices = []  # Initialize an empty list of visited vertices
        queue = deque()  # Initialize an empty queue

        # if the starting vertex is in the graph add it to the queue
        if v_start in self.adj_list:
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

                # to get a list of vertices to add to the queue sort the list adjacency list for the vertex
                successors = self.adj_list[vertex]
                successors.sort()
                for successor in successors:
                    # if the vertex is not already visited enqueue it to the queue
                    if successor not in visited_vertices:
                        queue.append(successor)

        return visited_vertices

    def count_connected_components(self):
        """
        Return number of connected components in the graph
        """
        count = 0   # initialize count to zero
        visited_vertices = set()   # keep a list of visited vertices
        stack = deque()     # initialize an empty stack

        # if the number of nodes is greater than zero
        if len(self.adj_list) > 0:
            # append the first key value the the stack
            stack.append(next(iter(self.adj_list.items()))[0])

        # while the stack is empty
        while len(stack) > 0:
            pop = stack.pop()  # pop the value in the stack
            dfs = self.dfs(pop)     # get a list of all the connected vertices

            # for each vertices in this connected component add it to the visited vertices set
            for vertex in dfs:
                visited_vertices.add(vertex)

            # for each vertex in the graph
            for vertex in self.adj_list:
                # if the vertex has not yet been visited
                if vertex not in visited_vertices:
                    # append it to the stack
                    stack.append(vertex)
                    break

            # increment count since we just discovered a connected component in the graph
            count += 1

        return count

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
        # for each vertex in  the graph
        for vertex in self.adj_list:
            # if the recursive helper function finds a cycle return True
            if self.rec_helper(vertex, None, set()) is True:
                return True

        # if we get through all the vertices and haven't found a single cycle return False
        return False

    def rec_helper(self, current, parent, visited):
        """
        Returns true if the graph passed to the method has a cycle. Otherwise return False.
        """
        visited.add(current)    # add the current vertex to the visited vertices set

        # for all the current vertex's successors if the vertex has not been visited check to see if it has a cycle
        for vertex in self.adj_list[current]:
            # if the vertex has been visited and is not the parent vertex then we return True since we have found
            # a cycle
            if vertex in visited and vertex != parent:
                return True
            # otherwise if vertex has not been visited check to see if it has a cycle
            if vertex not in visited:
                # if its does have a cycle return True
                if self.rec_helper(vertex, current, visited): return True

        # otherwise return False
        return False


if __name__ == '__main__':

    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = UndirectedGraph()
    # print(g)
    #
    # for v in 'ABCDE':
    #     g.add_vertex(v)
    # print(g)
    #
    # g.add_vertex('A')
    # print(g)
    #
    # for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
    #     g.add_edge(u, v)
    # print(g)
    #
    #
    # print("\nPDF - method remove_edge() / remove_vertex example 1")
    # print("----------------------------------------------------")
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    # g.remove_vertex('DOES NOT EXIST')
    # g.remove_edge('A', 'B')
    # g.remove_edge('X', 'B')
    # print(g)
    # g.remove_vertex('D')
    # print(g)
    # #
    # #
    # print("\nPDF - method get_vertices() / get_edges() example 1")
    # print("---------------------------------------------------")
    # g = UndirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    #
    # #
    # print("\nPDF - method is_valid_path() example 1")
    # print("--------------------------------------")
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    # test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    # for path in test_cases:
    #     print(list(path), g.is_valid_path(list(path)))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')

    #
    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()
    #
    #
    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
