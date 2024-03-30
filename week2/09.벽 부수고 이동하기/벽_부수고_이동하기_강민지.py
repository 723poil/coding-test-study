"""
Fail 
- 시간초과
- 틀린 풀이 방법 : 전체 벽을 부수는 모든 경우의 수에 대해 BFS를 수행 
- 원인 : 
    > 일반적으로 1초 안에 수행할 수 있는 연산 => 1억 = 10**8
    > 위와 같이 풀면 10**6 x 10**6 = 10 **12가 됨

- 올바른 풀이
    > 벽 부쉈는지 아닌지에 따라 경우를 나눠서 visited를 저장
    > 먼저 끝나는 결과 출력(최단거리)
"""


from collections import deque

def get_valid_wall_list(matrix):
    n, m = len(matrix), len(matrix[0])

    valid_wall_set = set([])
    for r in range(n-1):
        for c in range(m):
            if matrix[r][c] == 0:
                
                if c+1 < m: 
                    if matrix[r][c+1]==1:
                        valid_wall_set.add((r, c+1))

                if r+1 < n:
                    if matrix[r+1][c] ==1:
                        valid_wall_set.add((r+1, c))

                if c-1 >= 0:
                    if matrix[r][c-1]==1:
                        valid_wall_set.add((r, c-1))

                if 4-1 >= 0:
                    if matrix[r-1][c]==1:
                        valid_wall_set.add((r-1, c))
    return list(valid_wall_set)


def bfs(matrix):
    n, m = len(matrix), len(matrix[0])
    drdc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    matrix[0][0] = 1
    queue = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()

        for d in drdc:
            dr, dc = d
            new_r, new_c = r+dr, c+dc
            if new_r < 0 or new_c < 0 or new_r >= n or new_c >= m:
                continue
            
            if matrix[new_r][new_c] == 0:
                matrix[new_r][new_c] += matrix[r][c] + 1
                queue.append((new_r, new_c))

    last_pang = matrix[n-1][m-1]
    return last_pang


n, m = map(int, input().split())
mat = [list(map(int, list(input()))) for _ in range(n)]

valid_wall_list = get_valid_wall_list(mat)

results = []
for wall_idx in valid_wall_list:
    new_mat = [row.copy() for row in mat]
    wall_r, wall_c = wall_idx
    new_mat[wall_r][wall_c] = 0
    result = bfs(new_mat)
    # print(f"{new_mat} / {result}")
    if result:
        results.append(result)

if results:
    print(min(results))
else:
    print(-1)