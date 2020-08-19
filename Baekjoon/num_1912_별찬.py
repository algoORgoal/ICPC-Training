# name: 연속합
# date: July 18, 2020
# status: solved

from sys import stdin

# n번째 항을 포함하면서 n번째 항에 왼쪽으로 연속된 수열의 최대값을 f(n)이라 하자.
# f(n) = an +  f(n - 1) if f(n - 1) > 0 else an
# answer = max(f(1), f(2), ... , f(n))


def solution():
    total_integer = int(stdin.readline())
    integers = [int(str) for str in stdin.readline().strip().split()]

    answer = tabulation(integers)
    print(answer)


def tabulation(integers):
    table = [0 for _ in integers]
    table[0] = integers[0]
    for i in range(1, len(table)):
        if table[i - 1] > 0:
            table[i] = integers[i] + table[i - 1]
            continue
        table[i] = integers[i]
    return max(table)


solution()

# test cases I've tried:
# 9
# -10 200 -10 200 -10 200 -10 1 -400 300
# 8
# -700 100 -80 50 -70 100 -10 80
# 8
# 80 -10 50 -70 100 -10 80
