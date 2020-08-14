# name: 전깃줄
# date: July 25, 2020
# status: solved


import sys
from operator import itemgetter

sys.setrecursionlimit(100000000)


def solution():
    total_line = int(sys.stdin.readline().strip())
    poles = [list(map(int, sys.stdin.readline().strip().split(' ')))
             for _ in range(total_line)]
    # poles = [[i, 501 - i] for i in range(1, 251)]
    sorted_poles = sorted(poles, key=itemgetter(0))
    answer = total_line - memoization(sorted_poles, 0, {})
    print(answer)


def memoization(poles, largest, memo):
    if len(poles) == 0:
        return 0
    if poles[0][0] in memo:
        return memo[poles[0][0]]
    next_poles = [memoization(poles[index + 1:], poles[index][1], memo)
                  for index in range(len(poles)) if poles[index][1] > largest]
    if not next_poles:
        return 0
    memo[poles[0][0]] = 1 + max(next_poles)
    return memo[poles[0][0]]


solution()
