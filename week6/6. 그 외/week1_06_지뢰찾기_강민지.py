"""
!주의! 지뢰가 있는 칸이 열렸다면 지뢰가 있는 모든 칸이 열려야 함
"""

def get_bomb_nums(bom_loc_list, row, col):
    n = len(bom_loc_list)
    drdc = [(0, -1), (-1, 0), (0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    cnt = 0
    for dr, dc in drdc:
        if 0 <= row + dr < n and 0 <= col + dc < n:
            if bom_loc_list[row + dr][col + dc] == "*":
                cnt += 1
    return cnt     


n = int(input())
bomb_loc_list = [list(input()) for _ in range(n)]
open_stat_list = [list(input()) for _ in range(n)]

# 열린 부분 숫자 채우기
step_bomb_flag = False
for i in range(n):
    for j in range(n):
        if open_stat_list[i][j]=='x':
            if bomb_loc_list[i][j] == ".":
                bomb_num = get_bomb_nums(bomb_loc_list, i, j)
                open_stat_list[i][j] = str(bomb_num)

            else:
                step_bomb_flag = True

# 지뢰를 밟으면 모든 지뢰 open => 지뢰 채우기
if step_bomb_flag:
    for i in range(n):
        for j in range(n):
            if bomb_loc_list[i][j] == "*":
                open_stat_list[i][j] = "*"

for o in open_stat_list:
    print(''.join(o))

