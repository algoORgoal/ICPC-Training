# name: a^b
# date: July 13, 2020
# status: solved

from sys import stdin


def solution():
    arr = stdin.readline().split(' ')
    base, exponent = [str(arr[0]), int(arr[1])]
    extended_base, power_to_extend = extend_to_int(base)
    extended_answer = exponential(extended_base, exponent)
    answer = place_floating_point(extended_answer, exponent, power_to_extend)
    print(answer)


def extend_to_int(str_num):
    power_to_extend = 0
    num = 0
    if float(str_num) < 1:
        power_to_extend = len(str_num) - 2
        num = int(str_num[2:])
    else:  # larger than 1
        point_index = str_num.index('.')
        power_to_extend = len(str_num[point_index + 1:])
        num = int(str_num[:point_index] + str_num[point_index + 1:])
    return [num, power_to_extend]


def place_floating_point(extended, exponent, power_to_extend):
    power_to_ten = exponent * power_to_extend
    str_extended = str(extended)
    power_to_reduce = len(str_extended) - power_to_ten
    if (power_to_reduce > 0):
        return str_extended[:power_to_reduce] + '.' + str_extended[power_to_reduce:]
    if (power_to_reduce == 0):
        return '0.' + str_extended
    if (power_to_reduce < 0):
        return '0.' + '0' * (abs(power_to_reduce)) + str_extended


def exponential(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    return exponential(base*base, exponent//2) * exponential(base, exponent % 2)


solution()
