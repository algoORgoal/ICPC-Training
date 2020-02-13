
'''
날짜: 2020-02-10
'''
'''
min, max = input().split()

min = int(min)
max = int(max)
print(min, max)


square_divided = list()


for i in range(2, max):
    if i * i > max:
        break
    square_divided.append(i*i)
print(square_divided)

count = 0
for i in range(min, max + 1):
    is_divided = False  # True when i is divided by any number in square_divided
    for j in square_divided:
        if i % j == 0:
            is_divided = True
            break
    if not is_divided:
        # print(i)
        count += 1
print(count)
'''

min, max = input().split()

min = int(min)
max = int(max)

square_divided = list()

for i in range(max):
    square_divided.append(False)


for i in range(2, max):
    j = 1
    while i ** 2 * j <= max:
        square_divided[i**2*j - 1] = True
        j += 1

count_square_divided = 0
for i in range(len(square_divided)):
    if not square_divided[i]:
        count_square_divided += 1

print(count_square_divided)


# 1 000 000 000 000 1 000 000 000 000
# 999999000000 1000000000000
# 1000000 2000000
# 99000000 100000000
# find numbers that are not divided by square numbers
# find numbers that can be divided by square numbers
