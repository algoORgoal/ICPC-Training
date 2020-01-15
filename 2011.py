


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

'''
def crypto(num):
    if num == 0:
        return 0
    elif num <= 10:
        return 1
    elif num <= 26:
        return 2
    else:
        i = 1
        while(num//i >= 10):
            i *= 10
        remainder = num % i
        
        if(num//(i/10) <= 26):
            return crypto(remainder) + crypto(remainder%(i/10))
        else:
            return crypto(remainder)

num = int(input())
result = crypto(num)
print(result%1000000)
'''



def crypto(num, dic, idx_list):
    print("=======")
    print(num)
    if num == '0':
        return 0
    if num in idx_list:
        if num in idx_list[0:10]:
            return 1
        else:
            return 2
    else:
        print(num[1:])
        print(num[2:])
        if num in dic.keys():
            return dic[num]
        else:
            two_d = num[0:2]
            
            if two_d in idx_list:
                
                dic[num] = crypto(num[1:], dic, idx_list) + crypto(num[2:], dic,  idx_list)
            else:
                dic[num] = crypto(num[1:], dic, idx_list)
            print("=======")
            return dic[num]
    

            



    

str1 = input()
dic = dict()
idx_list = list()
for i in range(1, 27):
    idx_list.append(str(i))

print(idx_list[0:10])
result = crypto(str1, dic, idx_list)
print(dic)
print(result)
print(result%1000000)