# name: 거스름돈
# date: July 25, 2020
# status: unsolved

import sys
sys.setrecursionlimit(100000000)


def solution(n, money):
    money.sort()

    # memoization
    # memo = [[None] * (len(money) + 1) for _ in range(n + 1)]
    # answer = memoization(n, n, len(money), money, memo)

    # tabulation
    answer = tabulation(n, money)

    print(answer)


def tabulation(n, money):
    table = [[0] * (len(money)) for _ in range(n + 1)]
    for i in range(len(money)):
        table[0][i] = 1
    for changes in range(1, n + 1):
        for limit in range(len(money)):
            for currency_index in range(limit + 1):
                if changes >= money[currency_index]:
                    table[changes][limit] += table[changes -
                                                   money[currency_index]][currency_index]
    return table[n][len(money) - 1]


def memoization(changes, limit, limit_index, money, memo):
    if memo[changes][limit_index]:
        return memo[changes][limit_index]
    if changes == 0:
        memo[changes][limit_index] = 1
        return memo[changes][limit_index]
    if limit == 1:
        memo[changes][limit_index] = 1
        return 1
    max_list = []
    for currency_index in range(1, len(money) + 1):
        currency = money[currency_index - 1]
        if changes >= currency and currency <= limit:
            max_list.append(memoization(
                changes - currency, currency, currency_index, money, memo))
        else:
            break

    if max_list:
        memo[changes][limit_index] = sum(max_list)
        return memo[changes][limit_index]
    memo[changes][limit_index] = 0
    return memo[changes][limit_index]


# solution(100000, [i + 1 for i in range(0, 100)])
solution(10, [1, 2, 5])
