# name: 가장 긴 증가하는 부분 수열 5
# date: August 21, 2020
# status: unsolved

from sys import stdin

# 출현한 원소가 들어갈 인덱스가 k => 다음에 k+1, k+2,..., n까지 순차적으로 바뀔 때 업데이트


def solution():
    length = int(stdin.readline())
    series = [int(string) for string in stdin.readline().strip().split()]
    max_length, expected_series = tabulation(length, series)
    print(max_length)
    print(*expected_series)


def tabulation(length, series):
    table = [0 for _ in range(length)]
    sliced_series = [series[0]]
    original_series = [series[0]]
    start = 0
    current = 0
    for i, num in enumerate(series):
        if sliced_series[len(sliced_series) - 1] < num:
            sliced_series.append(num)
            original_series.append(num)
            table[i] = len(sliced_series)
            continue
        index = binary_search(sliced_series, 0, len(sliced_series) - 1, num)
        sliced_series[index] = num

        if index == current + 1:
            current += 1
        else:
            start = index
            current = start
        if current == len(sliced_series) - 1:
            copy(sliced_series, original_series, start)
            # start = -1
            # current = start
        table[i] = index + 1
    return max(table), original_series


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


def copy(new, original, start):
    for i in range(start, len(new)):
        original[i] = new[i]


solution()

# test cases I've tried
'''
2
2 1

1
1

9
1 2 3 4 5 4 3 2 1

5
1 2 3 4 5

5
5 4 3 2 1

16
1 2 5 4 6 7 5 6 7 8 9 2 3 4 5 6

15
1 5 10 15 20 25 2 3 4 5 6 7 8 9 10

11
1 5 10 15 20 25 2 3 4 5 

8
1 2 5 3 4 7 9 6

10
1 2 6 4 7 9 6 5 10

11
1 2 6 4 7 9 6 5 3 10 4

6
1 2 4 3 10 5
'''
