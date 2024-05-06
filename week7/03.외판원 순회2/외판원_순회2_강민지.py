# 여행 순회 경로 구하기
# 최소 비용 출력
    ## 최소 비용으로 모든 도시를 이동
    ## 비용 0 <=> 이동할 수 없는 도시

# 모든 경우의 수에 대하여 비용 구하기

n = int(input())
cost_matrix = [list(map(int, input().split())) for _ in range(n)]
inf = int(1e10)
min_cost = inf
visited = [False] * n

def recursive(start_city, current_city, count, cost):
    
    global min_cost

    # 가지치기
    if cost >= min_cost:
        return

    # 종료 조건
    if count == n and cost_matrix[current_city][start_city]:
        min_cost = min(min_cost, cost+cost_matrix[current_city][start_city])
        return
    
    for i in range(n):
        if not visited[i] and cost_matrix[current_city][i]:
            visited[i] = True
            recursive(start_city, i, count+1, cost+cost_matrix[current_city][i])
            visited[i] = False # backtracking


for curr in range(n):
    visited[curr] = True
    recursive(curr, curr, 1, 0)
    visited[curr] = False

print(min_cost)