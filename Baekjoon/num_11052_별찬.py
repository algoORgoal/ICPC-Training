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
    current_price_list = [memoization(card_spent, price_list, price_len, memo) + memoization(cards - card_spent, price_list, price_len, memo)
                          for card_spent in range(1, cards + 1) if cards > card_spent]
    if cards <= price_len:
        current_price_list += [price_list[cards]]
    memo[cards] = max(current_price_list)
    return memo[cards]


solution()
