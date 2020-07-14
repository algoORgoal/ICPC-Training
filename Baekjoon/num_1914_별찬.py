# name: 하노이 탑
# date: July 12, 2020
# status: solved

from sys import stdin


def solution():
    total_disks = int(stdin.readline())
    disk_size = total_disks
    history = []
    count = 2 ** total_disks - 1
    print(count)
    if total_disks <= 20:
        move(1, 3, disk_size)


def move(move_from, move_to, size):
    count = 0
    if (size == 1):
        print(move_from, move_to)
        return
    another_rod = find_another_rod(move_from, move_to)
    move(move_from, another_rod, size - 1)
    print(move_from, move_to)
    move(another_rod, move_to, size - 1)


def find_another_rod(move_from, move_to):
    rods = [move_from, move_to]
    if 1 not in rods:
        return 1
    if 2 not in rods:
        return 2
    if 3 not in rods:
        return 3


solution()
