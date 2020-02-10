count = int(input())

series = input().split()

for i in range(len(series), -1):


for i in range(len(series)):
    series[i] = int(series[i])


count_swap = 0
for i in range(len(series)):
    for j in range(i):
        if series[i] < series[j]:
            temp = series[i]
            series[i] = series[j]
            series[j] = temp
            count_swap += 1

print(count_swap)
