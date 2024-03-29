from collections import deque


def bfs(x, y):
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < M and 0 <= ny < N):
                continue
            if maze[ny][nx] == 0:
                continue
            if maze[ny][nx] == 1:
                maze[ny][nx] = maze[y][x] + 1
                queue.append((nx, ny))
    return maze[N-1][M-1]

def solution():
    minSize = bfs(0, 0)
    print(minSize)

N, M = map(int, input().split())
maze = [[] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    maze[i] = list(map(int, list(input())))
solution()