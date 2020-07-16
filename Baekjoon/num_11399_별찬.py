# name: ATM
# date: July 16, 2020
# status: solved

from sys import stdin


def solution():
    total_people = int(stdin.readline())
    waiting_time = list(map(int, stdin.readline().split(' ')))
    waiting_time_sorted = sorted(waiting_time)
    answer = determine_total_waiting_time(waiting_time_sorted)
    print(answer)


def determine_total_waiting_time(waiting_time):
    total_waiting_time = 0
    for i in range(len(waiting_time)):
        total_waiting_time += waiting_time[i] * (len(waiting_time) - i)
    return total_waiting_time


solution()
