# name: 가장 긴 증가하는 부분 수열
# date: August 14, 2020
# status: solved

import sys
sys.setrecursionlimit(100000000)


def solution():
    total_series = int(sys.stdin.readline())
    series = list(map(int, sys.stdin.readline().strip().split(' ')))
    answer = memoization(series, -1, len(series) - 1, 0, [0] * len(series))
    print(answer)


def memoization(series, current, last, largest, memo):
    if memo[current] != 0:
        return memo[current]
    part_of_series = [memoization(series, next, last, series[next], memo)
                      for next in range(current + 1, last + 1) if series[next] > largest]
    if not part_of_series:
        return 0
    memo[current] = 1 + max(part_of_series)
    return memo[current]


solution()
