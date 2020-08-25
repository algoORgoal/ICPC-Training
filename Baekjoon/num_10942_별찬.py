# name: 팰린드롬?
# date: August 25, 2020
# status: solved

from sys import stdin


def solution():
    length = int(stdin.readline())
    series = [int(string) for string in stdin.readline().strip().split(' ')]
    count_questions = int(stdin.readline())
    questions = [[int(string) - 1 for string in stdin.readline(
    ).strip().split(' ')] for _ in range(count_questions)]
    answers = tabulation(length, series, questions)
    for answer in answers:
        print(answer)


def tabulation(length, series, questions):
    odd_table = [[0] * (i + 1) if i < (length // 2) else [0]
                 * (length - i) for i in range(0, length)]
    even_table = [[0] * (i + 1) if i < (length // 2) else [0]
                  * (length - i - 1) for i in range(0, length - 1)]

    for i in range(len(odd_table)):
        odd_table[i][0] = 1

    for i in range(len(odd_table)):
        for j in range(1, len(odd_table[i])):
            if odd_table[i][j - 1] == 0:
                break
            if series[i - j] == series[i + j]:
                odd_table[i][j] = 1

    for i in range(len(even_table)):
        for j in range(len(even_table[i])):
            if even_table[i][j - 1] == 0 and j != 0:
                break
            if series[i - j] == series[i + 1 + j]:
                even_table[i][j] = 1

    answers = []
    for start, end in questions:
        mid = (end + start) // 2
        offset = mid - start
        if (end - start) % 2 == 0:  # odd
            answers.append(odd_table[mid][offset])
            continue
        answers.append(even_table[mid][offset])  # even
    return answers


solution()

# test cases I've tried:
'''
10
1 2 3 4 5 6 7 8 9 10
11
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10
1 10

6
1 2 1 3 2 1
1 
1 3
for even
for odd

7
1 2 1 4 3 2 1
1 
1 3 
for odd
for even
'''
