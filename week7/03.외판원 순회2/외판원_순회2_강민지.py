# 여행 순회 경로 구하기
# 최소 비용 출력
    ## 최소 비용으로 모든 도시를 이동
    ## 비용 0 <=> 이동할 수 없는 도시

# 모든 경우의 수에 대하여 비용 구하기

n = int(input())
cost_matrix = [list(map(int, input().split())) for _ in range(n)]
inf = int(1e10)
min_cost = inf

def recursive(route=[], cost=0):
    global min_cost

    # ※빼먹은 부분: 가지치기※
    if cost >= min_cost:
        return

    if len(route) == n:
        added_cost = cost_matrix[route[-1]][route[0]]
        if added_cost > 0:
            min_cost = min(min_cost, cost+added_cost)
            return
        return
    
    for i in range(n):
        if len(route) == 0:
            route.append(i)
            recursive(route, 0)
            route.pop()
        else:
            last_city = route[-1]
            part_cost = cost_matrix[last_city][i]
            if (i not in route) and (part_cost>0):
                route.append(i)
                recursive(route, cost+part_cost)
                route.pop()

recursive()
print(min_cost)
                
