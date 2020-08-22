# name: 내리막 길
# date: August 18, 2020
# status: unsolved

import sys
sys.setrecursionlimit(100000000)


def solution():
    m, n = map(int, sys.stdin.readline().strip().split())
    square = [list(map(int, sys.stdin.readline().strip().split()))
              for _ in range(m)]
    memo = [[-1] * n for _ in range(m)]
    answer = memoization(square, 0, 0, m, n, memo)
    print(answer)


def memoization(square, i, j, m, n, memo):
    if memo[i][j] != -1:
        return memo[i][j]
    if i == m - 1 and j == n - 1:
        memo[i][j] = 1
        return 1
    ways_to_go = 0
    if i > 0 and square[i][j] > square[i - 1][j]:
        ways_to_go += memoization(square, i - 1, j, m, n, memo)  # up
    if i < m - 1 and square[i][j] > square[i + 1][j]:
        ways_to_go += memoization(square, i + 1, j, m, n, memo)  # down
    if j > 0 and square[i][j] > square[i][j - 1]:
        ways_to_go += memoization(square, i, j - 1, m, n, memo)  # left
    if j < n - 1 and square[i][j] > square[i][j + 1]:
        ways_to_go += memoization(square, i, j + 1, m, n, memo)  # right
    memo[i][j] = ways_to_go
    return memo[i][j]


solution()

# test cases I've tried
'''
4 3
12 5 4
11 6 3
10 7 2
9 8 1
'''
