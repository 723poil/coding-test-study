import copy

def makeNewMap(R, C, islandMap):
    newMap = copy.deepcopy(islandMap)
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]


    for i in range(R):
        for j in range(C):
            if islandMap[i][j] == "X":
                cnt = 0
                for k in range(4):
                    if not (0 <= i + dx[k] < R and 0 <= j + dy[k] < C):
                        cnt += 1
                        continue
                    if islandMap[i + dx[k]][j + dy[k]] == ".":
                        cnt += 1
                if cnt >= 3:
                    newMap[i][j] = "."
    return newMap

def resizeCoordinate(R, C, newMap):
    minX, minY, maxX, maxY = -1, -1, -1, -1
    for i in range(R):
        for j in range(C):
            if newMap[i][j] == "X":
                if (minX == -1 or minX > i):
                    minX = i
                if (minY == -1 or minY > j):
                    minY = j
                if (maxX == -1 or maxX < i):
                    maxX = i
                if (maxY == -1 or maxY < j):
                    maxY = j
    return minX, minY, maxX, maxY

R, C = map(int, input().split())
islandMap = [list(input()) for _ in range(R)]

newMap = makeNewMap(R, C, islandMap)
minX, minY, maxX, maxY = resizeCoordinate(R, C, newMap)


for i in range(minX, maxX+1):
    print("".join(newMap[i][minY:maxY+1]))
