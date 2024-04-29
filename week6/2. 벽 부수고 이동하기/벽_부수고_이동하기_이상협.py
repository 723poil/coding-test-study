from sys import stdin
from collections import deque

input = stdin.readline

x = [0, 1, 0, -1]
y = [1, 0, -1, 0]

def bfs(start: list) -> list:
    for n in range(1, N+1):
        for m in range(1, M+1):
            visited[n][m] = False
            
    new_board = [[0 for _ in range(M+1)] for _ in range(N+1)]
            
    q = deque()
    q.append([start, 1])
    visited[start[0]][start[1]] = True
    new_board[start[0]][start[1]] = 1
    
    while q:
        cur, dis = q.popleft()
        
        for i in range(4):
            cx = cur[1] + x[i]
            cy = cur[0] + y[i]
            
            if not (0 < cx <= M and 0 < cy <= N):
                continue
            
            if visited[cy][cx]:
                continue
            
            visited[cy][cx] = True
            
            if board[cy][cx] != 0:
                new_board[cy][cx] = dis
            else:
                new_board[cy][cx] = dis + 1
                q.append([[cy, cx], dis+1])
            
    return new_board
        

if __name__ == '__main__':
    
    N, M = map(int, input().split())
    
    board = [[0]]
    visited = [[False for _ in range(M+1)] for _ in range(N+1)]
    
    for i in range(N):
        n_list = list(map(int, input().rstrip()))
        
        board.append([0] + n_list)
        
    start_b = bfs([1, 1])
    end_b = bfs([N, M])
    
    min_count = int(1e9)
    
    for n in range(1, N+1):
        for m in range(1, M+1):
            if start_b[n][m] == 0 or end_b[n][m] == 0:
                continue
            
            min_count = min(min_count, start_b[n][m] + end_b[n][m] + 1)
            
    min_count = min(min_count, start_b[N][M] if start_b[N][M] != 0 else int(1e9))
    
    print(min_count if min_count != int(1e9) else -1)
        
