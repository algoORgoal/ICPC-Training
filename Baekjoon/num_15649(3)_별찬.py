# pick m numbers out of [1...n]

def solution() -> None:
    n, m = [int(string) for string in input().split(' ')]

    for i in range(1, n + 1):
        SEQUENCE_STR = 'sequence'
        VISITED_STR = 'visited'
        root = {SEQUENCE_STR: [i], VISITED_STR: {i: True}}
        stack = []

        stack = stack + [root]

        while len(stack) > 0:
            current = stack.pop()
            if len(current[SEQUENCE_STR]) == m:
                print(*current[SEQUENCE_STR], sep=" ")

            for j in range(n, 0, -1):
                if j not in current[VISITED_STR]:
                    new = {
                        'sequence': current[SEQUENCE_STR][:] + [j],
                        'visited': {
                            **current[VISITED_STR],
                            j: True,
                        }
                    }
                    stack = stack + [new]


solution()
