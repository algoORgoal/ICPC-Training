# name: 내려가기
# date: July 22, 2020
# status: solved

import sys


def solution():
    total_lines = int(sys.stdin.readline().strip())
    score_list = [list(map(int, sys.stdin.readline().strip().split(' ')))
                  for i in range(total_lines)]

    maximum, mininum = [tabulation(
        score_list, max), tabulation(score_list, min)]

    print(maximum, mininum)


def start_memoization(score_list, row, select):
    memo = [[None] * 3 for i in range(row)]
    last_row = len(score_list) - 1
    start_row = 0
    start_cols = [0, 1, 2]

    score = select([memoization(
        score_list, last_row, start_row, start_col, memo, select) for start_col in start_cols])
    return score


def tabulation(score_list, select):
    row = len(score_list)
    score_list.reverse()
    table = [None] * 3
    paths = [0, 1, 2]

    for i in range(row):
        if i == 0:
            for path in paths:
                table[path] = score_list[0][path]
            continue

        table = [score_list[i][path] + select([table[prev_path]
                                               for prev_path in find_available_paths(path)]) for path in paths]
    return select([table[path] for path in paths])


def find_available_paths(col):
    if col == 0:
        return [0, 1]
    if col == 1:
        return [0, 1, 2]
    if col == 2:
        return [1, 2]


solution()
