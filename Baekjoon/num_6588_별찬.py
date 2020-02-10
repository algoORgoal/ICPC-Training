'''
    날짜: 2020-01-30
    언어: python
    문제: 골드바흐의 추측(백준 문제번호 6588)
    작성자: 김별찬
    상태: 시간초과
'''

import math


def get_cases_from_user():
    cases = list()
    cases.append(int(input()))
    while (cases[len(cases) - 1] != 0):
        cases.append(int(input()))
    cases.pop()  # get rid of 0 at the end of list
    return cases


def find_max(numbers):
    max = numbers[0]
    for i in range(1, len(numbers)):
        if max < numbers[i]:
            max = numbers[i]
    return max


def create_odd_list(max):
    # create a list of odd numbers, ranging from 1 to the number of test case
    odd_list = list()
    for i in range(3, max, 2):
        odd_list.append(i)
    return odd_list


def find_primes(numbers):
    i = 0
    while i < len(numbers):
        for j in range(i):
            if numbers[j] > int(math.sqrt(numbers[i])):
                break
            elif numbers[i] % numbers[j] == 0:
                numbers.pop(i)
                i -= 1  # check same index when the element is removed from the list
                break
        i += 1
    return numbers


def get_result(cases, prime_list):
    equation = ""
    for case in cases:
        for prime in prime_list:
            '''
                let n = a + b, a <= b
                    1. a = b: a = b = n/2
                    2. a < b: a < n/2, b > n/2
                    therefore we can make sure of the answer by checking the condition from start to n/2
            '''
            if prime > case / 2:
                equation += "Goldbach's conjecture is wrong."
                break
            else:
                if case - prime in prime_list:
                    equation += get_equation(prime, case - prime, case)
                    break
        equation += '\n'
    return equation


def get_equation(left_side, right_side, sum):
    return str(sum) + ' = ' + str(left_side) + \
        ' + ' + str(right_side)


cases = list()
max = 0
odd_list = list()
prime_list = list()
result = ""

cases = get_cases_from_user()
max = find_max(cases)
odd_list = create_odd_list(max)
# let the list except the power of prime numbers(3, 5, 7, 11, ...)
prime_list = find_primes(odd_list)
result = get_result(cases, prime_list)
print(result)


'''
현재의 방법
입력 중에 가장 큰 숫자를 n이라 하자. 1부터 n까지의 모든 소수를 찾는다. 그 뒤에 소수 쌍이 리스트 안에 있는지 찾는다.

대안
입력 중에 가장 큰 숫자를 n이라 하자. 1부터 n의 제곱근까지의 모든 소수를 찾는다. 작은 소수 순서대로 n - 소수가 소수인지 확인한다. 만약 n - 소수가 소수이면 리스트에 추가한다.
'''
