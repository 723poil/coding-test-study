from sys import stdin
from collections import deque

input = stdin.readline

def bfs_tomato(tomato: list, pos: tuple, zero_c: int, ones: deque):
    x = [0, 1, 0, -1]
    y = [1, 0, -1, 0]
    
    m, n = pos
    
    count = 0
        
    while ones:
        cp, cc = ones.popleft()
        
        for i in range(4):
            curx = cp[1]+x[i]
            cury = cp[0]+y[i]
            
            if 0 <= curx < m and 0 <= cury < n and tomato[cury][curx] == 0:
                ones.append(((cury, curx), cc + 1))
                tomato[cury][curx] = 1
                zero_c -= 1
                
        count = max(cc, count)
        
    if zero_c > 0:
        return -1
    
    return count
        

def solution():
    M, N = map(int, input().split())
    
    tomato = []
    zero_c = 0
    ones = deque()
    
    for n in range(N):
        tomato.append(list(map(int, input().split())))
        
        zero_c += tomato[n].count(0)
        
        for m in range(M):
            if tomato[n][m] == 1:
                ones.append(((n, m), 0))
        
    return bfs_tomato(tomato, (M, N), zero_c, ones)

print(solution())