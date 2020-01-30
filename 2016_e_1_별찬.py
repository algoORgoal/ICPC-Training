

def find_start(triangle):
    last_row = triangle[len(triangle) - 1]
    max = 0
    for i in range(0, len(last_row)):
        if last_row[max] < last_row[i]:
            max = i

    return max


def find_max(triangle, row, index, memo):
    if row == 0:
        return triangle[0][0]
    elif index == len(triangle[row]) - 1:
        if memo[row - 1][index -
                         1] == -1:
            memo[row - 1][index -
                          1] = find_max(triangle, row - 1, index - 1, memo)
        return memo[row - 1][index -
                             1] + triangle[row][index]
    elif index == 0:
        if memo[row - 1][index] == -1:
            memo[row - 1][index] = find_max(triangle, row - 1, index, memo)
        return memo[row-1][index] + triangle[row][index]
    else:
        if memo[row - 1][index -
                         1] == -1:
            memo[row - 1][index -
                          1] = find_max(triangle, row - 1, index - 1, memo)
        if memo[row - 1][index] == -1:
            memo[row - 1][index] = find_max(triangle, row - 1, index, memo)
        left_side = memo[row - 1][index - 1]
        right_side = memo[row - 1][index]
        if (left_side > right_side):
            return left_side + triangle[row][index]
        else:
            return right_side + triangle[row][index]


triangle = list()
count_row = int(input())
memo = list()

for i in range(count_row):
    row = input().split()
    for k in range(len(row)):
        row[k] = int(row[k])
    triangle.append(row)


for i in range(count_row):
    row = list()
    for j in range(i + 1):
        row.append(-1)
    memo.append(row)


count_last_row = count_row - 1
max = find_max(triangle, count_last_row, 0, memo)
for i in range(1, count_row):
    temp = find_max(triangle, count_last_row, i, memo)
    if max < temp:
        max = temp
print(max)
