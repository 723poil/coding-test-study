from sys import stdin

input = stdin.readline

def setNumber(ss: list) -> list:
    temp_index = -1
    index = 0
    sss = []
    
    while index < len(ss):
        if ss[index].isdigit():
            if temp_index == -1:
                temp_index = index
            index += 1
            continue
        
        if temp_index != -1:
            sss.append("".join(ss[temp_index: index]))
            temp_index = -1
        
        sss.append(ss[index])
        index += 1
        
    last = "".join(ss[temp_index: index])
    
    if len(last) != 0:
        sss.append(last)
        
    return sss

def findMin(sss: list) -> int:
    temp_sum = 0
    result = 0
    
    for i in range(len(sss)-1, -1, -1):
        if sss[i].isdigit():
            temp_sum += int(sss[i])
            continue
        
        if sss[i] == '+':
            continue
        
        result -= temp_sum
        temp_sum = 0
        
    return result + temp_sum

def solution():
    ss = list(str(input().rstrip()))
    
    sss = setNumber(ss)
    
    return findMin(sss)

print(solution())