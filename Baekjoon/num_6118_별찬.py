# name: Hide and Seek
# date: July 16, 2020
# status: unsolved

from sys import stdin
from operator import itemgetter

# issue(resolved)
# Let's say there're vertices A and B connected to start-point and the greatest paths are through both A and B.
# if element of A < B but last index of the path passing A isn't, there's a problem. This code prints out the last index of A no matter what.
# 1 - 6 - 3
#   - 5 - 4
#   - 2


INDICES = 'indices'
DISTANCE = 'distance'


def solution():

    total_barns, total_paths = list(
        map(int, stdin.readline().strip().split(' ')))
    path_list = [sorted(map(int, stdin.readline().strip().split(' ')))
                 for i in range(total_paths)]
    path_list_sorted = sorted(path_list, key=itemgetter(0, 1))
    g = Graph(total_barns)
    g.add_edges(path_list_sorted)
    min_dex, distance, barns_with_same_paths = g.BFSUtil()
    print(min_dex, distance, barns_with_same_paths)


class Graph:
    def __init__(self, total_vertices):
        self.edge_list = []
        self.vertex_list = [Vertex(i) for i in range(total_vertices + 1)]

    def add_edges(self, vertices_to_connect):
        for origin_pos, destination_pos in vertices_to_connect:
            origin = self.vertex_list[origin_pos]
            destination = self.vertex_list[destination_pos]
            edge = Edge(origin, destination)
            self.edge_list.append(edge)
            origin.incident_list.append(edge)
            destination.incident_list.append(edge)

    def BFSUtil(self):
        queue = []
        start = self.vertex_list[1]
        start.visited = True
        farthest = {INDICES: [0], DISTANCE: 0}
        queue.append([start, 0])
        while len(queue) > 0:
            self.BFS(queue, farthest)
        # print(farthest)

        return [sorted(farthest['indices'])[0], farthest['distance'], len(farthest['indices'])]

    def BFS(self, queue, farthest):
        current_vertex, distance = queue.pop(0)
        if farthest[DISTANCE] < distance:
            farthest[INDICES] = [current_vertex.element]
            farthest[DISTANCE] = distance
        elif farthest[DISTANCE] == distance:
            farthest[INDICES].append(current_vertex.element)
        for edge in current_vertex.incident_list:
            if edge.visited == True:
                continue
            edge.visited = True
            next_vertex = self.opposite(current_vertex, edge)
            if next_vertex.visited == False:
                next_vertex.visited = True
                queue.append([next_vertex, distance + 1])

    def opposite(self, vertex, edge):
        return edge.origin if edge.destination is vertex else edge.destination


class Vertex:
    def __init__(self, element):
        self.incident_list = []
        self.element = element
        self.visited = False
        self.distance = 0


class Edge:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.visited = False


solution()
