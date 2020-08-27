# name: 동전 바꿔주기
# date: August 19, 2020
# status: solved


from operator import itemgetter
import sys


def solution():
    t = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    coins = [list(map(int, sys.stdin.readline().strip().split(' ')))
             for _ in range(k)]
    # in a tabulation manner
    answer = tabulation(t, k, coins)
    print(answer)


def tabulation(t, k, coins):
    coins.sort(key=itemgetter(0))
    ways_to_spend = [0 for _ in range(t + 1)]
    ways_to_spend[0] = 1
    ways_to_be_added = [0 for _ in range(t + 1)]
    first_coin, count = coins[0]

    for coin, count in coins:
        for i in range(1, count + 1):
            for j in range(coin * i, len(ways_to_be_added)):
                ways_to_be_added[j] += ways_to_spend[j - coin * i]
        for i in range(coin, len(ways_to_spend)):
            ways_to_spend[i] += ways_to_be_added[i]
        ways_to_be_added = [0] * (t + 1)
    return ways_to_spend.pop()


solution()


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

# ways to be added: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3]
# ways to spend: [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 2, 2, 2, 4, 1, 1, 1, 1, 3]


'''
20
4
1 20
2 20
3 20
4 20
'''
