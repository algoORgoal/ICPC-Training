# name: 다리 놓기
# date: July 22, 2020
# status: solved

from sys import stdin


def solution():
    total_test_cases = int(stdin.readline().strip())
    for i in range(total_test_cases):
        left_sites, right_sites = [
            int(char) for char in stdin.readline().strip().split(' ')]
        answer = memoization(right_sites, left_sites, [
                             [None] * (i + 1) for i in range(right_sites + 1)])
        print(answer)


def memoization(n, r, memo):
    if memo[n][r]:
        return memo[n][r]
    if r == 0 or r == n:
        memo[n][r] = 1
        return memo[n][r]
    memo[n][r] = memoization(n - 1, r - 1, memo) + memoization(n - 1, r, memo)

    return memo[n][r]


def tabulation(n, r):
    if r > n // 2:
        r = n - r
    table = [[0] * (i + 1) for i in range(n + 1)]
    table[1][0] = 1
    table[1][1] = 1
    for row in range(2, n + 1):
        for col in range(0, row + 1):
            if col == 0 or col == row:
                table[row][col] = 1
                continue
            table[row][col] = table[row - 1][col] + table[row - 1][col - 1]
    return table[n][r]


solution()
