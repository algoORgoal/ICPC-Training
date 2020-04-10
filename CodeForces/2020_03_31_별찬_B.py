



# import math


# def primes(n):
#     composites = []
#     prime = [2]
#     i = 3

#     while (i <= 1000):
#         if i not in composites:
#             prime.append(i)
#             j = i
#             while (j <= n / i):
#                 composites.append(i * j)
#                 j += 1
#         i += 2

#     return prime


# def eratosthesnes(n):
#     required_primes = primes(int(math.sqrt(n)))
#     result = [2]
#     i = 3

#     if (n == 1):
#         return []

#     while (i <= n):
#         for prime in required_primes:
#             if i != prime and i % prime == 0:
#                 break
#         else:
#             result.append(i)
#         i += 2

#     return result


# def prime_factorize(num):
#     possible_prime = eratosthesnes(int(math.sqrt(num)))

#     for divisor in possible_prime:
#         if num % divisor == 0:
#             temp = int(num / divisor)
#             return str(divisor) + ',' + str(prime_factorize(temp))
#     return str(num)


# def solve(test):
#     print(test)


countTest = int(input())
print(countTest)
for i in range(countTest):
    countNum = int(input())
    test = list(map(int, input().split()))
    solve(test)

'''
    set으로 배열 만들어
    첫번째 set: 2의 배수의 입력값들의 모임, 3 '' , 5 '' ,
    두번째 set:

    1000, 5, 36
    100 입력시 소인수분해 2 * 5, object 
    input.value -> 100
    첫번째 set을 채움 => 사이즈 기준으로 정렬
    해당하는 숫자들이 있으면 같은 색깔로(object의 color 설정)
    500을 삭제해주면서 5있는데서 발견 -> 2 있는데서 삭제
    재정렬 => 9번
    
'''
