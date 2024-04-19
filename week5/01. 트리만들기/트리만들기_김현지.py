def buildTree(n, m):
    edges = []
    # 루트 노드 0에 리프 노드를 m개만큼 연결
    for i in range(1, m+1):
        edges.append((0, i))

    # 남은 노드들을 이전의 노드들에 연결
    lastConnected = 1
    for i in range(m+1, n):
        edges.append((lastConnected, i))
        lastConnected = i
    return edges

# n: 노드, m: 리프
n, m = map(int, input().split())
edges = buildTree(n, m)
for u, v in edges:
    print(u,v)