# name: Fire!
# date: July 13, 2020
# status: unsolved

from sys import stdin


def solution():
    row, col = list(map(int, stdin.readline().split(' ')))
    maze = [list(stdin.readline()) for i in range(col)]
    print(maze)


solution()
