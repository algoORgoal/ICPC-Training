# name: 미로 탐색
# date: August 31, 2020
# status: solved

from sys import stdin


def solution():
    n, m = list(map(int, stdin.readline().strip().split(' ')))
    maze = [[int(char) for char in ''.join(stdin.readline().strip())]
            for _ in range(n)]
    answer = bfs(maze, n, m)
    print(answer)


def bfs(maze, n, m):
    start = [0, 0]
    visited = [[False] * m for _ in range(n)]
    queue = []

    queue.append([start, 1])
    visited[0][0] = True

    while queue:
        current = queue.pop(0)
        if is_the_end(n, m, current):
            return current[1]

        available_path = list(filter(
            lambda path: not visited[path[0][0]][path[0][1]] and maze[path[0][0]][path[0][1]], find_passable(n, m, visited, current)))
        for [x, y], step in available_path:
            visited[x][y] = True
        queue = queue + available_path


def is_the_end(n, m, current):
    x, y = current[0]
    if x == n - 1 and y == m - 1:
        return True
    return False


def find_passable(n, m, visited, current):
    [x, y], step = current
    next_step = step + 1
    path = []
    if x + 1 <= n - 1:  # up
        path.append([[x + 1, y], next_step])
    if x - 1 >= 0:  # down
        path.append([[x - 1, y], next_step])
    if y + 1 <= m - 1:  # right
        path.append([[x, y + 1], next_step])
    if y - 1 >= 0:  # left
        path.append([[x, y - 1], next_step])
    return path


solution()

'''
6 7
1000111
1110101
0010101
1110101
1000101
1111101
'''
