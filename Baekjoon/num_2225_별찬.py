# name: 합분해
# date: July 23, 2020
# status: solved

import sys
# for recursion
sys.setrecursionlimit(100000000)


def solution():
    n, k = list(map(int, sys.stdin.readline().strip().split(' ')))

    # combination with repetition:
    answer = homogeneous(k, n)

    # memoization:
    # memo = [[None for _ in range(k + 1)] for _ in range(n + 1)]
    # answer = memoization(n, k, memo)

    # tablulation:
    # answer = tabulation(n, k)

    print(answer % 1000000000)


def memoization(n, k, memo):
    if memo[n][k]:
        return memo[n][k]
    if n == 0:
        return 1
    if k == 1:
        return 1
    memo[n][k] = 0
    for i in range(0, n + 1):
        memo[n - i][k - 1] = memoization(n - i, k - 1, memo)
        memo[n][k] += memo[n - i][k - 1]
    return memo[n][k]


def tabulation(n, k):
    row = n + 1
    col = k + 1
    table = [[None] * col for _ in range(row)]
    for y in range(0, row):
        table[y][1] = 1
    for x in range(2, col):
        for y in range(row):
            table[y][x] = sum([table[i][x - 1] for i in range(0, y + 1)])
    return table[n][k]


# H(n, r): distribute r identical objects amoung n people
# a1 + a2 + a3 + ... + ak = N
# equals distribute N identical objects amung K people = H(K, N) = C(N + K - 1, K - 1) = C(N + K - 1, N)
def homogeneous(n, r):
    length = n + r - 1
    memo = [[None] * (length + 1) for _ in range(length + 1)]

    # memoization:
    if r < n - 1:
        return combination_memoization(n + r - 1, r, memo)
    return combination_memoization(n + r - 1, n - 1, memo)

    # tabulation:
    # if r < n - 1:
    #     return combination_tabulation(n + r - 1, r)
    # return combination_tabulation(n + r - 1, n - 1)


def combination_memoization(n, r, memo):
    if memo[n][r]:
        return memo[n][r]
    if r == 0 or r == n:
        memo[n][r] = 1
        return memo[n][r]
    memo[n][r] = combination_memoization(
        n-1, r, memo) + combination_memoization(n-1, r-1, memo)
    return memo[n][r]


def combination_tabulation(n, r):
    table = [[None] * (i + 1) for i in range(n + 1)]
    table[1][0] = table[1][1] = 0
    for row in range(1, n + 1):
        for col in range(row + 1):
            if col == 0 or col == row:
                table[row][col] = 1
                continue
            table[row][col] = table[row - 1][col] + table[row - 1][col - 1]
    return table[n][r]


solution()
