


'''
    날짜: 2020-01-11
    언어: python
    문제: 2017년도 초등부 문제 3(백준 14864번)
    작성자: 김별찬
'''



def getPair(countPair):
    pair = list()
    i = 0
    while(i < countPair):
        first, second = input().split()
        first = int(first)
        second = int(second)
        pair.append(list([first, second]))
        i += 1
    return pair

def isCardFake(pair, total):
    for i in pair:
        if(total[i[0] - 1] < total[i[1] - 1]):
            print(-1)
            return True
    return False


def main():
    countStu, countPair = input().split()
    countStu = int(countStu)
    countPair = int(countPair)

    index = list()
    frequency = list()

    pair = list()
    pair = getPair(countPair)

    total = list()

    for i in range(0, countStu):
        index.append(i + 1)
        frequency.append(0)

    for i in pair:
        frequency[i[0] - 1] += 1
    

    for i in range(0, len(frequency)):
        total.append(index[frequency[i]])
        index.pop(frequency[i])

    if(not isCardFake(pair, total)):
        for i in total:
            print(i, end=" ")
    
    
main()