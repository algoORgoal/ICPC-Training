# name: Card Game
# date: August 27, 2020
# status: unsolved

import sys
sys.setrecursionlimit(100000000)


def solution():
    count_test_cases = int(sys.stdin.readline())
    for _ in range(count_test_cases):
        count_cards = int(sys.stdin.readline())
        cards = [int(string)
                 for string in sys.stdin.readline().strip().split(' ')]
        print(count_cards, cards)
        memoization(cards)


def memoization(cards):


solution()
