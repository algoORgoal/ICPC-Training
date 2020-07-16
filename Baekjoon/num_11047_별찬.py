# name: 동전 0
# date: July 16, 2020
# status: solved


from sys import stdin


def solution():
    total_coins, target_value = list(map(int, stdin.readline().split(' ')))
    coin_iterator = reversed(list(map(int, [stdin.readline().strip()
                                            for i in range(total_coins)])))
    answer = determine_needed_coins(coin_iterator, target_value)
    print(answer)


def determine_needed_coins(coin_iterator, target_value):
    count_needed_coins = 0
    for coin in coin_iterator:
        if target_value == 0:
            return count_needed_coins
        count_coin = target_value // coin
        target_value %= coin
        count_needed_coins += count_coin
    return count_needed_coins


solution()
