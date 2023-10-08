# pick m numbers out of [1...n]

def solution() -> None:
    n, m = [int(string) for string in input().split(' ')]

    for i in range(1, n + 1):
        root = [i]
        stack = []

        stack = stack + [root]

        while len(stack) > 0:
            current = stack.pop()
            if len(current) == m:
                print(*current, sep=" ")

            for j in range(n, 0, -1):
                if j not in current:
                    new = current[:] + [j]
                    stack = stack + [new]


solution()
