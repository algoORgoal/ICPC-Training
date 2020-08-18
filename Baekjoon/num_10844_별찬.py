# name: 쉬운 계단 수
# date: August 18, 2020
# status: solved

from sys import stdin


def solution():
    num = int(stdin.readline().strip())
    answer = tabulation(num)
    print(answer % 1000000000)


def tabulation(num):
    table = [[0] * 10 for _ in range(num)]
    for i in range(len(table[0])):
        table[0][i] = 1
    for i in range(1, len(table)):
        for j in range(0, len(table[i])):
            if j == 0:
                table[i][j] = table[i - 1][1]
                continue
            if j == 9:
                table[i][j] = table[i - 1][8]
                continue
            table[i][j] = table[i - 1][j - 1] + table[i - 1][j + 1]
    return sum(table[len(table) - 1][1:])


solution()
