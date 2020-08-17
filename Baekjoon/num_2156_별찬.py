# name: 포도주 시식
# date: August 17, 2020
# status: solveda

from sys import stdin

# n번째까지 포도주가 있을 때 마실 수 있는 양을 최대로 만드는 경우의 수
# 1. n-2번째에 마시고 난 다음
# 2. n-3번째를 마시고, n-1번째를 마시고 난 다음
# 3. n번째를 마시지 않는 경우


def solution():
    lines = int(stdin.readline())
    wine_series = [0] + [int(stdin.readline().strip()) for _ in range(lines)]
    answer = tabultation(wine_series)
    print(answer)


def tabultation(series):
    table = [0] * 3
    series_len = len(series) - 1
    table[1] = series[1]
    if series_len == 1:
        return table[1]
    table[2] = series[1] + series[2]
    if series_len == 2:
        return table[2]

    for i in range(3, len(series)):
        next_sum = max(table[0] + series[i - 1] + series[i], table[1] + series[i],
                       table[2])
        table = [table[1], table[2], next_sum]
    return table.pop()


solution()
