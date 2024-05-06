def main(students):
    results = 0
    N = 5
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y, visited, totalCnt, leeCnt):
        nonlocal results
        if totalCnt == 7:
            if leeCnt >= 4:
                results += 1
            return

        # 재귀 확장
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < N and not visited[nx][ny]):
                continue
            visited[nx][ny] = True
            dfs(nx, ny, visited, totalCnt + 1, leeCnt + (1 if students[nx][ny] == 'S' else 0))
            visited[nx][ny] = False

    for i in range(N):
        for j in range(N):
            visited = [[False] * N for _ in range(N)]
            visited[i][j] = True
            dfs(i, j, visited, 1, 1 if students[i][j] == 'S' else 0)

    print(results)

if __name__ == '__main__':
    students = []
    for _ in range(5):
        students.append(list(input()))
    main(students)