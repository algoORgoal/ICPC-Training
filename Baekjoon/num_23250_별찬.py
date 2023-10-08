
def hanoi(diskSize: int, move: list[int], goal_step, total_step) -> None:
    [start, via, end] = move
    if diskSize == 1:
        print(start, end)
        return

    middle = total_step // 2 + 1
    if goal_step < middle:
        hanoi(diskSize - 1, [start, end, via], goal_step, middle - 1)
    elif goal_step == middle:
        hanoi(1, [start, via, end], goal_step, total_step)
    else:
        hanoi(diskSize - 1, [via, start, end],
              goal_step - middle, total_step - middle)


def solution():
    diskSize, goal = [int(string) for string in input().split(' ')]
    step = 2 ** diskSize - 1
    hanoi(diskSize, (1, 2, 3), goal, step)


solution()
