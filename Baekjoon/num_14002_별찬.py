# name: 가장 긴 증가하는 부분 수열 4
# date: August 14, 2020
# status: solved

import sys
sys.setrecursionlimit(100000000)


def solution():
    total_series = int(sys.stdin.readline())
    series = list(map(int, sys.stdin.readline().strip().split(' ')))
    memo = [0] * len(series)
    size = memoization(series, -1, len(series) - 1,
                       0, memo)
    part_of_series = []
    current = 0

    if size == 1:
        part_of_series.append(series[0])
    else:
        for i in range(0, len(memo)):
            # second time current's got zero: end of series
            if current == 0 and part_of_series:
                break
            # add element to part_of_series for the first time
            if current == 0 and memo[i] == size - 1:
                current = memo[i]
                part_of_series.append(series[i])
                continue
            if current - 1 == memo[i]:
                current -= 1
                part_of_series.append(series[i])

    print(size)
    for num in part_of_series:
        print(num, end=" ")


def memoization(series, current, last, largest, memo):
    if memo[current] != 0:
        return memo[current]
    part_of_series = [memoization(series, next, last, series[next], memo)
                      for next in range(current + 1, last + 1) if series[next] > largest]
    if not part_of_series:
        return 0
    if current == -1:
        return 1 + max(part_of_series)
    memo[current] = 1 + max(part_of_series)

    return memo[current]


solution()
