'''
날짜: 2020-02-12
상태: 해결
'''


A, P = input().split()
A = int(A)
P = int(P)


powers = list()

for i in range(0, 10):
    powers.append(i ** P)
# print(powers)

D = list()


D.append(A)
temp = D[0]

while True:
    total = 0
    while temp > 0:
        index = temp % 10
        temp //= 10
        # print(index)
        total += powers[index]
    # print(total)
    if total in D:
        # print("total은 ", total, "입니다")
        temp = total
        break
    else:
        D.append(total)
        temp = D[len(D) - 1]

count = 0

for i in D:
    if temp != i:
        count += 1
    else:
        break
print(count)
