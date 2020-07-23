# name: 카드 구매하기
# date: July 22, 2020
# status: solved

import sys
sys.setrecursionlimit(10000000)


def solution():
    total_cards = int(sys.stdin.readline().strip())
    price_list = [0] + [int(char)
                        for char in sys.stdin.readline().strip().split(' ')]
    answer = memoization(total_cards, price_list, len(price_list) - 1, {})
    print(answer)


def tabulation(total_cards, price_list):
    len_price_list = len(price_list) - 1
    table = [0] * (total_cards + 1)
    for index in range(1, total_cards + 1):
        if index <= len_price_list:
            table[index] = price_list[index]
        for offset in range(1, index // 2 + 1):
            if table[index] < table[offset] + table[index - offset]:
                table[index] = table[index -
                                     offset] + table[offset]
    return table[total_cards]


def memoization(cards, price_list, price_len, memo):
    if cards in memo:
        return memo[cards]
    current_price = 0
    for card_spent in range(1, cards // 2 + 1):
        memo[card_spent] = memoization(
            card_spent, price_list, price_len, memo)
        memo[cards - card_spent] = memoization(
            cards - card_spent, price_list, price_len, memo)

        if current_price < memo[card_spent] + memo[cards - card_spent]:
            current_price = memo[card_spent] + memo[cards - card_spent]
    current_price = price_list[cards] if cards <= price_len and current_price < price_list[
        cards] else current_price
    memo[cards] = current_price
    return memo[cards]


solution()
