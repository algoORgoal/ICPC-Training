# name: 피보나치 함수
# date: July 15, 2020
# status: solved

from sys import stdin


def solution():
    total_test_cases = int(stdin.readline())
    for i in range(total_test_cases):
        n = int(stdin.readline())
        memo = [[0, 0] for i in range(n + 1)]
        answer = fibonacci_counter(n, memo)
        print(answer[0], answer[1])


def fibonacci_counter(n, memo):
    if memo[n] != [0, 0]:
        return memo[n]
    if n == 0:
        memo[n][0] += 1
        return memo[n]
    if n == 1:
        memo[n][1] += 1
        return memo[n]
    memo[n - 1] = fibonacci_counter(n - 1, memo)
    memo[n - 2] = fibonacci_counter(n - 2, memo)
    memo[n] = [memo[n - 1][0] + memo[n - 2]
               [0], memo[n - 1][1] + memo[n - 2][1]]
    return memo[n]


solution()
