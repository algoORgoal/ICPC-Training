# name: 쿼드트리
# date: July 13, 2020
# status: solved

from sys import stdin


def solution():
    length = int(stdin.readline())
    image = [[int(letter) for letter in stdin.readline() if letter != '\n']
             for i in range(length)]
    expression = []
    compress(image, length, 0, 0, expression)
    answer = ''.join(expression)
    print(answer)


def compress(image, length, start_x, start_y, expression):
    if length == 1 or is_all_the_same(image, length, start_x, start_y):
        expression.append(str(image[start_y][start_x]))
        return

    half = length // 2
    expression.append('(')
    compress(image, half, start_x, start_y, expression)
    compress(image, half, start_x + half, start_y, expression)
    compress(image, half, start_x, start_y + half, expression)
    compress(image, half, start_x + half, start_y + half, expression)
    expression.append(')')


def is_all_the_same(image, length, x, y):
    first_element = image[y][x]
    for offset_y in range(length):
        for offset_x in range(length):
            if image[y + offset_y][x + offset_x] != first_element:
                return False
    return True


solution()
