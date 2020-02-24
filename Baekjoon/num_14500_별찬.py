width, length = map(int, input().split())
sheet = list()


for i in range(width):
    sheet.append(list(map(int, input().split())))


def dfs(x, y, width, length, sheet, depth, max):
    depth += 1
    max += sheet[x][y]
    if depth == 4:
        return max
    else:
        if x < width - 1:
            return dfs(x + 1, y, width, length, sheet, depth, max)
        else:

        if y < length - 1:
            return dfs(x, y + 1, width, length, sheet, depth, max)
        else:
