from collections import deque
from copy import deepcopy

def dfs(graph, node, visited, path):
    visited[node] = True
    path.append(node)
    for i in graph[node]:
        if visited[i]:
            continue
        dfs(graph, i, visited, path)
    return path

def bfs(graph, node, visited, path):
    visited[node] = True
    queue = deque([node])
    while queue:
        vertex = queue.popleft()
        path.append(vertex)
        for i in graph[vertex]:
            if visited[i]:
                continue
            queue.append(i)
            visited[i] = True
    return path

def main(graph, visited, V):
    bfsVisited  = deepcopy(visited)
    dfsPath = dfs(graph, V, visited, [])
    bfsPath = bfs(graph, V, bfsVisited, [])
    print(" ".join(map(str, dfsPath)))
    print(" ".join(map(str, bfsPath)))


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
visited = [False] * (N+1)
sortedGraph = list(map(sorted, graph))


main(sortedGraph, visited, V)