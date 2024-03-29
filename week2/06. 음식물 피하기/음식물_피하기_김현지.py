from collections import deque


def bfs(x, y):
    cnt = 0
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        if not (0 <= x < M and 0 <= y < N):
            continue
        if trash[y][x] == 0:
            continue
        trash[y][x] = 0
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            queue.append((nx, ny))
    return cnt


def solution():
    maxSize = 0
    for i in range(N):
        for j in range(M):
            if trash[i][j] == 1:
                size = bfs(j, i)
                maxSize = max(maxSize, size)
    print(maxSize)


N, M, K = map(int, input().split())
trash = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(K):
    r, c = map(int, input().split())
    trash[r - 1][c - 1] = 1

solution()
