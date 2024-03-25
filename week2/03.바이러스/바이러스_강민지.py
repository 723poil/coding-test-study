def dfs(graph, root, visited):
    
    visited[root] = True

    for i in graph[root]:
        if not visited[i]:
            dfs(graph, i, visited)

    return visited

n = int(input()) # 컴퓨터 수
m = int(input()) # 네트워크 수

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_= dfs(graph, 1, visited)
print(sum(visited)-1)