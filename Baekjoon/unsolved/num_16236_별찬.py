# name: 아기 상어
# date: September 3, 2020
# status: solved

# approach: breath first search each time the shark eats fish, moves the shark to the fish, and start bfs again
# label nodes as visited and unvisited => O(n^2) time
# indices serve as edges so we can say there are 2n(n-1) edges
# try bfs for every node => O(2n(n-1)) = O(n^2)
# total time: (O(n^2) + O(n^2)) * O(2n(n-1)) = O(n^4)

from sys import stdin
from operator import itemgetter


def solution():
    n = int(stdin.readline())
    sea = [[int(char) for char in stdin.readline().strip().split(' ')]
           for i in range(n)]
    answer = bfs(n, sea)
    print(answer)


def bfs(n, sea):
    SHARK = 9

    shark_level = 2

    shark_x, shark_y = find_object(n, sea, SHARK)
    # prevent bfs from recognize block 9 as eatable fish
    sea[shark_x][shark_y] = 0
    visited = [[True if i == shark_x and j ==
                shark_y else False for j in range(n)] for i in range(n)]

    exp_point = 0

    queue = [[[shark_x, shark_y], 0]]
    total_time = 0
    candidate = []
    minimal_step = 0
    while queue:
        current = queue.pop(0)
        [x, y], step = current
        if x == y == -1:  # when it finished collecting every possible blocks to step forward
            x, y = sorted(candidate, key=itemgetter(0, 1)).pop(0)
            sea[x][y] = 0
            exp_point += 1
            visited = [[True if i == x and j ==
                        y else False for j in range(n)] for i in range(n)]
            total_time += minimal_step
            queue = []
            candidate = []
            minimal_step = 0

        if 0 < sea[x][y] < shark_level:
            # when the current blcok has fish and it takes longer to get to it
            if minimal_step != 0 and minimal_step < step:
                continue
            visited[x][y] = True
            candidate.append([x, y])

            minimal_step = step if minimal_step == 0 else minimal_step
            # there could be useless search result in it
            queue = queue + [[[-1, -1], 0]]
            # avoid obsolete calculation(the neibors are added two times in the queue without continuing)
            continue
        if exp_point == shark_level:
            exp_point = 0
            shark_level += 1

        path = list(filter(lambda block: is_okay(block, visited, sea,
                                                 shark_level), find_path(x, y, step, n)))
        for [x, y], step in path:
            visited[x][y] = True
        queue = queue + path
    return total_time


def is_okay(block, visited, sea, shark_level):
    [x, y], step = block
    return not visited[x][y] and sea[x][y] <= shark_level


def find_object(n, sea, SHARK):
    for i in range(n):
        for j in range(n):
            if sea[i][j] == SHARK:
                return [i, j]


def find_path(i, j, step, n):
    path = []
    next_step = step + 1
    if i > 0:  # up
        path.append([[i - 1, j], next_step])
    if j > 0:  # left
        path.append([[i, j - 1], next_step])
    if j < n - 1:  # right
        path.append([[i, j + 1], next_step])
    if i < n - 1:  # down
        path.append([[i + 1, j], next_step])

    return path


solution()
