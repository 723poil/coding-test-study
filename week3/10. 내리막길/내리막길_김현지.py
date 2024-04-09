def dfs(x, y):
    # print("dp", dp)
    if x == N-1 and y == M-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        if heightMap[ny][nx] < heightMap[y][x]:
            dp[y][x] += dfs(nx, ny)
    return dp[y][x]


# M : 세로의 길이, N: 가로의 길이
M, N = map(int, input().split())
heightMap = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(dfs(0, 0))

