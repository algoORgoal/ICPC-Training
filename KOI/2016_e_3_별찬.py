'''
    날짜: 2020-01-18
    언어: python
    문제: 리조트-2016년도 초등부 문제 3(백준 13302번)
    작성자: 김별찬
    incomplete
'''


duration, count_days_off = input().split()
duration = int(duration)
count_days_off = int(count_days_off)
days_off = []

days_off.append(input().split())

ways = 0
price = 0
coupon = 0
current = 1

'''
    해당 날짜에 리조트를 갈 수 있을 때
    :하루 이용권, 3일 이용권, 5일 이용권으로 나눠서 계산
    아니면
    :다음 날짜로 이동
'''


def find_ways(current, ways, days_off, price, coupon):
    if current > duration:
        return price
    elif current not in days_off:  # 쉬는 날이 아닐 경우
        current1 = current + 1
        ways1 = ways.append(1)

        current2 = current + 3
        ways2 = ways2.append(3)

        current3 = current + 5
        ways3 = ways.append(5)

        price1 = 10000

        find_ways(current1, ways, days_off, price + 10000, coupon)
        find_ways(current2, ways2, days_off, price + 25000, coupon + 1)
        find_ways(current3, ways3, days_off, price + 37000, coupon + 2)
        if (coupon >= 3):
            find_ways(current + 1, ways, days_off, price, coupon - 3)
    else:

    return price
