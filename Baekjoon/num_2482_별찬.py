# name: 색상환
# date: August 31, 2020
# status: solved

from sys import stdin


def solution():
    n = int(stdin.readline())
    k = int(stdin.readline())
    answer = tabulation(n, k)
    print(answer)


def tabulation(n, k):
    table = [0 for i in range(n + 1)]
    for i in range(1, k + 1):
        updated = [0 for j in range(n + 1)]
        if i == 1:
            for j in range(1, n + 1):
                updated[j] = 1
                table = updated
            continue
        start = 2 * i - 1
        for j in range(start, n):
            updated[j] = updated[j - 1] + table[j - 2]
        updated[n] = updated[n - 1]
        table = updated
    return sum(table) % 1000000003


solution()
