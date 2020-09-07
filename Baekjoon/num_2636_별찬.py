# name: 치즈
# date: Setptember 7, 2020
# status: solved

# 1 <= width, height <= 100
# n = max(width, height)
# the number of vertices: n^2
# the number of edges(the number of indexing): 2n(n-1)
# each search takes n^2 + 2 * 2n(n-1) time = O(n^2) time
# search n/2 times at worst case: O(n^2) * n/2 = O(n^3)

# n <= 100 so it's a decent approach.

from sys import stdin


def solution():
    row, col = list(map(int, stdin.readline().strip().split(' ')))
    cheese = [[int(char) for char in stdin.readline().strip().split(' ')]
              for i in range(row)]
    time, last_spaces = bfs(cheese, row, col)
    print(time)
    print(last_spaces)


def bfs(cheese, row, col):
    time = 0
    last_melted_cheese = 0
    melted_cheese = 0
    visited = [[False for j in range(col)] for i in range(row)]
    while time == 0 or melted_cheese != 0:
        last_melted_cheese = melted_cheese
        melted_cheese = 0
        initial = [0, 0]
        queue = [[initial]]
        while queue:
            x, y = queue.pop(0)
            if cheese[x][y]:
                melted_cheese += 1
                cheese[x][y] = 0
            else:
                blocks = filter(lambda position: is_in_cheese(position, row, col) and not is_visited(visited, position),
                                find_next_block(cheese, row, col, x, y))
                for x, y in blocks:
                    visited[x][y] = True
                    queue = queue + [[x, y]]
        if melted_cheese != 0:
            time += 1

    return time, last_melted_cheese


def find_next_block(cheese, row, col, x, y):
    yield ([x - 1, y])  # up
    yield ([x + 1, y])  # down
    yield ([x, y - 1])  # left
    yield ([x, y + 1])  # right


def is_in_cheese(position, row, col):
    x, y = position
    return 0 <= x < row and 0 <= y < col


def is_visited(visited, position):
    x, y = position
    return visited[x][y]


def is_empty(cheese, row, col):
    for i in range(row):
        for j in range(col):
            if cheese[i][j] != 0:
                return False
    return True


solution()
