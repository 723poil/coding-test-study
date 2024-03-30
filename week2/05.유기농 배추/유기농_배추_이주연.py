import collections
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, k =map(int, input().split()) # 가로(j), 세로(i), 배추 갯수
    maps = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(k):
        y, x = map(int, input().split())
        maps[x][y] = 1 # 배추를 심은 곳의 위치
    # BFS
    cnt = 1
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                cnt += 1
                q = collections.deque()
                q.append([i, j])
                maps[i][j] = cnt
                while q:
                    cx, cy = q.popleft()
                    for mx, my in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        nx = cx + mx
                        ny = cy + my
                        if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                            maps[nx][ny] = cnt # 양배추를 먹어야 하는 곳이라면.해당 갯수의 벌레가 먹는다.
                            q.append([nx, ny])
    if cnt == 1:
        print(0)
    else:
        print(cnt - 1)

