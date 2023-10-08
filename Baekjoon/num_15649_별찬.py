# pick m numbers out of [1...n]
from collections import deque


def solution():
    n, m = [int(string) for string in input().split(' ')]

    for i in range(1, n + 1):
        root = [i]
        queue = deque()

        queue.appendleft(root)

        while len(queue) > 0:
            current = queue.pop()
            if len(current) == m:
                print(*current, sep=" ")

            for j in range(1, n + 1):
                if j not in current:
                    new = current + [j]
                    queue.appendleft(new)


solution()
