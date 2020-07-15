# name: 병든 나이트
# date: July 15, 2020
# status: solved

from sys import stdin


def solution():
    row, col = list(map(int, stdin.readline().split(' ')))
    answer = count_moves(row, col)
    print(answer)


def count_moves(row, col):
    x = y = 1
    count = 1
    if row == 1 or col == 1 or (row <= 2 and col <= 2):
        # cannot move
        return count
    if row >= 3 and col < 7:
        # move one step right
        step = col - 1
        count += step
        if (count <= 4):
            return count
        return 4
    if row < 3 and col >= 7:
        # move two steps right
        return 4
    if row >= 3 and col >= 7:
        # row doesn't matter. move right until it reaches the end.
        count += 4
        step = col - 7
        count += step
        return count
    # row < 3 and col < 7, can move
    # move two steps right
    step = (col - 1) // 2
    count += step
    return count


solution()
