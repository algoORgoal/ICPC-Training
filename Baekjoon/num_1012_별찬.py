# name: 유기농 배추
# date: July 10, 2020
# status: solved

from sys import stdin


# doesn't exist => 0
# visited => don't have to revisit again
# not visited => visit => set to zero

def solution():
    total_test_cases = int(stdin.readline())
    for i in range(total_test_cases):
        length, width, total_positions = list(
            map(int, stdin.readline().split(' ')))
        graph = create_graph(length, width, total_positions)
        positions = [list(map(int, stdin.readline().split(' ')))
                     for i in range(total_positions)]
        mark_one(graph, positions)
        print(count_subgraph(graph, positions))


def create_graph(length, width, total_positions):
    graph = [[0] * length for i in range(width)]
    return graph


def mark_one(graph, positions):
    for x, y in positions:
        graph[y][x] = 1


def count_subgraph(graph, positions):
    total_subgraphs = 0
    for x, y in positions:
        if (graph[y][x] == 1):
            BFS(graph, len(graph[y]), len(graph), x, y)
            total_subgraphs += 1
    return total_subgraphs


def BFS(graph, length, width, initial_x, initial_y):
    queue = []
    queue.append([initial_x, initial_y])
    graph[initial_y][initial_x] = 0
    while (len(queue) > 0):
        current_x, current_y = queue.pop(0)
        adjacent_positions = find_adjacent_positions(current_x, current_y)
        for next_x, next_y in adjacent_positions:
            if is_in_range(graph, length, width, next_x, next_y) and hasToVisit(graph, next_x, next_y):
                graph[next_y][next_x] = 0
                queue.append([next_x, next_y])


def is_in_range(graph, length, width, x, y):
    return 0 <= y < width and 0 <= x < length


def hasToVisit(graph, x, y):
    return graph[y][x] == 1


def find_adjacent_positions(x, y):
    return [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]


solution()
