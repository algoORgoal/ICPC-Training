# name: 계단 오르기
# date: August 10, 2020
# status: solved

import sys
# sys.setrecursionlimit(100000000)


def solution():
    total_stairs = int(sys.stdin.readline())
    stairs = [int(sys.stdin.readline().strip()) for i in range(total_stairs)]

    # memoization
    # answer = memoization(stairs, len(stairs) - 1, -1,
    #                      True, [[0, 0] for _ in stairs])

    # tabulation
    answer = tabulation(stairs)
    print(answer)


def memoization(stages, last, current, can_take_single_step, memo):
    flag = 1 if can_take_single_step else 0
    if memo[current][flag] != 0:
        return memo[current][flag]
    if current == -1:
        if last == 0:
            return stages[last]
        return max(memoization(stages, last, 0, True, memo), memoization(stages, last, 1, True, memo))
    if current == last:
        memo[current][flag] = stages[current]
        return memo[current][flag]
    if current == last - 1:
        memo[current][0] = stages[current] + \
            memoization(stages, last, current + 1, False, memo)
        return memo[current][0]
    # disallow taking a single step
    if current == last - 2:
        memo[current][0] = stages[current] + \
            memoization(stages, last, current + 2, False, memo)
        return memo[current][0]
    if can_take_single_step:
        memo[current][flag] = stages[current] + max(memoization(
            stages, last, current + 1, False, memo), memoization(stages, last, current + 2, True, memo))
        return memo[current][flag]
    memo[current][flag] = stages[current] + \
        memoization(stages, last, current + 2, True, memo)
    return memo[current][flag]


def tabulation(stages):
    stages = [0] + stages
    table = [0] * 3
    len_stages = len(stages) - 1
    table[0] = stages[1]
    if len_stages == 1:
        return table[0]
    table[1] = stages[1] + stages[2]
    if len_stages == 2:
        return table[1]
    table[2] = max(stages[1], stages[2]) + stages[3]
    if len_stages == 3:
        return table[2]

    for index in range(4, len_stages + 1, 3):
        for offset in range(3):
            current = index + offset
            table[offset] = max(table[(offset + 1) % 3] + stages[current], table[offset] +
                                stages[current - 1] + stages[current])
            if current == len_stages:
                return table[(current - 1) % 3]

# define memory space a, b, c
# a updated by a, b
# b updated by b, c
# c updated by c, a
# 4 => 1 2
# 5 => 2 3
# 6 => 3 4


solution()
