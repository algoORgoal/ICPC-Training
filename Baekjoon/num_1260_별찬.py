# name: DFS와 BFS
# date: July 8, 2020
# status: solved

# edge list structure
# space: 1000 + 10000 = 11000
# time taken:  n * m + 2n = nm
# adjacency list structure
# space: 1000 + 10000 = 11000
# time taken: sum of degree + labeling = 2m + 2n = m + n
# adjacency list matrix structure
# space: 10000 * 10000 = 100,000,000
# time taken: n^2
# therefore, it's obvious that adjacency list strucutre is the best stradegy.

import sys
import operator


class Vertex:
    def __init__(self, element):
        self.incidence_list = []
        self.visited = False
        self.element = element


class Edge:
    def __init__(self, origin=None, destination=None):
        self.origin = origin
        self.destination = destination
        self.visited = False


# adjacency list structure


class Graph:
    def __init__(self, vertices_amount, entry_point):
        self.vertices_list = [Vertex(i) for i in range(vertices_amount + 1)]
        self.edges_list = []
        self.entry_point = entry_point

    def connect(self, start, end):
        origin = self.vertices_list[start]
        destination = self.vertices_list[end]
        edge = Edge(origin, destination)
        self.edges_list.append(edge)
        origin.incidence_list.append(edge)
        destination.incidence_list.append(edge)

    def DFSUtil(self):
        self.initialize()
        start = self.vertices_list[self.entry_point]
        self.DFS(start)
        print()

    def DFS(self, vertex):
        if (vertex.visited == True):
            return
        vertex.visited = True
        print(vertex.element, end=" ")
        for edge in vertex.incidence_list:
            if (edge.visited):
                continue
            edge.visited = True
            opposite_vertex = self.opposite(vertex, edge)
            self.DFS(opposite_vertex)

    def BFSUtil(self):
        self.initialize()
        start = self.vertices_list[self.entry_point]
        self.BFS(start)
        print()

    def BFS(self, start):
        queue = []
        queue.append(start)
        start.visited = True
        while (len(queue) > 0):
            vertex = queue.pop(0)
            print(vertex.element, end=" ")
            for edge in vertex.incidence_list:
                if (edge.visited):
                    continue
                edge.visited = True
                opposite_vertex = self.opposite(vertex, edge)
                if (not opposite_vertex.visited):
                    opposite_vertex.visited = True
                    queue.append(opposite_vertex)

    def initialize(self):
        for vertex in self.vertices_list:
            vertex.visited = False
        for edge in self.edges_list:
            edge.visited = False

    def opposite(self, vertex, edge):
        return edge.destination if vertex is edge.origin else edge.origin

    def print_graph(self):
        for vertex in self.vertices_list:
            print("{}: ".format(vertex.element))
            for edge in vertex.incidence_list:
                print("{}, {}".format(edge.origin.element, edge.destination.element))
            print()
        print()


def solution():
    vertices_amount, edges_amount, start = list(
        map(int, sys.stdin.readline().split(' ')))
    graph = Graph(vertices_amount, start)
    edges = []
    for i in range(edges_amount):
        start, end = list(
            map(int, sys.stdin.readline().split(' ')))
        start, end = (end, start) if start > end else (start, end)
        edges.append([start, end])
    sorted_edges = sorted(edges, key=operator.itemgetter(0, 1))
    for edge in sorted_edges:
        start, end = edge
        graph.connect(start, end)
    graph.DFSUtil()
    graph.BFSUtil()


solution()
