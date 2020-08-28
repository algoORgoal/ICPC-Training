# name: 테트로미노
# date: August 28, 2020
# status: solved

from sys import stdin


def solution():
    n, m = [int(char) for char in stdin.readline().strip().split(' ')]
    sheet = [[int(char) for char in stdin.readline().strip().split(' ')]
             for _ in range(n)]
    reversed_sheet = [list(reversed(row)) for row in sheet]
    sheets, reversed_sheets = generate_versions(
        sheet, 4), generate_versions(reversed_sheet, 4)
    versions = sheets + reversed_sheets
    answer = max([maximize(version) for version in versions])
    print(answer)


def generate_versions(sheet, left):
    if left == 4:
        return [sheet] + generate_versions(sheet, left - 1)
    if left == 0:
        return []
    turned_sheet = [[sheet[i][j] for i in range(len(sheet))]
                    for j in reversed(range(len(sheet[0])))]
    sheets = generate_versions(turned_sheet, left - 1)
    return sheets + [turned_sheet]


def maximize(sheet):
    row = len(sheet)
    col = len(sheet[0])
    return max([sum_up_each_shape(i, j, row, col, sheet) for i in range(row) for j in range(col)])


def sum_up_each_shape(i, j, n, m, sheet):
    shapes = [0]
    # shape 1:
    if i < n - 3:
        shapes.append(sheet[i][j] + sheet[i + 1][j] +
                      sheet[i + 2][j] + sheet[i + 3][j])
    # shape 2:
    if i < n - 1 and j < m - 1:
        shapes.append(sheet[i][j] + sheet[i + 1][j] +
                      sheet[i][j + 1] + sheet[i + 1][j + 1])
    # shape 3:
    if i < n - 2 and j < m - 1:
        shapes.append(sheet[i][j] + sheet[i + 1][j] +
                      sheet[i + 2][j] + sheet[i][j + 1])
    # shape 4:
    if i < n - 2 and j < m - 1:
        shapes.append(sheet[i][j] + sheet[i + 1][j] +
                      sheet[i + 1][j + 1] + sheet[i + 2][j + 1])
    # shape 5:
    if i < n - 2 and j < m - 1:
        shapes.append(sheet[i][j] + sheet[i + 1][j] +
                      sheet[i + 2][j] + sheet[i + 1][j + 1])
    return max(shapes)


solution()

# test cases I've tried:
'''
3 3
1 2 3
4 5 6
7 8 9

4 4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
'''
