def dfs(x, y, field):
    if not (0 <= x < M and 0 <= y < N):
        return False
    if field[y][x] == 1:
        field[y][x] = 0
        dfs(x-1, y, field)
        dfs(x, y-1, field)
        dfs(x+1, y, field)
        dfs(x, y+1, field)
        return True
    return False


def countCabbageWarm(field):
    cabbageWarm = 0
    for i in range(N):
        for j in range(M):
            if dfs(j, i, field):
                cabbageWarm += 1
    print(cabbageWarm)


T = int(input())
for _ in range(T):
    M, N, K = map(int, (input().split()))
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, (input().split()))
        field[Y][X] = 1

    countCabbageWarm(field)