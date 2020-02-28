'''
날짜: 2020-02-28
상태: 완성(정답)
문제 이름: 동전 1
'''


n, k = input().split()
n = int(n)
k = int(k)
arr = []
answer = []
for i in range(n):
    arr.append(int(input()))


for i in range(k + 1):
    answer.append(0)

# print(answer)


for i in range(len(answer)):
    # print(i)
    unit = i % arr[0]
    if (unit == 0):
        answer[i] += 1
# print(answer)


for i in range(1, n):
    # print(arr[i])
    for j in range(arr[i], len(answer)):
        answer[j] = answer[j] + answer[j - arr[i]]
    # print(answer)
print(answer[len(answer) - 1])
