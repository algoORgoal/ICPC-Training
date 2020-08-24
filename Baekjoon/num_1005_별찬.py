# name: ACM Craft
# date: August 24, 2020
# status: solved

import sys
sys.setrecursionlimit(100000000)


def solution():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = [int(string)
                for string in sys.stdin.readline().strip().split(' ')]
        delays = [0] + [int(string)
                        for string in sys.stdin.readline().strip().split(' ')]
        connection = [[int(string)
                       for string in sys.stdin.readline().strip().split(' ')] for _ in range(k)]
        next_previous = {}
        for previous, next in connection:
            if next in next_previous:
                next_previous[next].append(previous)
            else:
                next_previous[next] = [previous]
        corresponding_index = int(sys.stdin.readline())
        memo = [-1 for _ in range(n + 1)]
        answer = memoization(delays, next_previous, memo, corresponding_index)
        print(answer)


def memoization(delays, next_previous, memo, current):
    if memo[current] != -1:
        return memo[current]
    if current not in next_previous:
        memo[current] = delays[current]
        return memo[current]
    previous = next_previous[current]
    memo[current] = delays[current] + \
        max([memoization(delays, next_previous, memo, groundwork)
             for groundwork in previous])
    return memo[current]


solution()

# test cases I've tried
'''
1
2 1
10 100
1 2
1

1
2 1
10 100
1 2
2
'''
