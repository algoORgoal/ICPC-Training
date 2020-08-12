# name: 이친수
# date: August 12, 2020
# status: solved

# f(n) = f(n-1) + f(n-2)
# 0 채우기: f(n-1)가지의 숫자에 0을 채운다.
# 1 채우기: 뒷 자리가 항상 0으로 끝나야 한다. 따라서 f(n-2)개의 경우의 수

from sys import stdin


def solution():
    total_digit = int(stdin.readline().strip())
    answer = tablution(total_digit)
    print(answer)


def tablution(total_digit):
    a, b = 0, 1
    if total_digit == 0:
        return a
    if total_digit == 1:
        return b
    for i in range(2, total_digit + 1, 2):
        a = a + b
        if i == total_digit:
            return a
        b = a + b
        if i + 1 == total_digit:
            return b


solution()
