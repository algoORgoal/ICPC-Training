# name: 치즈
# date: September 8, 2020
# status: solved

from sys import stdin


def solution():
    n, m = list(map(int, stdin.readline().strip().split(' ')))
    cheese = [list(map(int, stdin.readline().strip().split(' ')))
              for i in range(n)]
    answer = bfs(cheese, n, m)
    print(answer)


def bfs(cheese, n, m):
    time = 0
    cheese_blocks = [[i, j]
                     for i in range(n) for j in range(m) if cheese[i][j] == 1]
    while cheese_blocks:
        start = [0, 0]
        queue = [start]
        visited = [[False] * m for i in range(n)]
        while queue:
            x, y = queue.pop(0)
            cheese[x][y] = 2

            next_blocks = filter(lambda position: is_position_valid(
                position, n, m) and is_not_visited(visited, position) and is_empty(cheese, position), get_next_blocks(x, y))

            for next_x, next_y in next_blocks:
                visited[next_x][next_y] = True
                queue = queue + [[next_x, next_y]]
        cheese_blocks = remove_melted(cheese, cheese_blocks)

        time += 1
    return time


def get_next_blocks(x, y):
    yield [x - 1, y]  # up
    yield [x + 1, y]  # down
    yield [x, y - 1]  # left
    yield [x, y + 1]  # right


def is_position_valid(position, n, m):
    x, y = position
    return 0 <= x <= n - 1 and 0 <= y <= m - 1


def is_empty(cheese, position):
    x, y = position
    return cheese[x][y] != 1


def is_all_melted(cheese, n, m):
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                return False
    return True


def is_not_visited(visited, position):
    x, y = position
    return not visited[x][y]


def is_outer_space(cheese, position):
    x, y = position
    return cheese[x][y] == 2


def remove_melted(cheese, cheese_blocks):
    melted = list()
    unmelted = list()
    for x, y in cheese_blocks:
        outer_spaces = len(list(filter(lambda position: is_outer_space(
            cheese, position), get_next_blocks(x, y))))
        if outer_spaces >= 2:
            melted += [[x, y]]
        else:
            unmelted += [[x, y]]

    for x, y in melted:
        cheese[x][y] = 2
    return unmelted


solution()


'''
8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0
'''
