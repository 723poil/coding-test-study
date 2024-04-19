def buildTree(node):
    edges = []
    for i in range(1, node):
        edges.append((1, i+1))
    return edges

def calculateMinDistanceSum(N):
    return (N-1)**2

N = int(input())
print(calculateMinDistanceSum(N))
edges = buildTree(N)
for u, v in edges:
    print(u, v)
