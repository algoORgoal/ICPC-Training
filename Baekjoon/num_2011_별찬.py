# name: Alphacode
# date: July 14, 2020
# status: solved

'''
f(25114) = f(5114) + f(25)-f(114)
         = f(114) + f(14) + f(4)
         = f(14) + f(4) + f(14) + f(4)
         = 2 + 1 + 2 + 1 = 6
'''

import sys
sys.setrecursionlimit(100000)


def decode(digits, memo):
    if digits in memo:
        return memo[digits]
    if len(digits) == 1:
        memo[digits] = 1
        return memo[digits]
    if not interpreted_two_ways(digits):
        memo[digits[1:]] = decode(digits[1:], memo)
        return memo[digits[1:]]
    if len(digits) == 2:
        memo[digits] = 2
        return memo[digits]
    memo[digits[1:]] = decode(digits[1:], memo)
    memo[digits[2:]] = decode(digits[2:], memo)
    memo[digits] = memo[digits[1:]] + memo[digits[2:]]
    return memo[digits]


def interpreted_two_ways(digits):
    # if there's 0 that follows two consecutive digits, it's translated in one way no matter what they are.
    # e.g. 110, 2503(In every step of recursion it would return false)
    if len(digits) >= 3 and int(digits[2]) == 0:
        return False
    # 10 and 20 can be translated in only one way because any character can't be mapped with zero.
    if 11 <= int(digits[0:2]) <= 26 and int(digits[0:2]) != 20:
        return True
    return False


def has_zero(two_digits):
    if int(two_digits) == 10 or int(two_digits) == 20:
        return True
    return False


def solution():
    digits = sys.stdin.readline()
    if '\n' in digits:
        digits = digits[:-1]
    valid_digits_list = [str(i) for i in range(10)]

    # 0 alone can't be interpreted
    if digits[0] in '0':
        print(0)
        return

    # 0 is allowed to follow 1 or 2 only
    errors = ['00', '30', '40', '50', '60', '70', '80', '90']
    for error in errors:
        if error in digits:
            print(0)
            return

    # make sure the input consists of numeric characters
    for digit in digits:
        if digit not in valid_digits_list:
            print(0)
            return

    memo = {}
    total_translations = decode(digits, memo)
    print(total_translations % 1000000)


solution()
