# name: 가장 긴 증가하는 부분 수열 3
# date: August 21, 2020
# status: solved

from sys import stdin


def solution():
    length = int(stdin.readline())
    series = list(map(int, stdin.readline().strip().split(' ')))
    answer = tabulation(length, series)
    print(answer)


def tabulation(length, series):
    table = [0 for _ in range(length)]
    sliced_series = [series[0]]
    for i, num in enumerate(series):
        if sliced_series[len(sliced_series) - 1] < num:
            sliced_series.append(num)
            table[i] = len(sliced_series)
            continue
        index = binary_search(sliced_series, 0, len(sliced_series) - 1, num)
        sliced_series[index] = num
        table[i] = index + 1
    return max(table)


def binary_search(li, start, end, target):
    mid = (start + end) // 2

    if start > end:  # example: intert k(which is greater than n) into [n]
        return start
    if target < li[mid]:
        return binary_search(li, start, mid - 1, target)
    if target > li[mid]:
        return binary_search(li, mid + 1, end, target)
    # if target == li[mid]
    return mid


solution()
