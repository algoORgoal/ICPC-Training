def solution():
    n, m = [int(letter) for letter in input().split(' ')]

    stack = [[i] for i in range(n, 0, -1)]
    result = []
    while len(stack) != 0:
        currentSequence = stack.pop()

        if len(currentSequence) == m:
            result.append(currentSequence)
            continue

        currentMax = currentSequence[len(currentSequence) - 1]

        for i in range(currentMax + 1, n + 1):
            stack.append(currentSequence + [i])
    sortedResult = sorted(result)
    for currentSequence in sortedResult:
        print(*sorted(currentSequence), sep=" ")


solution()
