'''
문제 이름: 치즈
날짜: 2020-02-19
상태: 미해결(런타임 에러)
'''


def find_next(x, y, width, length, cheese):  # 0,0에서 시작
    cheese[x][y] = -1
    if x > 0:  # 상측 이동
        if cheese[x - 1][y] >= 1:
            cheese[x - 1][y] += 1
        elif cheese[x - 1][y] != -1:
            find_next(x - 1, y, width, length, cheese)
    if x < width - 1:  # 하측 이동
        if cheese[x + 1][y] >= 1:
            cheese[x + 1][y] += 1
        elif cheese[x+1][y] != -1:
            find_next(x + 1, y, width, length, cheese)
    if y > 0:  # 좌측 이동
        if cheese[x][y - 1] >= 1:
            cheese[x][y-1] += 1
        elif cheese[x][y - 1] != -1:
            find_next(x, y - 1, width, length, cheese)
    if y < length - 1:  # 우측 이동
        if cheese[x][y + 1] >= 1:
            cheese[x][y + 1] += 1
        elif cheese[x][y + 1] != -1:
            find_next(x, y + 1, width, length, cheese)


def melt(width, length, cheese):
    for i in range(width):
        for j in range(length):
            # 치즈 제거와 없던 부분은 다시 0으로 할당
            if cheese[i][j] == -1 or cheese[i][j] >= 3:
                cheese[i][j] = 0
            elif cheese[i][j] == 2:
                cheese[i][j] = 1


def is_all_melted(width, length, cheese):
    for i in range(width):
        for j in range(length):
            if cheese[i][j] != 0:
                return False
    return True


width, length = map(int, input().split())
width = int(width)
length = int(length)
cheese = list()

for i in range(width):
    line = list(map(int, input().split()))
    cheese.append(line)

count = 0
while not is_all_melted(width, length, cheese):
    find_next(0, 0, width, length, cheese)
    melt(width, length, cheese)
    count += 1
print(count)
'''
8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0       1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0

5 5
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
'''
