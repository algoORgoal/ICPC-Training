# name: 가장 큰 증가 부분 수열
# date: August 19, 2020
# status: solved

from sys import stdin

# 첫번째 항부터 n번째 항까지의 부분 수열 중에서 합이 가장 큰 것을 f(n)라 하자.
# ak < an 을 만족하는 k 값의 집합을 b1, ..., bm이라 하자.  (1 <= k <= n - 1)
# f(n) = an + max(f(b1), ..., f(bm))
# k 값이 존재하지 않는다면, f(n) = an


def solution():
    N = int(stdin.readline())
    series = [int(string) for string in stdin.readline().strip().split()]
    answer = tabulation(series)
    print(answer)


def tabulation(series):
    table = [0 for _ in series]
    table[0] = series[0]
    for i in range(1, len(table)):
        table[i] = series[i] + max([0] + [table[j]
                                          for j in range(i) if series[j] < series[i]])
    return max(table)


solution()
