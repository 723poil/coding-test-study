from collections import deque
from copy import deepcopy


def bfs(x, y, wallList, newWallMap):
    breakWall = False
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        print("x", x, "y", y)
        newWallMap[y][x] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < M and 0 <= ny < N):
                continue
            # 벽 부술 수 있는 다양한 경우의 수를 어떻게 처리할지가 관건
            if newWallMap[ny][nx] == 1 and breakWall == False and (nx, ny) in wallList:
                newWallMap[ny][nx] = newWallMap[y][x] + 1
                queue.append((nx, ny))
                breakWall = True
                wallList.remove((nx, ny))
                print("wallList", wallList)
            if newWallMap[ny][nx] == 0:
                newWallMap[ny][nx] = newWallMap[y][x] + 1
                queue.append((nx, ny))
    return newWallMap[N-1][M-1]

def getWalls():
    wallList = list()
    for i in range(N):
        for j in range(M):
            if wallMap[i][j] == 1:
                wallList.append((j, i))
    return wallList

def solution():
    print("wallList", wallList)
    shortestPath = M * N
    wallListCnt = len(wallList)
    while True:
        if not wallList:
            break
        print("while wallList", wallList)
        newWallMap = deepcopy(wallMap)
        shortestPath = min(shortestPath, bfs(0,0, wallList, newWallMap))
        # 이미 부쉈던 벽을 부수지 않으면 길이 안생기는 경우
        if wallListCnt == len(wallList):
            break
        wallListCnt = len(wallList)
    if shortestPath == 1:
        print(-1)
        return
    print(shortestPath)


N, M = map(int, input().split())
wallMap = [[] for _ in range(N)]
for i in range(N):
    wallMap[i] = list(map(int, list(input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print("오리지널 wallMap", wallMap)
wallList = getWalls()
solution()
print("이동 후 wallMap", wallMap)