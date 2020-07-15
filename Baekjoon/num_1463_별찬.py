# name: 1로 만들기
# date: July 15, 2020
# status: solved

from sys import stdin


def solution():
    n = int(stdin.readline())
    answer = make_n_zero(n)
    print(answer)


def make_n_zero(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    maximum = 1000000
    table = [maximum for i in range(n + 1)]
    table[2] = 1
    table[3] = 1
    for i in range(2, n + 1):
        if i + 1 <= n and table[i+1] > table[i] + 1:
            table[i + 1] = table[i] + 1
        if 2 * i <= n and table[2*i] > table[i] + 1:
            table[2 * i] = table[i] + 1
        if 3 * i <= n and table[3*i] > table[i] + 1:
            table[3 * i] = table[i] + 1
    return table[n]


solution()
