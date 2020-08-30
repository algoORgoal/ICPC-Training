# name: Term Project
# date: August 29, 2020
# status: solved

import sys
sys.setrecursionlimit(100000000)


def solution():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        edges = {i + 1: int(char)
                 for i, char in enumerate(sys.stdin.readline().strip().split(' '))}
        has_cycles = [0 for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
        for edge in edges:
            path = {}
            start = find_cycle(edges, edge, visited, path, 0)
            if start == -1:
                continue
            path_reversed = {path[node]: node for node in path}
            current = start
            while current in path_reversed:
                student = path_reversed[current]
                has_cycles[student] = 1
                current += 1
        answer = n - sum(has_cycles)
        print(answer)


def find_cycle(edges, current, visited, path, index):
    if current in path:
        return path[current]
    if visited[current]:
        return -1
    visited[current] = True
    path[current] = index
    next1 = edges[current]
    index = find_cycle(edges, next1, visited, path, index + 1)
    return index


solution()
