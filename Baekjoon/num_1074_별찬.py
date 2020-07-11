# name: Z
# datae: July 11, 2020
# status: solved

from sys import stdin


def solution():
    size_power_two, target_y, target_x = list(
        map(int, stdin.readline().split(' ')))
    length = 2 ** size_power_two
    answer = z_search(length, 0, 0, target_x, target_y, 0)
    print(answer)


def z_search(length, x, y, target_x, target_y, index):
    if length == 1:
        return index
    half = length // 2
    # fourth quadrant
    if (target_x >= x + half and target_y >= y + half):
        return z_search(half, x + half, y + half, target_x,
                        target_y, index + 3 * half ** 2)
    # third quadrant
    elif (target_y >= y + half):
        return z_search(half, x, y + half, target_x,
                        target_y, index + 2 * half ** 2)
    # second quadrant
    elif (target_x >= x + half):
        return z_search(half, x + half, y, target_x, target_y, index + half ** 2)
    # first quadrant
    else:
        return z_search(half, x, y, target_x, target_y, index)


solution()
