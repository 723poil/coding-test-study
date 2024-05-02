def main(N, graph):
    INF = int(1e9)
    minCost = INF

    def backTracking(depth, current, cost):
        nonlocal minCost, visited, start
        if depth == N:
            # 이부분 처음에 놓쳐서 헤맴
            # if문이 없으면 길이 없는 경우에도 돌아오게 되어 최솟값이 틀리게 나옴
            if graph[current][start] > 0:
                minCost = min(minCost, cost + graph[current][start])
            return
        for next in range(1, N):
            if not visited[next] and graph[current][next] > 0:
                visited[next] = True
                backTracking(depth + 1, next, cost + graph[current][next])
                visited[next] = False

    for i in range(N):
        visited = [False] * N
        visited[i] = True
        start = i
        backTracking(1, start, 0)

    # # 사이클이니까 출발지점은 중요하지  않아서 모든 출발 지점 고려할 필요없이 하나만 고려하면 됨
    # visited = [False] * N
    # backTracking(1, 0, 0)
    print(minCost)

if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input().split()))for _ in range(N)]
    main(N, graph)
