from sys import stdin

input = stdin.readline

def check_lastest(stack: list, ks_c: list) -> int:
    
    # 현재 스택에 있는 전자기기중 이제 쓰지 않을 예정이거나 가장 늦게 사용할 것으로 예상되는 전자기기를 선정
    temp = [
        (
            i,                                         # 1 -> 전자기기 이름
            ks_c[i][0] if len(ks_c[i]) != 0 else 999,  # 2 -> 다음에 이 전자기기를 사용하게 될 인덱스 가져오기 (없을 경우 999)
            0 if i in stack else 999                   # 3 -> 스택에 없으면 안뽑히게 하기위해 999로 설정
        ) for i in range(1, len(ks_c))
    ]
    
    temp.sort(key= lambda x: (
        x[2], # 3 -> 스택에 없는 친구들 뒤로 정렬 목적
        -x[1] # 2 -> 이제 사용할 예정이 없는 전자기기 또는 사용예정이지만 가장 나중에 사용하게될 전자기기 선정 목적
    ))

    return stack.index(temp[0][0])  # 1 -> 전자기기 이름으로 index 찾기

def optimal_method(N: int, K: int, ks: list, ks_c: list) -> int:
    
    stack = []
    count = 0
    
    for i in range(K):
        # 이미 꽂혀있으면 넘어가기
        if ks[i] in stack:
            ks_c[ks[i]].pop(0)
            continue
        
        # 플러그 남았을때 그냥 꽂기
        if len(stack) < N:
            stack.append(ks[i])
            ks_c[ks[i]].pop(0)
            continue
        
        # 최적의 경우 찾기
        index = check_lastest(stack, ks_c)
        ks_c[ks[i]].pop(0)
        stack[index] = ks[i]
        
        count += 1    
            
    return count

def solution():
    N, K = map(int, input().split())
    
    ks = list(map(int, input().split()))
    ks_c = [[] for _ in range(K+1)]
    
    for k in range(K):
        ks_c[ks[k]].append(k)
    
    return optimal_method(N, K, ks, ks_c)

print(solution())