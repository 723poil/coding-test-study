N = int(input())

cowDict = dict()

cnt = 0
for _ in range(N):
    cowNum, location = map(int, input().split())
    if cowNum in cowDict:
        if location != cowDict.get(cowNum):
            cnt += 1
    cowDict[cowNum] = location

print(cnt)