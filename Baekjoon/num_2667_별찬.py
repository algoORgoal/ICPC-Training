# name: 단자번호붙이기
# date: September 1, 2020
# status: solved

from sys import stdin


def solution():
    n = int(stdin.readline())
    maps = [[int(char) for char in stdin.readline().strip()]
            for _ in range(n)]
    answer = bfs(maps, n)
    print(len(answer))
    print(*answer, sep="\n")


def bfs(maps, n):
    visited = [[False] * n for i in range(n)]
    count_residents = []
    for i in range(n):
        for j in range(n):
            if is_available([i, j], maps, visited):
                count = 0
                queue = [[i, j]]
                visited[i][j] = True
                while queue:
                    current = queue.pop(0)
                    count += 1
                    paths = list(filter(lambda position: is_available(position, maps, visited),
                                        find_possible_path(current, n)))
                    change_visited(paths, visited)

                    queue = queue + paths
                count_residents.append(count)
    count_residents.sort()
    return count_residents


def find_possible_path(position, n):
    x, y = position
    path = []
    if x - 1 >= 0:  # up
        path.append([x - 1, y])
    if x + 1 < n:  # down
        path.append([x + 1, y])
    if y - 1 >= 0:  # left
        path.append([x, y - 1])
    if y + 1 < n:  # right
        path.append([x, y + 1])
    return path


def is_available(position, maps, visited):
    x, y = position
    if maps[x][y] and not visited[x][y]:
        return True
    return False


def change_visited(paths, visited):
    for x, y in paths:
        visited[x][y] = True


solution()
