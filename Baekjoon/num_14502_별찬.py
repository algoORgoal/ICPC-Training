# name: 연구소
# date: September 1, 2020
# status: solved

from sys import stdin

# time complexity
# build walls: nC3= n(n-1)(n-2)/(3!) = O(n^3)
# search(visit every node): O(n)
# O(n) * O(n^3) =  O(n^4)
# n = 64 => runs 16777216 times


def solution():
    n, m = [int(char) for char in stdin.readline().strip().split(' ')]
    lab = [list(map(int, stdin.readline().strip().split(' ')))
           for _ in range(n)]
    answer = bfs(lab, n, m)
    print(answer)


def bfs(lab, n, m):
    EMPTY = 0
    VIRUS = 2
    cases = generate_walls(lab, n, m)
    virus_positions = [[i, j]
                       for i in range(n) for j in range(m) if lab[i][j] == 2]
    count_walls = sum([1 for i in range(n)
                       for j in range(m) if lab[i][j] == 1]) + 3
    count_polluted = m * n
    for case in cases:
        if any(map(lambda position: is_not_empty(position, lab), case)):
            continue
        lab_with_new_walls = [[lab[i][j] for j in range(m)] for i in range(n)]
        for position in case:
            x, y = position
            lab_with_new_walls[x][y] = 1
        visited = [[False] * m for _ in range(n)]
        count = 0
        for x, y in virus_positions:
            if not visited[x][y]:
                queue = [[x, y]]
                visited[x][y] = True
                while queue:
                    current = queue.pop(0)
                    count += 1
                    next = list(filter(lambda path: is_passable(
                        path, visited, lab_with_new_walls, EMPTY), search(n, m, current)))
                    visit(visited, next)
                    queue = queue + next
        count_polluted = count if count < count_polluted else count_polluted

    maximal_area = m * n - (count_polluted + count_walls)

    return maximal_area


def generate_walls(lab, n, m):
    walls = [[[i, j], [k, l], [o, p]] for i in range(n) for j in range(m) for k in range(i, n) for l in (range(
        m) if k != i else range(j + 1, m)) for o in range(k, n) for p in (range(m) if o != k else range(l + 1, m))]
    return walls


def search(n, m, position):
    x, y = position
    path = []
    if x > 0:  # up
        path.append([x - 1, y])
    if x < n - 1:  # down
        path.append([x + 1, y])
    if y > 0:  # left
        path.append([x, y - 1])
    if y < m - 1:  # right
        path.append([x, y + 1])
    return path


def is_passable(current, visited, lab, space_type=2):
    x, y = current
    return True if lab[x][y] == space_type and not visited[x][y] else False


def visit(visited, path):
    for x, y in path:
        visited[x][y] = True


def is_not_empty(position, lab):
    x, y = position
    return lab[x][y] != 0


solution()
