#   제출일 : 2020-03-23
#   문제 이름: 조합
#   상태: 해결


n, m = list(map(int, input().split()))
# nCm = n-1Cm-1 + n-1Cm
# 100C6 =  99C5 + 99C6
# 99C5 = 98C4 + 98C5
# 99C6 = 98C5 + 98C6
if (m > n/2):
    m = n - m

total = 1
for i in range(m):
    total *= (n - i)

for i in range(m):
    total //= i + 1
total = int(total)
print(total)


# memo = list()

# for i in range(n):
#     temp = list()
#     for j in range(m):
#         temp.append(0)
#     memo.append(temp)


# def solveCombination(memo, n, m):
#     if(memo[n-1][m-1])
