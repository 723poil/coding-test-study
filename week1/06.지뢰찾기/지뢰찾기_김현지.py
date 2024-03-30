import copy

def countMines(i, j, n, mines):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    x, y = i, j
    cnt = 0
    if mines[x][y] == '*':
        return -1
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if not (0 <= nx < n and 0 <= ny < n):
            continue
        if mines[nx][ny] == '*':
            cnt += 1
    return cnt

def markAllMines(n, mines, revealedMines):
    for i in range(n):
        for j in range(n):
            if mines[i][j] == '*':
                revealedMines[i][j] = '*'

n = int(input())

mines = [list(input()) for _ in range(n)]
openedMines = [list(input()) for _ in range(n)]
revealedMines = copy.deepcopy(openedMines)

for i in range(n):
    for j in range(n):
        if openedMines[i][j] == '.':
            continue
        if openedMines[i][j] == 'x':
            mineCnt = countMines(i, j, n, mines)
            if (mineCnt != -1):
                revealedMines[i][j] = mineCnt
        # 지뢰가 있는 칸이 열렸다면 지뢰가 있는 모든 칸을 *로 표시
        if mines[i][j] == '*':
            markAllMines(n, mines, revealedMines)
for row in range(n):
    print("".join(map(str, revealedMines[row])))
