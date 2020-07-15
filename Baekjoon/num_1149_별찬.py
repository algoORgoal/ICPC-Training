# name: RGB거리
# date: July 15, 2020
# status: solved


import sys
sys.setrecursionlimit(100000)


def solution():
    total_houses = int(sys.stdin.readline())
    costs = [list(map(int, sys.stdin.readline().split(' ')))
             for i in range(total_houses)]
    memo = [[0, 0, 0] for i in range(total_houses)]
    answer = find_minimal_cost(costs, [0, 0], 0, memo)
    print(answer)


def find_minimal_cost(coloring_costs, current_color, distance, memo):

    if memo[distance][current_color[0]] != 0 and memo[distance][current_color[1]] != 0:
        return memo[distance][current_color[0]] if memo[distance][current_color[0]] < memo[distance][current_color[1]] else memo[distance][current_color[1]]
    if distance == 0:
        minimal_cost = 1000000
        for initial_color in range(len(coloring_costs[0])):
            total_cost = coloring_costs[0][initial_color] + \
                find_minimal_cost(
                coloring_costs, find_other_colors(initial_color), distance + 1, memo)

            if total_cost < minimal_cost:
                minimal_cost = total_cost
        return minimal_cost
    if distance == len(coloring_costs) - 1:
        first_color, second_color = current_color
        memo[distance][first_color], memo[distance][second_color] = coloring_costs[distance][first_color], coloring_costs[distance][second_color]

        return memo[distance][first_color] if memo[distance][first_color] <= memo[distance][second_color] else memo[distance][second_color]

    first_color, second_color = current_color
    next_color1, next_color2 = list(map(find_other_colors, current_color))

    memo[distance][first_color] = coloring_costs[distance][first_color] + \
        find_minimal_cost(coloring_costs, next_color1, distance + 1, memo)
    memo[distance][second_color] = coloring_costs[distance][second_color] + \
        find_minimal_cost(coloring_costs, next_color2, distance + 1, memo)
    return memo[distance][first_color] if memo[distance][first_color] <= memo[distance][second_color] else memo[distance][second_color]


def find_other_colors(index):
    colors = [0, 1, 2]
    colors.pop(index)
    return colors


solution()
