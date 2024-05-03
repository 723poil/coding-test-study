################################################################################
# sol 1) backtracking 방식
################################################################################
# 가능한 모든 경우 실행 => 정답
# 중복체크 
# 종료 조건 
# 하부 함수 호출

import sys

def bt(n:int, lst:list) -> list:
    # 종료조건(n에 관련) 처리 + 정답 처리도 일반적으로 한번에 해줌
    if n == M: # n: 선택된 숫자개수(길이)
        ans.append(lst)
        return
    
    # 하부단계(함수) 호출
    for i in range(1, N+1):
        if v[i] == 0: # 중복되지 않았을 때, 선택하지 않은 숫자인 경우 추가
            v[i] = 1
            bt(n+1, lst+[i])
            v[i] = 0

if __name__=="__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    ans = []        # 정답 리스트를 저장할 리스트, 길이 M짜리 수열
    v = [0]*(N+1)   # 중복 확인을 위한 visited[]
    
    bt(0, [])
    for lst in ans:
        print(*lst)
        
################################################################################
# sol 2) permutations 방식 - 성공 
################################################################################
# import sys
# from itertools import permutations

# def main(N, M):

#     lst_total = [ _ for _ in range(1, N+1)]
#     lst = []
#     for ele in permutations(lst_total, M):
#         lst.append(ele)
#     return lst

# if __name__=="__main__":
#     input = sys.stdin.readline
#     N, M = map(int, input().strip().split())
#     rets = main(N, M)
#     for ret in rets:
#         for intg in ret:
#             print(intg, end=' ')
#         print()