
countStick, height = input().split()
countStick = int(countStick)
height = int(height)

lines = [[], []]
for i in range(0, countStick):
    up, down = input().split()
    up = int(up)
    down = int(down)
    lines[0].append(up)
    lines[1].append(down)
'''
for i in range(0, countStick):
    up, down = input().split()
    up = int(up)
    down = int(down)
    lines.append([up, down])
'''

dis = list()


'''
dis = [initial_point, final_point, boolean1, boolean2, cost]]
boolean1: True -> initial point on upside
          False -> inital point on downside
boolean1: True -> final point on upside
          False -> final point on downside
'''


for i in range(0, countStick):
    up = lines[0][i]
    down = lines[1][i]
    is_initial_up = True
    is_final_up = False
    dis.append([up, down, is_initial_up, is_final_up, abs(up - down) + height])


'''
for pair in lines:
    up = pair[0]
    down = pair[1]
    is_initial_up = True
    is_final_up = False
    dis.append([up, down, is_initial_up, is_final_up, abs(up - down) + height])
'''


print(lines)
print(dis)




for i in range(0, countStick):
    temp = lines[1].copy()
    temp.pop(i)
    if lines[1][i] in temp:
        print("똑같은게 있다")
    else:
        print("똑같은게 없다")
        


