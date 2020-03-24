'''
문제 이름: 곱셈
상태: 정답
날짜: 2020-03-24
반복되는 수열이 있다고 가정하고 찾음: 시간 초과
(A * B) % C = (A % C * B % C) % C 적용: 시간 초과
다음 링크의 방법 적용: 맞았습니다!
https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-multiplication
A^4 % C = (A^2 % C * A^2 % C) % C
A^20 % C = (A^4 % C * A^16 % C) % C
'''

line = list(map(int, input().split()))
num = line[0]
power = line[1]
divider = line[2]

# 자연수를 받아서 이진수 문자열로 반환


def decimalToBinary(decimal):
    if (decimal == 0):
        return ""
    else:
        return decimalToBinary(decimal // 2) + str(decimal % 2)


power_binary_str = decimalToBinary(power)
power_binary_len = len(power_binary_str)

series = []
remainder = num % divider  # A % C
series.append(remainder)  # A % C를 리스트에 추가

remainder_power = remainder

for i in range(1, power_binary_len):
    # (A^n % C * A^n % C) = A^(2n) % C
    # B를 이진수로 표현하는데 필요한 비트의 개수만큼 추가
    # 예시:
    # (A%C * A%C) % C = A^2 % C
    # (A^2 % C * A^2 % C) % C = A^4 % C

    remainder_power *= remainder_power
    remainder_power %= divider
    series.append(remainder_power)

answer = 1
for i in power_binary_str:
    # series에 들어있는 remainder의 순서: 작은 지수의 나머지 순서대로 쌓임
    # power_binary_str에 들어있는 이진수: 큰 값 순서대로 접근
    # 따라서 power_binary_str에 있는 숫자를 접근할 때마다 series에 있는 숫자는 끝에서부터 접근
    # 예시: A^20 % C = (A^16 % C * A^4 % C ) % C (지수가 8, 2, 1일 경우는 power_binary_str에서 0에 해당함
    # => series에서 지수대로 쌓이므로 pop()을 통해 제거)

    if int(i) == 1:
        answer *= series.pop()
    else:
        series.pop()
answer %= divider
print(answer)
