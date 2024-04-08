from sys import stdin

input = stdin.readline

def solution():
    N = int(input())
    mm = []
    index = 0
    result = 0
    
    for _ in range(N):
        mm.append(int(input()))
        
    mm.sort(key= lambda x: -x)
    
    while index < N:
        temp = mm[index: index+3]
        
        if len(temp) == 3:
            result += (sum(temp) - min(temp))
        else:
            result += sum(temp)
            
        index += 3
        
    return result

print(solution())