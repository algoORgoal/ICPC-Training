# name: 별 찍기 - 11
# date: August 27, 2020
# status: solved

from sys import stdin


def solution():
    n = int(stdin.readline())
    answer = nest(draw(n), n)
    print(answer)


def draw(n):
    if n == 3:
        return ['*', '* *', '*****']
    previous = draw(n // 2)
    white_spaces = [''.join([char for char in row.replace('*', ' ')])
                    for row in reversed(previous)]
    group = [''.join(sequences)
             for sequences in list(zip(previous, white_spaces, previous))]
    current = previous + group
    return current


def nest(li, n):
    last = li.pop()
    nesting_white_spaces = [' ' * i for i in range(n - 1, 0, -1)]
    nested_li = [''.join(sequences)
                 for sequences in list(zip(nesting_white_spaces, li, nesting_white_spaces))] + [last]
    return '\n'.join(nested_li)


solution()
