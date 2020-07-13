# name: 종이의 개수
# date: July 13, 2020
# status: solved

from sys import stdin
import math


def solution():
    length = int(stdin.readline())
    matrix = [list(map(int, stdin.readline().split(' ')))
              for i in range(length)]
    answer = [0, 0, 0]
    cut(matrix, 0, 0, length, answer)
    for frequency in answer:
        print(frequency)


def cut(matrix, start_x, start_y, length, frequency):
    if length == 1:
        index = find_index(matrix, start_x, start_y)
        frequency[index] += 1
        return
    if is_all_the_same(matrix, start_x, start_y, length):
        index = find_index(matrix, start_x, start_y)
        frequency[index] += 1
        return
    total_pieces = 0
    pieces_length = length // 3
    for offset_y in range(3):
        for offset_x in range(3):
            cut(matrix, start_x + pieces_length *
                offset_x, start_y + pieces_length * offset_y, pieces_length, frequency)


def is_all_the_same(matrix, start_x, start_y, length):
    start_value = matrix[start_y][start_x]
    for offset_y in range(length):
        for offset_x in range(length):
            if start_value != matrix[start_y + offset_y][start_x + offset_x]:
                return False
    return True


def find_index(matrix, x, y):
    if matrix[y][x] == -1:
        return 0
    if matrix[y][x] == 0:
        return 1
    if matrix[y][x] == 1:
        return 2


solution()
