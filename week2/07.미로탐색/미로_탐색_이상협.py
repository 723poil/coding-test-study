from sys import stdin

input = stdin.readline

def find_finish(miro: list, pos: tuple):
    x = [0, 1, 0, -1]
    y = [1, 0, -1, 0]
    
    n, m = [pos[0]-1, pos[1]-1]
    
    qq = [((0, 0), 1)]
    miro[0][0] = 0
    
    while qq:
        cp, cc,  = qq.pop(0)
        
        if cp[0] == n and cp[1] == m:
            return cc
        
        for i in range(4):
            cur_x = cp[1] + x[i]
            cur_y = cp[0] + y[i]
            
            if 0 <= cur_x <= m and 0 <= cur_y <= n and miro[cur_y][cur_x] == 1:
                qq.append(((cur_y, cur_x), cc+1))
                miro[cur_y][cur_x] = 0

def solution():
    N, M = map(int, input().split())
    
    miro = []
    
    for _ in range(N):
        row = list(map(int, list(str(input().strip()))))
        
        miro.append(row)
        
    return find_finish(miro, (N, M))
        

print(solution())