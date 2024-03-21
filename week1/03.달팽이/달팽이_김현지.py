import sys
input = sys.stdin.readline

N = int(input())
target = int(input())

maze = [[0]*N for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
x, y = N // 2, N // 2

val = 1
dirIdx = 0
move = 1
foundX, foundY = 0, 0

while val <= N**2:
    for _ in range(2):
        for _ in range(move):
            # 마지막엔 2번이 아니라 한번만 갱신되어야하므로 이 부분 추가
            if val > N**2:
                break
            maze[y][x] = val
            if val == target:
                foundX, foundY = x, y
            val+=1
            x += dx[dirIdx]
            y += dy[dirIdx]
        dirIdx = (dirIdx + 1) % 4
    move += 1

for i in range(N):
    print(" ".join(map(str, maze[i])))

print(foundY+1, foundX+1)
