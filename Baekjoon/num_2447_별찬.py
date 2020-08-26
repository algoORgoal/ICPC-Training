# name: 별 찍기 - 10
# date: August 25, 2020
# status: solved

from sys import stdin


def solution():
    n = int(stdin.readline().strip())
    table = [[0] for _ in range(n)]
    draw(table, n)
    for row in table:
        print(row)


def draw(table, n):
    table[0] = "***"
    table[1] = "* *"
    table[2] = "***"
    if n == 3:
        return
    current = 9
    while current <= n:
        previous = current // 3
        mid_start = previous
        mid_end = 2 * mid_start
        end = mid_end + previous
        for row in range(mid_start, mid_end):
            table[row] = table[row - previous]
            table[row] += " " * previous
            table[row] += table[row - previous]
        for row in range(0, previous):
            table[row] *= 3
        for row in range(mid_end, end):
            table[row] = table[row - 2 * previous]
        current *= 3


solution()
