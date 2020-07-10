# name: 연결 요소의 개수
# date: July 11, 2020
# status: solved


from sys import stdin

# adjacency-list structure


class Vertex:
    def __init__(self, element):
        self.incidence_list = []
        self.element = element
        self.visited = False


class Edge:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.visited = False


class Graph:
    def __init__(self, total_vertices):
        self.vertices_list = [Vertex(i) for i in range(total_vertices + 1)]
        self.edges_list = []

    def add_edges(self, edge_positions):
        for origin_position, destination_position in edge_positions:
            origin = self.vertices_list[origin_position]
            destination = self.vertices_list[destination_position]
            edge = Edge(
                origin, destination)
            self.edges_list.append(edge)
            origin.incidence_list.append(edge)
            destination.incidence_list.append(edge)

    def search(self):
        total_connected_components = 0
        for start_vertex in self.vertices_list:
            if start_vertex is self.vertices_list[0]:
                continue
            if not start_vertex.visited:
                self.DFS(start_vertex)
                total_connected_components += 1
        return total_connected_components

    def BFS(self, vertex):
        queue = []
        vertex.visited = True
        queue.append(vertex)
        while queue:
            current_vertex = queue.pop(0)
            for edge in current_vertex.incidence_list:
                if edge.visited:
                    continue
                edge.visited = True
                opposite_vertex = self.find_opposite_vertex(
                    current_vertex, edge)
                if not opposite_vertex.visited:
                    opposite_vertex.visited = True
                    queue.append(opposite_vertex)

    def DFS(self, vertex):
        stack = []
        vertex.visited = True
        stack.append(vertex)
        while stack:
            current_vertex = stack.pop(0)
            for edge in current_vertex.incidence_list:
                if edge.visited:
                    continue
                edge.visited = True
                opposite_vertex = self.find_opposite_vertex(
                    current_vertex, edge)
                if not opposite_vertex.visited:
                    opposite_vertex.visited = True
                    stack.append(opposite_vertex)

    def find_opposite_vertex(self, vertex, edge):
        return edge.origin if vertex is edge.destination else edge.destination

    def print_elements(self):
        for vertex in self.vertices_list:
            print('{}: '.format(vertex.element), end=" ")
            for edge in vertex.incidence_list:
                print('({}, {})'.format(edge.origin.element,
                                        edge.destination.element), end=" ")
            print()


def solution():
    total_vertices, total_edges = list(map(int, stdin.readline().split(' ')))
    edges_list = [list(map(int, stdin.readline().split(' ')))
                  for i in range(total_edges)]
    graph = Graph(total_vertices)
    graph.add_edges(edges_list)
    answer = graph.search()
    print(answer)


solution()
