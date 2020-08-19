# name: 동전 2
# date: August 19, 2020
# status: solved

from sys import stdin


def solution():
    n, k = list(map(int, stdin.readline().strip().split()))
    coins = [int(stdin.readline().strip()) for _ in range(n)]
    answer = tabulation(coins, k)
    print(answer)


def tabulation(coins, k):
    coins.sort()
    table = [-1 for _ in range(k + 1)]
    # element -1 => can't be created by any coin

    first_coin = coins[0]

    if k < first_coin:
        return -1

    table[first_coin] = 1
    for i in range(2 * first_coin, len(table), first_coin):
        table[i] = table[i - first_coin] + table[first_coin]

    for i in range(1, len(coins)):
        coin = coins[i]
        if k < coin:
            break
        table[coin] = 1
        for j in range(coin + 1, len(table)):
            table[j] = table[j - coin] + \
                table[coin] if table[j - coin] != -1 \
                and (table[j] == -1 or table[j] > table[j-coin] + table[coin]) else table[j]
    return table.pop()


solution()

# test cases I've tried:
# 3 15
# 2
# 5
# 7

# 3 15
# 20
# 30
# 40

# 3 15
# 3
# 5
# 60
