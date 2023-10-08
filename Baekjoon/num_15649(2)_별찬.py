from itertools import permutations


def solution():
    n, m = [int(string) for string in input().split(' ')]
    sequences = list(permutations([i for i in range(1, n + 1)], m))
    for sequence in sequences:
        print(*sequence, sep=" ")


solution()
