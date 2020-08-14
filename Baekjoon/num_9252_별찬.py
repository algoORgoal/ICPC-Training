# name: LCS 2
# date: July 25, 2020
# status: solved
import sys


def solution():
    first_str = sys.stdin.readline().strip()
    second_str = sys.stdin.readline().strip()

    # memoization:
    # answer = memoization(first_str, second_str, len(first_str), len(second_str), [
    #                      [None] * (len(second_str) + 1) for _ in range(len(first_str) + 1)])

    # tabulation:
    answer1, answer2 = tabulation(first_str, second_str)
    print(answer1)
    print(answer2)


def tabulation(first_str, second_str):
    first_len = len(first_str)
    second_len = len(second_str)
    table = [[0] * (second_len + 1) for _ in range(first_len + 1)]
    for row in range(1, first_len + 1):
        for col in range(1, second_len + 1):
            if first_str[row - 1] == second_str[col - 1]:
                table[row][col] = table[row - 1][col - 1] + 1
                continue
            table[row][col] = max(table[row - 1][col], table[row][col - 1])

    subsequence = ""
    i = first_len
    j = second_len
    while i > 0 and j > 0:
        if first_str[i - 1] == second_str[j - 1]:
            subsequence = first_str[i - 1] + subsequence
            i -= 1
            j -= 1
            continue
        if table[i - 1][j] > table[i][j - 1]:
            i -= 1
            continue
        j -= 1
    return [table[first_len][second_len], subsequence]


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
