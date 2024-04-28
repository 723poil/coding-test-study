def findSeat(N, favorites):
    grid = [[0]*N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for student, likes in favorites.items():
        candidate = []
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    likeCnt, emptyCnt = 0, 0
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if not (0 <= nr < N and 0 <= nc < N):
                            continue
                        if grid[nr][nc] in likes:
                            likeCnt += 1
                        elif grid[nr][nc] == 0:
                            emptyCnt += 1
                    candidate.append((likeCnt, emptyCnt, r, c))
        # 최적의 자리 선택
        candidate.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
        _, _, bestR, bestC = candidate[0]
        grid[bestR][bestC] = student

    return grid

def calculateSatisfaction(N, seats, favorites):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    totalSatisfaction = 0
    for r in range(N):
        for c in range(N):
            likeStudentCnt = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if seats[nr][nc] in favorites[seats[r][c]]:
                    likeStudentCnt += 1
            if likeStudentCnt == 4:
                totalSatisfaction += 1000
            elif likeStudentCnt == 3:
                totalSatisfaction += 100
            elif likeStudentCnt == 2:
                totalSatisfaction += 10
            elif likeStudentCnt == 1:
                totalSatisfaction += 1
    return totalSatisfaction



    pass

def main():
    N = int(input())
    favorites = dict()
    for i in range(N**2):
        inputs = list(map(int, input().split()))
        favorites[inputs[0]] = inputs[1:]
    seats = findSeat(N, favorites)
    satisfaction = calculateSatisfaction(N, seats, favorites)
    print(satisfaction)


if __name__ == '__main__':
    main()