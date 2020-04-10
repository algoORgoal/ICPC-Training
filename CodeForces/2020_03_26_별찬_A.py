#상태: 해결


def solve(a, b):
    divided = a / b
    if (divided != int(divided)):
        remainder = b * (int(divided) + 1) - a
    else:
        remainder = 0
    return remainder


count = int(input())
for i in range(count):
    a, b = list(map(int, input().split()))
    answer = solve(a, b)
    print(answer)
