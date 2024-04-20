n, m = map(int, input().split())

edge_list = [[0, 1], [1, 2]]
root = 1
leaf = 2
leaf_cnt = 2

for i in range(3, n):

    # 새로운 leaf 추가
    if leaf_cnt < m:
        edge_list.append([root, i])
        leaf_cnt += 1

    # 기존 leaf에 간선 추가
    else:
        edge_list.append([leaf, i])
    leaf = i


for e in edge_list:
    print(e[0], e[1])