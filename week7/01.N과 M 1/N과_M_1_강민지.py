# # 내장함수
# from itertools import permutations

# n, m = map(int, input().split())
# perm = permutations([i for i in range(1, n+1)], m)

# for seq in perm:
#     print(' '.join(map(str, seq)))

#=============================================
# 백트래킹
n, m = map(int, input().split())
str_num = ""

def recursive(n, m):
    global str_num
    
    if len(str_num) == m:
        print(' '.join(str_num))
        return
    
    for i in range(1, n+1):
        str_i = str(i)
        
        if str_i not in str_num:
            str_num += str_i
            recursive(n, m)
            str_num = str_num[:-1] # 백트랙(backtrack): 이전 상태로 돌아가 다른 가능성을 탐색

recursive(n, m)