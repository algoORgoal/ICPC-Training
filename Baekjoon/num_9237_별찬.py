# name: Planting trees
# date: August 10, 2020
# status: solved

from sys import stdin


def solution():
    total_plants = int(stdin.readline())
    days_to_plant = list(map(int, stdin.readline().strip().split(' ')))
    days_to_plant.sort()
    days_to_plant.reverse()

    maximal_days = 0
    for index in range(len(days_to_plant)):
        if maximal_days < days_to_plant[index] + index + 1:
            maximal_days = days_to_plant[index] + index + 1
    maximal_days += 1
    print(maximal_days)


solution()
