import sys

def construct_tree_with_leaves(n, m):
    edges = []
    # 기본 트리: 첫 번째 노드에서 시작하여 선형으로 연결
    for i in range(1, n):
        edges.append((i - 1, i))
    
    # 이미 2개의 리프 노드가 존재: 0번과 n-1번 노드
    additional_leaves_needed = m - 2
    
    # 1번 노드에 추가 리프 노드를 만들기 위해 새로운 노드를 연결
    current_leaf = n - 1  # 마지막으로 연결된 노드
    while additional_leaves_needed > 0:
        current_leaf += 1
        edges.append((1, current_leaf))
        additional_leaves_needed -= 1

    return edges

# 결과 출력 함수
def print_tree_edges(n, m):
    if m == 2:
        # 이미 처음 연결에서 2개의 리프가 만들어진 경우
        for i in range(n - 1):
            print(i, i + 1)
    else:
        edges = construct_tree_with_leaves(n, m)
        for u, v in edges:
            print(u, v)

if __name__=="__main__":
    input = sys.stdin.readline
    n, m = map(int, input().strip().split())
    ret = construct_tree_with_leaves(n, m)
    print(ret)

    # for i in ret:
    #     print(i, end=" ")