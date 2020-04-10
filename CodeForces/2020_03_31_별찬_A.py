


def solve(test, test_range):
    a, b, c, d = test.split()
    x, y, x1, y1, x2, y2 = test_range.split()
    # right : +, up: +
    horizontal = b - a
    vertical = d - c
    isX = False
    isY = False
    if (a == b == 0): #안움직여도 된다.
        isX = True
    elif (x == x1 == x2): # 못움직인다.
        isX = False
    elif (x + horizontal >= x1 and x + horizontal <= x2):
        isX = True
    else:
        isX = False
    if (c == d == 0):  # 안움직여도 된다.
        isY = True
    elif (y == y1 == y2):  # 못움직인다.
        isY = False
    elif (y + vertical >= y1 and y + vertical <= y2):
        isY = True
    else:
        isY = False
    
    if (isX == True and isY == True):
        return True
    else:
        return False


    



countTest = int(input())
for i in range(countTest):
    test = list(map(int, input().split()))
    test_range = list(map(int, input().split()))
    if (solve(test, test_range)):
        print("YES")
    else:
        print("NO")

