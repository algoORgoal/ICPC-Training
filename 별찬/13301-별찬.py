
'''
    날짜: 2020-01-17
    언어: python
    문제: 2016년도 초등부 문제 2(백준 13301번)
    작성자: 김별찬
'''




num = int(input())
temp = 1
i = 0
tile_length1 = 1
tile_length2 = 1
if(num == 1):
    width = tile_length1
    length = tile_length2
else:
    while(i < num - 1):
        if i%2 == 0:
            tile_length1 += tile_length2
        else:
            tile_length2 += tile_length1
        i += 1
    width = tile_length1
    length = tile_length2
round = 2*(width+length)
print(round)