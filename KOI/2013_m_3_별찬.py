'''
#윗주석 없음
#주석 추가 요망
'''

def find_dis(dis):
    while(True):
        temp = list()
        count = 0 
        #dis랑 lines를 비교해서 연결될 수 있는 모든 것을 찾는다.
        for i in range(0, countStick):
            final_point = dis[i][1]
            sec_to_last = dis[i][5]
            if lines[i][0] < lines[j][0] and lines[i][1] == lines[j][1]:


        for i in range(0, countStick):
            for j in range(i + 1, countStick):
                if lines[i][0] < lines[j][0] and lines[i][1] == lines[j][1]:
                    init_point = lines[i][0]
                    sec_to_last = final_point
                    final_point = lines[j][0]                        
                    is_final_up = True
                    length = dis[i][4] + dis[j][4]
                    temp.append([init_point, final_point, is_init_up, is_final_up, length, sec_to_last])
                elif lines[i][1] < lines[j][1] and lines[i][0] == lines[j][0]:
                    init_point = lines[i][1]
                    sec_to_last = final_point
                    final_point = lines[j][1]
                    is_final_up = False
                    length = dis[i][4] + dis[j][4]
                    temp.append([init_point, final_point, is_init_up, is_final_up, length, sec_to_last])
                else:
                    count += 1
    
            for i in range(0, countStick):
                for j in range(i + 1, countStick):
                    if lines[i][0] < lines[j][0] and lines[i][1] == lines[j][1]:
                        init_point = lines[i][0]
                        final_point = lines[j][0]
                        is_final_up = True
                        length = dis[i][4] + dis[j][4]
                        temp.append([init_point, final_point, is_init_up, is_final_up, length])
                    elif lines[i][1] < lines[j][1] and lines[i][0] == lines[j][0]:
                        init_point = lines[i][1]
                        final_point = lines[j][1]
                        is_final_up = False
                        length = dis[i][4] + dis[j][4]
                        temp.append([init_point, final_point, is_init_up, is_final_up, length])
                    else:
                        count += 1
        max_trial = len(dis) * len(dis)-1 / 2
        if(max_trial == count):
            return dis
        dis = temp
        print(dis)
    


countStick, height = input().split()
countStick = int(countStick)
height = int(height)

lines = []

'''
lines = [[x1, x2, ..], [y1, y2, ..]]
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





dis = list()
#dis stores [initial point, final point, second to last point, is_init_up, is_final_up, length]
for i in range(0, countStick):
    init_point = lines[i][0]
    final_point = lines[i][1]
    sec_to_last = init_point
    is_init_up = True
    is_final_up = False
    length = abs(init_point - final_point) + height
    dis.append([init_point, final_point, is_init_up, is_final_up, length, sec_to_last])

print(lines)
print(dis)
find_dis(dis)
'''
점에서 점 사이가 조건을 만족하는 경우, 두 점 사이의 거리를 저장해서 다음 계산시에도 쓴다!
'''

#아래쪽에서 연결된 경우








