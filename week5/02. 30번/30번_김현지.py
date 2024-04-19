def divideByTwo(num):
    listNum = [num]
    while num != 1:
        num = num//2
        listNum.append(num)
    listNum.sort(reverse=True)
    return listNum

def findMaxCommon(listA, listB):
    listALen = len(listA)
    listBLen = len(listB)
    for i in range(listALen):
        for j in range(listBLen):
            if listA[i] == listB[j]:
                return listA[i]

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    listA = [a]
    listB = [b]
    listA = divideByTwo(a)
    listB = divideByTwo(b)
    print(10 * findMaxCommon(listA, listB))
