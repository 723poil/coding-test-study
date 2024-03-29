import collections

n, m=map(int,input().split())
maps=[list(map(int, list(input()))) for _ in range(n)]
# bfs
q=collections.deque()
q.append([0,0])
maps[0][0]+=1
while q:
    x, y=q.popleft()
    for mx, my in [[1, 0],[-1, 0],[0, 1], [0, -1]]:
        nx=mx+x
        ny=my+y
        if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1: # 한번도 지난간적이 없는, 갈 수 있는 곳이라면
            maps[nx][ny]+=maps[x][y] # 누적된 길들을 더해준다.
            q.append((nx, ny))
print(maps[n-1][m-1]-1)