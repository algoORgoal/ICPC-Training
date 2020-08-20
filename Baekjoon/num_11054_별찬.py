# name: 가장 긴 바이토닉 수열
# date: August 20, 2020
# status: solved

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
    answer = tabulation(length, series)
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


solution()
