from collections import deque


def getTotalDamage():
    totalDamage = sum(value[0] for value in knightDamage.values() if value[1] != 0)
    totalDamage -= sum(value[1] for value in knightDamage.values() if value[1] != 0)
    return totalDamage

def updateDamage(attackingKnight):
    for i in range(L):
        for j in range(L):
            # 함정에 걸려든 경우 and 기사가 함정에 있고 해당 기사가 공격 기사가 아닐 때
            if chess[i][j] == 1 and located[i][j][0] != 0 and located[i][j][0] != attackingKnight:
                damage = located[i][j][1]
                located[i][j][1] -= 1
                knightDamage[located[i][j][0]][1] = damage-1
                bfs(j, i, located[i][j][0], damage)

def bfs(x, y, attackedKnight, damage):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < L and 0 <= ny < L):
                continue
            # 데미지 -1
            # if located[ny][nx][0] != 0 and located[ny][nx][0] != attackingKnight:
            if located[ny][nx][0] == attackedKnight and located[ny][nx][1] == damage:
                located[ny][nx][1] -= 1
                # 체력을 다하면 체스판에서 out
                if located[ny][nx][1] == 0:
                    located[ny][nx][0] = 0
                queue.append((nx, ny))

# 벽에 부딪치지 않는다면 기사 이동
def moveKnights(ithKnight, direction):
    afterMoveLocated = [[[0, 0] for _ in range(L)] for _ in range(L)]
    if direction == 0: # 위쪽
        for i in range(L):
            for j in range(L):
                ni, nj = (i-1)%L, j
                afterMoveLocated[ni][nj] = located[i][j]
                if afterMoveLocated[ni][nj] != [0,0] and chess[ni][nj] == 2:
                    return located
    elif direction == 1: # 오른쪽
        for i in range(L):
            for j in range(L):
                ni, nj = i, (j+1)%L
                afterMoveLocated[ni][nj] = located[i][j]
                if afterMoveLocated[ni][nj] != [0,0] and chess[ni][nj] == 2:
                    return located
    elif direction == 2: # 아래쪽
        for i in range(L):
            for j in range(L):
                ni, nj = (i+1)%L, j
                afterMoveLocated[ni][nj] = located[i][j]
                if afterMoveLocated[ni][nj] !=[0,0] and chess[ni][nj] == 2:
                    return located
    elif direction == 3: # 왼쪽
        for i in range(L):
            for j in range(L):
                ni, nj = i, (j-1)%L
                afterMoveLocated[ni][nj] = located[i][j]
                if afterMoveLocated[ni][nj] != [0,0] and chess[ni][nj] == 2:
                    return located
    return afterMoveLocated

def locateKnightsOnChess():
    # located = [[[0, 0] for _ in range(L)] for _ in range(L)]
    for num, knight in enumerate(knights):
        r, c, h, w, k = knight[0]-1, knight[1]-1, knight[2], knight[3], knight[4]
        knightDamage[num+1] = [k, k]
        for i in range(r, r+h):
            for j in range(c, c+w):
                # 기사 번호
                located[i][j][0] = num+1
                # 기사 체력
                located[i][j][1] = k
    return located


def solution():
    # 체스판에 Knight 위치시킴
    global located
    located = locateKnightsOnChess()
    # 명령에 따라 움직임
    for order in orders:
        # order[0]: i번째 기사
        # order[1]: d방향
        move = True
        i, d = order[0], order[1]
        afterMoveLocated = moveKnights(i, d)
        if located == afterMoveLocated:
            continue
        located = afterMoveLocated
        updateDamage(i)
    print(getTotalDamage())



L, N, Q = map(int, input().split())
chess = [[] for _ in range(L)]
knights = [[] for _ in range(N)]
knightDamage = dict()
orders = [[] for _ in range(Q)]
for i in range(L):
    chess[i] = list(map(int, input().split()))
for i in range(N):
    knights[i] = list(map(int, input().split()))
for i in range(Q):
    orders[i] = list(map(int, input().split()))
located = [[[0, 0] for _ in range(L)] for _ in range(L)]



# 위, 오른, 아래, 왼
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


solution()