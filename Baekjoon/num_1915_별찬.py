# name: 가장 큰 정사각형
# date: August 24, 2020
# status: solved


import sys


def solution():
    n, m = [int(string) for string in sys.stdin.readline().strip().split(' ')]
    square = [[int(char) for char in sys.stdin.readline().strip()]
              for _ in range(n)]
    answer = tabulation(square, n, m)
    print(answer)


def tabulation(square, n, m):
    table = [0] * m
    max_len = 0
    for i in range(n):
        row = square[i]
        present = 0
        for j in range(m):
            if row[j] == 0:
                table[j] = 0
            table[j] += row[j]
            if table[j] > max_len:
                present += 1
                if present > max_len:
                    max_len += 1
                    present = 0
            else:
                present = 0
    return max_len * max_len


solution()


'''
10 10
0000001111
0000001111
0000001111
1111101111
1111101111
1111101111
1111101111
1111101111
1111101111
1111101111

3 11
00000000111
11000000111
11000000111

3 9
110000111
110000111
000000111

6 6
000111
111111
111111
111000

5 13
1110000011111
1110000111111
1110000111111
0000000111111
0000000111111

4 4
1100
1111
1111
0011

6 6
000111
111111
111111
111111
111111
011111

2 10 
11000000011
11000000011
'''
