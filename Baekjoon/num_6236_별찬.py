# name: 용돈 관리
# date: July 13, 2020
# status: solved

from sys import stdin
from operator import itemgetter


def solution():
    total_days, total_fajomonths = list(map(int, stdin.readline().split(' ')))
    expenses = [int(stdin.readline()) for i in range(total_days)]
    max_expense = expenses[0]
    sum_expense = 0
    for expense in expenses:
        if max_expense < expense:
            max_expense = expense
        sum_expense += expense
    answer = binary_search(max_expense, sum_expense,
                           expenses, total_fajomonths)
    print(answer)


def has_manageable_budget(budget, expenses, fajomonths):
    current_budget = budget
    required_fajomonths = 1
    for expense in expenses:
        if current_budget < expense:
            current_budget = budget
            required_fajomonths += 1
        current_budget -= expense

    if fajomonths < required_fajomonths:
        return False
    return True


def binary_search(low, high, expenses, fajomonths):
    mid = (low + high) // 2

    while high - low > 1:
        if has_manageable_budget(mid, expenses, fajomonths):
            high = mid
            mid = (low + high) // 2
        else:
            low = mid
            mid = (low + high) // 2
    if has_manageable_budget(low, expenses, fajomonths):
        return low
    else:
        return high


solution()
