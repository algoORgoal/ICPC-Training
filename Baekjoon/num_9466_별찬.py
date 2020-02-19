'''
문제이름: 텀프로젝트
상태: 미완성
'''


def main():
    count_tests = int(input())
    for i in range(count_tests):
        count_students = int(input())
        selection = list()
        selection = input().split()
        for i in range(len(selection)):
            selection[i] = int(selection[i])
        print(selection)

        index_list = list()
        for i in range(1, count_students + 1):
            index_list.append(i)

        # print(index_list)

        students_in_team = 0
        while index_list:
            route = list()
            team = create_team(index_list[0], index_list[0], selection, route)
            if team:
                for member in team:
                    index_list.remove(member)
                    students_in_team += 1
            else:
                index_list.remove(index_list[0])
        students_out_of_team = count_students - students_in_team
        #print("students_out_of_team:", students_out_of_team)
        print(students_out_of_team)


def create_team(start, current, selection, route):
    # print("start", start)
    # print("current", current)
    route.append(current)
    # print("route", route)
    idx = current - 1
    if selection[idx] == start:
        return route
    elif selection[idx] in route:
        return []
    elif selection[idx] == current:  # when node points to itself
        if start == current:
            return route
        else:
            return []
    elif selection[idx] != start:
        return create_team(start, selection[idx], selection, route)


main()


'''
for i in range(1, count_students + 1):
    route = list()
    team = create_team(i, i, selection, route)
    # if team:
    print("case ", i, "team created: ", team)
'''


'''
for i in range(1, count_students + 1):
    route = list()
    team = create_team(i, i, selection, route)
    # if team:
    print("case ", i, "team created: ", team)
'''

'''
test case
2
7
3 1 3 7 3 4 6

2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
'''
