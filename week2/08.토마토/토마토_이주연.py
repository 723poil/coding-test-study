import sys
import collections

input = sys.stdin.readline
m, n=map(int, input().split())
maps=[list(map(int, input().split())) for _ in range(n)]
q=collections.deque() # 위치 저장.
zero=0
for i in range(n):
    for j in range(m):
        if maps[i][j]==1:
            q.append([i, j])
        elif maps[i][j]==0:
            zero+=1
if zero==0: # 이미 모든 토마토가 익어있는 상태
    print(0)
else:
    while q:
        x, y=q.popleft()
        for mx,my in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx=mx+x
            ny=my+y
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==0:
                maps[nx][ny]=maps[x][y]+1
                q.append([nx, ny])
    # 토마토 확인
    total_chk=False
    total_day=0
    for i in range(n):
        for j in range(m):
            if maps[i][j]==0:
                total_chk=True
                break
            total_day=max(total_day, maps[i][j])
        if total_chk:
            break
    if total_chk:
        print(-1)
    else:
        print(total_day-1)