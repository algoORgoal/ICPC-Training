SHEEP = 'S'


def solution():
    row, column = [int(string) for string in input().split(' ')]
    farm = [[letter for letter in input()] for i in range(0, row)]
    [isEverySheepProtected, newFarm] = checkAccessibility(farm, [
        row, column])
    if not isEverySheepProtected:
        print(isEverySheepProtected)
    else:
        print(isEverySheepProtected)
        for i in range(0, row):
            print(*newFarm[i], sep='')


def checkAccessibility(farm: list[list[str]], shape: [int, int]) -> [int, list[list[str]]]:
    [row, column] = shape
    for x in range(0, row):
        for y in range(0, column):
            if farm[x][y] == 'W':
                isLeftSheep = x > 0 and farm[x - 1][y] == SHEEP
                isRightSheep = x < row - 1 and farm[x + 1][y] == SHEEP
                isUpSheep = y > 0 and farm[x][y - 1] == SHEEP
                isDownSheep = y < column - 1 and farm[x][y + 1] == SHEEP
                if isLeftSheep | isRightSheep | isUpSheep | isDownSheep:
                    return [0, None]

                if x > 0 and farm[x-1][y] == '.':
                    farm[x-1][y] = 'D'
                if x < row - 1 and farm[x+1][y] == '.':
                    farm[x+1][y] = 'D'
                if y > 0 and farm[x][y-1] == '.':
                    farm[x][y-1] = 'D'
                if y < column - 1 and farm[x][y+1] == '.':
                    farm[x][y+1] = 'D'

    return [1, farm]


solution()
