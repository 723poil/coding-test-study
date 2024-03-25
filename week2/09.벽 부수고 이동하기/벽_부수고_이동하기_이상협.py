from sys import stdin
from collections import deque

input = stdin.readline

# def find_finish(maps: list, pos: tuple):
#     x = [0, 1, 0, -1]
#     y = [1, 0, -1, 0]
    
#     n, m = pos
    
#     searched = [[False for _ in range(m)] for _ in range(n)]
#     searched_broken = [[False for _ in range(m)] for _ in range(n)]
    
#     qq = deque()
    
#     qq.append(((0,0), 1, False))
#     searched[0][0] = True
    
#     while qq:
#         cp, cc, cb = qq.popleft()
        
#         if cp[0] == n-1 and cp[1] == m-1:
#             return cc
        
#         for i in range(4):
#             curx = cp[1] + x[i]
#             cury = cp[0] + y[i]
            
#             able_pos = 0 <= curx < m and 0 <= cury < n
            
#             if able_pos and not searched[cury][curx]:
#                 if cb:
#                     if maps[cury][curx] == 0 and not searched_broken[cury][curx]:
#                         searched_broken[cury][curx] = True
#                         qq.append(((cury, curx), cc + 1, cb))
#                 else:
#                     if maps[cury][curx] == 0:
#                         searched[cury][curx] = True
#                         qq.append(((cury, curx), cc + 1, cb))
#                     else:
#                         searched[cury][curx] = True
#                         qq.append(((cury, curx), cc + 1, True))
        
#     return -1

# def solution():
#     N, M = map(int, input().split())
    
#     maps = []
    
#     for _ in range(N):
#         maps.append(list(map(int, list(str(input().strip())))))
        
#     return find_finish(maps, (N, M))

# print(solution())


## solution 2
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
INF = int(1e9)
N, M = map(int, input().split())

def bfs(start: tuple, maps: list):
    global N, M, d, INF
    
    qq = deque()
    qq.append(start)
    
    searched = [[INF for _ in range(M)] for _ in range(N)]
    searched[start[0]][start[1]] = 0
    
    while qq:
        y, x = qq.popleft()
        
        for dx, dy in d:
            cy = y + dy
            cx = x + dx
            
            if not (0 <= cy < N and 0 <= cx < M):
                continue
            if searched[cy][cx] != INF:
                continue
            searched[cy][cx] = searched[y][x] + 1
            if maps[cy][cx] == 0:
                qq.append((cy, cx))
                
    return searched


def solution():
    maps = [list(map(int, input().strip())) for _ in range(N)]
    
    start_b = bfs((0, 0), maps)
    end_b = bfs((N-1, M-1), maps)
    
    result = min(INF, start_b[N-1][M-1] + 1)
    
    for n in range(N):
        for m in range(M):
            if maps[n][m] == 1:
                result = min(result, start_b[n][m] + end_b[n][m] + 1)
                
    return result if result != INF else -1

print(solution())