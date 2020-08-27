# name: 별 찍기 - 18
# date: August 27, 2020
# status: solved

import sys
sys.setrecursionlimit(1000000)


def solution():
    n = int(sys.stdin.readline())
    answer = nest(draw(n), n)
    print(answer)


def draw(n):
    if n == 1:
        return ['*']
    previous = draw(n - 1)

    if n % 2:  # odd
        first = previous[0]
        bottom = [first * 2 + "***"]
        top = list(reversed(['*' + ' ' * len(string[1:-1]) + '*' if string !=
                             '*' else '*' for string in previous]))
        mid = ['*' + ' ' * (2 * i) +
               string + ' ' * (2 * i) + '*' for i, string in enumerate(previous)]
        return top + mid + bottom

    last = previous[len(previous) - 1]
    top = [last * 2 + "***"]
    bottom = list(reversed(['*' + ' ' * len(string[1:-1]) + '*' if string !=
                            '*' else '*' for string in previous]))
    mid = ['*' + ' ' * (2 * (len(previous) - 1 - i))
           + string + ' ' * (2 * (len(previous) - 1 - i)) + '*' for i, string in enumerate(previous)]
    return top + mid + bottom


def nest(li, n):
    if n % 2:  # odd
        for i, row in enumerate(li):
            li[i] = " " * (len(li) - 1 - i) + row
    else:  # even
        for i, row in enumerate(li):
            li[i] = " " * i + row
    return '\n'.join(li)


solution()
