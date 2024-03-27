from collections import deque

def bfs(box, rc_list):

    n, m = len(box), len(box[0])
    drdc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque(rc_list)

    while queue:
        r, c = queue.popleft()

        for d in drdc:
            dr, dc = d
            new_r = r + dr
            new_c = c + dc

            if new_r < 0 or new_c < 0 or new_r >= n or new_c >= m:
                continue

            if box[new_r][new_c] == 0:
                box[new_r][new_c] += box[r][c] + 1
                queue.append((new_r, new_c))
    return box

        
m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

ripe_rc_list = []
for r in range(n):
    for c in range(m):
        if box[r][c] == 1:
            ripe_rc_list.append((r, c))

box = bfs(box, ripe_rc_list)
nums_in_box = [i for row in box  for i in row]

if 0 in nums_in_box:
    print(-1)
else:
    print(max(nums_in_box)-1)