# name: LCS
# date: July 23, 2020
# status: solved

import sys
sys.setrecursionlimit(100000000)


def solution():
    first_str = sys.stdin.readline().strip()
    second_str = sys.stdin.readline().strip()

    # memoization:
    # answer = memoization(first_str, second_str, len(first_str), len(second_str), [
    #                      [None] * (len(second_str) + 1) for _ in range(len(first_str) + 1)])

    # tabulation:
    answer = tabulation(first_str, second_str)

    print(answer)


def tabulation(first_str, second_str):
    first_len = len(first_str)
    second_len = len(second_str)
    previous_table = [0] * (second_len + 1)
    current_table = [0] * (second_len + 1)
    for row in range(1, first_len + 1):
        for col in range(1, second_len + 1):
            if first_str[row - 1] == second_str[col - 1]:
                current_table[col] = previous_table[col - 1] + 1
                continue
            current_table[col] = max(
                previous_table[col], current_table[col - 1])
        previous_table = current_table
        current_table = [0] * (second_len + 1)
    return previous_table[second_len]


def memoization(first_str, second_str, first_len, second_len, memo):
    if memo[first_len][second_len]:
        return memo[first_len][second_len]
    if not (first_str and second_str):
        memo[first_len][second_len] = 0
        return memo[first_len][second_len]
    first_last_char = first_str[-1]
    second_last_char = second_str[-1]
    if first_last_char == second_last_char:
        memo[first_len][second_len] = 1 + \
            memoization(first_str[:-1], second_str[:-1],
                        first_len - 1, second_len - 1, memo)
        return memo[first_len][second_len]
    memo[first_len][second_len] = max([memoization(first_str[:-1], second_str, first_len - 1, second_len, memo),
                                       memoization(first_str, second_str[:-1], first_len, second_len - 1, memo)])
    return memo[first_len][second_len]


solution()
