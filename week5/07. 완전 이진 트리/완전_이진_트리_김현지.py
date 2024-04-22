def buildLevels(K, nodes):
    levels = [[] for _ in range(K)]
    idx = 0

    def inorder(level):
        nonlocal idx
        if level >= K:
            return
        # 왼쪽 자식 노드
        inorder(level+1)
        # 현재 노드
        levels[level].append(nodes[idx])
        idx += 1
        # 오른쪽 자식 노드
        inorder(level+1)

    inorder(0)
    return levels

def main():
    K = int(input())
    nodes = list(map(int, input().split()))
    levels = buildLevels(K, nodes)
    for level in levels:
        print(" ".join(map(str, level)))

if __name__ == '__main__':
    main()