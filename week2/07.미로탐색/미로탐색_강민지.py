# (1, 1) => (N, M) 지나는 최소 칸 수
from collections import deque

def bfs(maze, r=0, c=0):
    n, m = len(maze), len(maze[0])
    drdc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for d in drdc:
            dr, dc = d
            new_r = r + dr
            new_c = c + dc 
            
            # maze를 넘어갔을 때
            if new_r < 0 or new_c < 0 or new_r >= n or new_c >= m:
                continue
            # maze 안에 있을 때
            else:
                if maze[new_r][new_c] == 1:
                    maze[new_r][new_c] += maze[r][c]
                    queue.append((new_r, new_c))

    return maze[n-1][m-1]
        

N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]


print(bfs(maze))