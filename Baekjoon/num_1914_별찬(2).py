
def hanoi(diskSize: int, start: int, via: int, end: int) -> int:
    if diskSize == 1:
        print(start, end)
        return
    hanoi(diskSize - 1, start, end, via)
    hanoi(1, start, via, end)
    hanoi(diskSize - 1, via, start, end)


def solution():
    diskSize = int(input())
    print(2**diskSize - 1)
    if diskSize <= 20:
        hanoi(diskSize, 1, 2, 3)


solution()
