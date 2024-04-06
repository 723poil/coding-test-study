from sys import stdin

input = stdin.readline

INF = int(1e9)

def solution():
    N, S = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    sum = sequence[0]
    li = 0
    ri = 0
    
    result = INF
    
    while ri < N-1:
        # 1. 합이 S보다 작을 경우 ri +1 후 더해주기
        if sum < S:
            ri += 1
            sum += sequence[ri]
        
        # 2. li == ri 일 경우 1 반환
        if sum >= S:
            if li == ri:
                return 1
            
            # 3. 합이 S보다 크거나 같은 경우만 남았으므로 li를 움직인다.
            result = min(ri - li + 1, result)
            sum -= sequence[li]
            li += 1    
            
        # 4. 이놈 추가하면 시간 단축 40% 가능
        elif sum < S and (ri - li + 1) >= result:
            sum -= sequence[li]
            li += 1  
            
    for lli in range(li, ri+1):
        if sum >= S:
            result = min(result, ri - lli + 1) 
       
        sum -= sequence[lli]
        if sum < S:
            break
        
    return result if result != INF else 0

print(solution())