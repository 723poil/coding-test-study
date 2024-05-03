################################################################################
# sol 1) backtracking 방식
################################################################################
# 가능한 모든 경우 실행 => 정답
# 중복체크 
# 종료 조건 
# 하부 함수 호출

import sys

def dfs(n:int, tmp_list:list) -> list:
    
    if n == M:
        ans.append(tmp_list)
        return
    
    prev = 0
    for i in range(N):
        if v[i] == 0 and prev != lst[i]:
            prev=lst[i]
            v[i] = 1
            dfs(n+1, tmp_list+[lst[i]])
            v[i] = 0
        
def main(N, M):
    global ans, v
    lst.sort()
    ans = []
    v = [0]*N
    tmp_list = []
    dfs(0, tmp_list)
    
    return ans

if __name__=="__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    global lst
    lst = list(map(int, input().strip().split()))
    rets = main(N, M)
    for ret in rets:
        print(*ret)