def solution() -> None:
    n = int(input())
    m = int(input())
    connections = [[int(string) for string in input().split(' ')]
                   for i in range(0, n)]
    plan = [int(string) - 1 for string in input().split(' ')]

    visited = [False for i in range(0, n)]

    # dfs
    root = plan[0]
    stack = [root]
    visited[root] = True

    while len(stack) > 0:
        current = stack.pop()
        for city, isAdjacent in enumerate(connections[current]):
            if not visited[city] and isAdjacent:
                stack.append(city)
                visited[city] = True

    for city in plan:
        if not visited[city]:
            print("NO")
            return

    print('YES')


solution()
