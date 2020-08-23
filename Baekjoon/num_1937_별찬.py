# name: 욕심쟁이 판다
# date: August 22, 2020
# status: solved

import sys
sys.setrecursionlimit(10000000)


def solution():
    n = int(sys.stdin.readline())
    forest = [list(map(int, sys.stdin.readline().strip().split(' ')))
              for _ in range(n)]
    answer = find_out_lasting_days(forest, n)
    print(answer)


def find_out_lasting_days(forest, n):
    memo = [[-1] * n for i in range(n)]
    maximum = 0
    for i in range(n):
        for j in range(n):
            if memo[i][j] == -1:
                memoization(forest, i, j, n, memo)
            if maximum < memo[i][j]:
                maximum = memo[i][j]
    return maximum


def memoization(forest, i, j, n, memo):
    lasting_days_list = []
    if memo[i][j] != -1:
        return memo[i][j]
    if i > 0 and forest[i][j] < forest[i - 1][j]:
        lasting_days_list.append(
            memoization(forest, i - 1, j, n, memo))  # up
    if i < n - 1 and forest[i][j] < forest[i + 1][j]:
        lasting_days_list.append(
            memoization(forest, i + 1, j, n, memo))  # down
    if j > 0 and forest[i][j] < forest[i][j - 1]:
        lasting_days_list.append(
            memoization(forest, i, j - 1, n, memo))  # left
    if j < n - 1 and forest[i][j] < forest[i][j + 1]:
        lasting_days_list.append(memoization(
            forest, i, j + 1, n, memo))  # right
    if not lasting_days_list:
        memo[i][j] = 1
        return 1
    memo[i][j] = max(lasting_days_list) + 1
    return memo[i][j]


solution()

# test cases I've tried
'''
4
4 4 4 4
4 4 4 4
4 4 4 4
4 4 4 4

4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

1
1

2
1 2
3 4

2
1 2
4 3
'''
