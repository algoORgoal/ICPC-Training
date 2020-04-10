#상태: 미완성

count = int(input())


def solve(n, k):
    added = 2
    i = 1
    while True:
        if (i * (i + 1) / 2 >= k):
            print(i)
            break
        i += added
        added += 1


for i in range(count):
    a, b = list(map(int, input().split()))
    solve(a, b)
