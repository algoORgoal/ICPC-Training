# name: Adding 1s, 2s, and 3s
# date: July 15, 2020
# status: solved

from sys import stdin


def solution():
    total_test_cases = int(stdin.readline())
    for i in range(total_test_cases):
        n = int(stdin.readline())
        memo = [0 for i in range(n + 1)]
        answer = count_expressions(n, memo)
        print(answer)


def count_expressions(n, memo):
    if memo[n]:
        return memo[n]
    if n == 1:
        memo[n] = 1
        return memo[n]
    if n == 2:
        memo[n] = 1 + count_expressions(n - 1, memo)
        return memo[n]
    if n == 3:
        memo[n] = 1 + count_expressions(n - 1, memo) + \
            count_expressions(n - 2, memo)
        return memo[n]
    memo[n - 3] = count_expressions(n-3, memo)
    memo[n - 2] = count_expressions(n-2, memo)
    memo[n - 1] = count_expressions(n-1, memo)
    return memo[n - 1] + memo[n - 2] + memo[n - 3]


solution()
