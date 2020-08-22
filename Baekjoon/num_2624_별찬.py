# name: 동전 바꿔주기
# date: August 19, 2020
# status: unsolved


from sys import stdin
from operator import itemgetter


def solution():
    t = int(stdin.readline())
    k = int(stdin.readline())
    coins = [list(map(int, stdin.readline().strip().split(' ')))
             for _ in range(k)]
    coins.sort()
    coins.reverse()
    print(coins)
    # in a tabulation manner
    # tabulation(t, k, coins)

    answer = memoization(t, k, coins, [])
    print(answer)


def memoization(t, k, coins, memo):
    if t == 0:
        return 1
    exchanges = []
    for i in range(len(coins)):
        coin, count = coins[i]
        if t - coin >= 0 and count > 0:
            exchanges.append(memoization(
                t - coin, k, [[coin, count - 1]] + coins[i + 1:], memo))
    if not exchanges:
        return 0
    return sum(exchanges)


def tabulation(t, k, coins):
    coins.sort(key=itemgetter(0))
    spent_coins = [[0 for _ in coins] for _ in range(t + 1)]
    print(spent_coins)
    print(coins)
    first_coin, count = coins[0]
    if t < first_coin:
        return 0

    table = [0 for _ in range(t + 1)]
    table[first_coin] = 1
    spent_coins[first_coin][0] = 1
    for i in range(2 * first_coin, len(table), first_coin):
        table[i] = 1
        spent_coins[i][0] = spent_coins[i - first_coin][0] + 1
        if spent_coins[i][0] == count:
            break

    print(table)
    for i in range(1, len(coins)):
        coin, count = coins[i]
        if t < coin:  # money amount t can't be represented by coins showing up from now on
            break
        table[coin] += 1
        spent_coins[coin][i] = 1
        limited = False
        for j in range(coin + 1, t + 1):
            # if count <= 0:
            #     table[j] += table[j - coin] - 1
            #     continue
            if limited:
                table[j] = table[j - coin] - 1
            table[j] += table[j - coin]
            spent_coins[j][i] = spent_coins[j - coin][i] + 1
            if spent_coins[j][i] == count:
                limited = True
        print(spent_coins)
        print(table)
    print(table)


solution()

# test cases I've tried:
# 10
# 3
# 1 10
# 2 5
# 5 2

# 100
# 5
# 100 1
# 200 2
# 300 3
# 400 4
# 500 5

# 10
# 3
# 2 5
# 5 2
# 7 2
