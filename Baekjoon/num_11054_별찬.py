# name: 가장 긴 바이토닉 수열
# date: August 20, 2020
# status: solved

# first solution - runs in O(n^2) time
# f, g
# f(n) the length of longest increasing subsequence that ends with n
# g(n) the length of longest decreasing subsequence that starts with n

# ak < an를 만족하는 임의의 k가 있다(1 < k < n). k가 될 수 있는 값의 집합을 A라 하자.
# f(n) = f(max(A))

# an < al을 만족하는 임의의 l이 있다.(n < l) l이 될 수 있는 값의 집합을 B라 하자.
# g(n) = g(max(B))

# h(n) = f(n) + g(n) - 1
# h(n): 최댓값이 an인 바이토닉 수열의 최대 길이
# 자기 자신은 제외하므로 1을 뺀다.


from sys import stdin


def solution():
    length = int(stdin.readline())
    series = [int(string) for string in stdin.readline().strip().split(' ')]
    answer = tabulation2(length, series)
    print(answer)


def tabulation(length, series):
    increasing_table = [0 for _ in range(length)]
    increasing_table[0] = 1
    for i in range(length):
        increasing_table[i] = 1 + max([0] + [increasing_table[j]
                                             for j in range(i) if series[j] < series[i]])

    decreasing_table = [0 for _ in range(length)]
    decreasing_table[length - 1] = 1
    for i in range(length - 1, -1, -1):
        decreasing_table[i] = 1 + max([0] + [decreasing_table[j]
                                             for j in range(i + 1, length) if series[j] < series[i]])

    total_table = [increasing_table[i] + decreasing_table[i] - 1
                   for i in range(length)]
    return max(total_table)

# second solution: runs in O(nlogn) time
# if table 리스트에 있는 최대값 < 현재의 원소: 해당 인덱스의 longest increasing sequence의 길이는 현재까지의 최대 lis 길이 + 1
# else: 오름차순 이진탐색으로 현재의 원소를 table 리스트에 넣는다. 넣은 원소가 n번째 원소일 때, 기존에 있는 n번째 원소는 삭제한다.
# 이진탐색(O(logn) * O(n) = O(nlogn))


def tabulation2(length, series):
    sliced_series = [series[0]]
    table = [[0, 0] for _ in range(length)]
    for i, num in enumerate(series):
        if sliced_series[len(sliced_series) - 1] < num:
            sliced_series.append(num)
            table[i][0] = len(sliced_series)
            continue
        index = binary_search(sliced_series, 0, len(sliced_series) - 1, num)
        sliced_series[index] = num
        table[i][0] = index + 1

    reversed_series = list(reversed(series))
    sliced_series = [reversed_series[0]]

    for i, num in enumerate(reversed_series):
        if sliced_series[len(sliced_series) - 1] < num:
            sliced_series.append(num)
            table[length - i - 1][1] = len(sliced_series)
            continue
        index = binary_search(sliced_series, 0, len(sliced_series) - 1, num)
        sliced_series[index] = num
        table[length - i - 1][1] = index + 1
    sum_table = [sum(table[i]) - 1 for i in range(len(table))]
    return max(sum_table)


def binary_search(li, start, end, target):
    mid = (start + end) // 2
    if start > end:
        return start
    if target < li[mid]:
        return binary_search(li, start, mid - 1, target)
    if target > li[mid]:  # exclude mid when it's smaller than target
        return binary_search(li, mid + 1, end, target)
    if target == li[mid]:
        return mid


solution()

# test cases I've tried
'''
10
1 5 2 1 4 3 4 5 2 1

5
1 1 1 1 1

5
1 2 3 4 5

5
5 4 3 2 1

9
1 2 3 4 5 4 3 2 

3
1 5 2

2
5 2
'''
