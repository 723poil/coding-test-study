from collections import deque


def bfs(x, y, wall):
    queue = deque([(x, y, wall)])
    # wall 있는지 없는지 유무로 나뉨
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    # visited[y][x][0]: 벽을 부수지 않고 이동
    # visited[y][x][1]: 벽을 부수고 이동
    visited[0][0][0] = 1
    while queue:
        x, y, wall = queue.popleft()
        if x == M-1 and y == N-1:
            return visited[y][x][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < M and 0 <= ny < N):
                continue
            # 이동 가능한 칸 and 아직 방문 x
            if wallMap[ny][nx] == 0 and visited[ny][nx][wall] == 0:
                visited[ny][nx][wall] = visited[y][x][wall] + 1
                queue.append((nx, ny, wall))
            # 벽이 존재하지만 and 아직 부수지 않고 and 방문하지 않은 경우
            if wallMap[ny][nx] == 1 and wall == 0 and visited[ny][nx][1] == 0:
                visited[ny][nx][1] = visited[y][x][wall] + 1
                queue.append((nx, ny, 1))

    return -1

def solution():
    shortestPath = bfs(0,0, 0)
    print(shortestPath)


N, M = map(int, input().split())
wallMap = [[] for _ in range(N)]
for i in range(N):
    wallMap[i] = list(map(int, list(input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

solution()