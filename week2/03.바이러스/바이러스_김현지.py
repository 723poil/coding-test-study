
def dfs(graph, node, visited):
    visited[node] = True
    for i in graph[node]:
        if visited[i]:
            continue
        dfs(graph, i, visited)
    return visited
def main(graph, visited):
    return dfs(graph, 1, visited)

numComputer = int(input())
numPairs = int(input())

graph = [[] for _ in range(numComputer+1)]
for _ in range(numPairs):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
visited = [False] * (numComputer + 1)

visitedResult = main(graph, visited)

cnt = 0
for isVisited in visitedResult:
    if isVisited == True:
        cnt += 1
print(cnt-1)