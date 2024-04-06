from sys import stdin

input = stdin.readline

def counting(sources: list, M: int) -> int:
    
    count = 0
    
    si = 0
    ei = len(sources) - 1
    
    while si < ei:
        sumSource = sources[si] + sources[ei]
        if sumSource == M:
            si += 1
            ei -= 1
            count += 1
            continue
        
        if sumSource < M:
            ei -= 1
            continue
        
        if sumSource > M:
            si += 1
            continue
        
    return count

def solution():
    N = int(input())
    M = int(input())
    
    sources = sorted([source if source < M else 0 for source in list(map(int, input().split()))], key= lambda x: -x)
    
    while 0 in sources:
        sources.remove(0)
        
    return counting(sources, M)
    
print(solution())