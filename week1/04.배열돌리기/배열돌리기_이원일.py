# 1. tgt = 라인 돌리기 부분, 움직일 list = 주대각, 부대각, 가운데 행, 가운데 열 => 4개
# 2. 복사할 matrix 하나 초기화
# 3. 안 바뀌는 부분(정가운데, 빈 곳), 빈곳은 원래 0으로 new_mat으로 해두고 0인 부분은 for 문 돌면서 그 부분만 0이면 원래 mat에서 인덱스로 접근해서 복사하기  
# 4. 음수 각도 = -(360 - 양수 각도)
# 5. 회전 규칙 경우의 수 다 나누기
# 6. 초기 점(대각선으로 하면 0,0 지점이 회전 시에 어디로 가는 지) 지정

# 5. 회전 규칙 경우의 수 다 나누기 -> 잘못접근함. 그냥 인덱싱을 각 4개의 경우로 나누고 -> 예를 들면 한 대각선이 갈수 있는 8가지로 접근하는 게 맞음.
# 


########################################################################
# 1번째 방식 -> 실패
########################################################################

# import sys
# input = sys.stdin.readline

# T = int(input().strip())

# main_diag = []
# sub_diag = []
# row = []
# col = []

# for i in range(T):
#     n, d = map(int, input().split())    
#     og_mat = [list(map(int, input().split())) for _ in range(n)]
#     turned_mat = [[0]*n for _ in range(n)]
    

# # 45 d
# for i in range(n):
#     for j in range(n):
#         main_diag.append(og_mat[i][j])
        
        
# for i in range(n):
#     turned_mat[i][n+1//2] = main_diag[i]
    
########################################################################
# 2번째 방식 => 여전히 틀림
########################################################################

import sys
input = sys.stdin.readline

T = int(input().strip())
final_mat = []

for i in range(T):
    n, d = map(int, input().split())    
    og_mat = [list(map(int, input().split())) for _ in range(n)]
    turned_mat = [[0]*n for _ in range(n)]

    if d < 0:
        d = 360 + d
    
    #어려웠던 부분 1
    start = d // 45 - 1 # 0 ~ 7
    
    # example
    # ['1 기준에서', ' ', '2', ' ', '3'],
    # [' ', ' ', ' ', ' ', ' '],
    # ['8', ' ', ' ', ' ', '4'],
    # [' ', ' ', ' ', ' ', ' '],
    # ['7', ' ', '6', ' ', '5']

    vector_list = [] # 원래 매트릭스의 주대각, 행, 부대각, 열 순서로 임시로 저장할 리스트
    vector_list.append([og_mat[i][i] for i in range(n)]) # 주대각
    vector_list.append([og_mat[n+1//2-1][i] for i in range(n)]) # 행
    vector_list.append([og_mat[n-i-1][i] for i in range(n-1, -1, -1)]) #부대각성분 # 거꾸로 가기
    vector_list.append([og_mat[i][n+1//2-1] for i in range(n)]) # 열

    # b_i는 움직일 벡터, 그리고 그것이 처음 시작할 곳 = start
    for vec_i in range(4):
        # 어려웠던 부분 2
        index = (vec_i + start) % 8  # 0 ~ 7

        if index == 0: # 45d
            for i in range(n):
                turned_mat[i][n+1//2-1] = vector_list[vec_i][i]
        
        elif index == 1: # 90
            for i in range(n):
                turned_mat[i][n-i-1] = vector_list[vec_i][i]
        
        elif index == 2: # 135
            for i in range(n):
                turned_mat[n+1//2-1][i] = vector_list[vec_i][i]
        
        elif index == 3: # 180
            for i in range(n):
                turned_mat[n-i-1][n-i-1] = vector_list[vec_i][i]

        elif index == 4: # 225
            for i in range(n):
                turned_mat[n-i-1][n+1//2-1] = vector_list[vec_i][i]
        
        elif index == 5: # 270
            for i in range(n):
                turned_mat[n+1//2-1][i] = vector_list[vec_i][i]
        
        elif index == 6: # 315
            for i in range(n):
                turned_mat[n+1//2-1][i] = vector_list[vec_i][i]
        
        else: #index == 7: # 360    
            for i in range(n):
                turned_mat[i][i] = vector_list[vec_i][i]
            
            
    # 안 움직인 애들 처리
    for i in range(n):
        for j in range(n):
            if turned_mat[i][j] == 0:
                turned_mat[i][j] = og_mat[i][j]
    
    for tmp_idx in range(n):
        final_mat.append(turned_mat[tmp_idx])

for tmp_list in range(len(final_mat)):
    print(*tmp_list)