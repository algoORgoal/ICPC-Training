

'''
    날짜: 2020-01-16
    언어: python
    문제: 백준 2011번
    작성자: 김별찬
'''

'''
앞의 두자리수가 26 이하인 경우
f(25890) = f(5890) + f(890)
         = f(890) + f(90)
         = f(90) + f(0)
         = f(0) + f(0)
         = 0

앞의 두자리수가 27 이상인 경우
f(5890) = f(890) = f(90) = f(0) = 0

f(25114) = f(5114) + f(114)
         = f(114) + f(14) + f(4)
         = f(14) + f(4) + f(14) + f(4)
'''




import sys
sys.setrecursionlimit(100000)
def crypto(num, dic, idx_list):
    if num == '0' or '00' in num or num[0] == '0':
        return 0
    elif num in idx_list:
        if num in idx_list[0:10]:
            return 1
        else:
            return 2
    else:
        
        if num in dic.keys():
            return dic[num]
        else:
            two_d = num[0:2]
            if two_d in idx_list:
                dic[num] = crypto(num[1:], dic, idx_list) + crypto(num[2:], dic,  idx_list)
            else:
                dic[num] = crypto(num[1:], dic, idx_list)
            return dic[num]
str1 = input()
dic = dict()
idx_list = list()
for i in range(1, 27):
    idx_list.append(str(i))

result = crypto(str1, dic, idx_list)
print(result%1000000)