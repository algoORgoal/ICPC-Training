# name: Term Project
# date: August 29, 2020
# status: solved

import sys


def solution():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        students = {i + 1: int(char)
                    for i, char in enumerate(sys.stdin.readline().strip().split(' '))}
        bullies = 0
        visited = [False for _ in range(n + 1)]
        for student in students:
            incomplete = []
            if visited[student]:
                continue
            current = student
            # find the start node of cycle or the one already visited
            while not visited[current]:
                visited[current] = True
                current = students[current]
            end = current
            current = student
            # find nodes until it's nor in cycle or visited already
            while current != end:
                incomplete.append(current)
                current = students[current]
            bullies += len(incomplete)

        answer = bullies
        print(answer)


solution()
