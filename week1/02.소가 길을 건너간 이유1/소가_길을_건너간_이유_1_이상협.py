import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    
    cows = [-1] * 11
    count = 0
    
    for _ in range(N):
        cow, loc = map(int, input().split())
        
        if cows[cow] == -1:
            cows[cow] = loc
        elif cows[cow] != loc:
            count+=1
            cows[cow] = loc
            
    return count

print(solution())