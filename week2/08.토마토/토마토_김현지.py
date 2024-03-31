from collections import deque


def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < M and 0 <= ny < N):
                continue
            if tomatoes[ny][nx] == -1:
                continue
            if tomatoes[ny][nx] == 0:
                tomatoes[ny][nx] = tomatoes[y][x] + 1
                queue.append((nx, ny))

def countMinDays():
    days = 0
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 0:
                return -1
            days = max(days, max(tomatoes[i]))
    return days-1

def solution():
    queue = deque()
    for i in range(N):
        for j in range(M):
            # 시작점 여러개
            if tomatoes[i][j] == 1:
                queue.append((j, i))
    bfs(queue)
    minDays = countMinDays()
    print(minDays)

M, N = map(int, input().split())
tomatoes = [[] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    tomatoes[i] = list(map(int, input().split()))
solution()