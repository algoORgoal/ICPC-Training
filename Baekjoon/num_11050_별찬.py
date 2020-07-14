# name: 이항계수1
# date: July 14, 2020
# status: solved

from sys import stdin


def solution():
    n, k = list(map(int, stdin.readline().split(' ')))
    answer = combination(n, k)
    print(answer)


def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


solution()
