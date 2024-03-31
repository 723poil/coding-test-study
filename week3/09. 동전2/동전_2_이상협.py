from sys import stdin

input = stdin.readline

INF = int(1e9)

def find_case(coins: list, k: int):
    global INF
    
    # 0원부터 k원까지 동전 개수 저장하기 위한 리스트 선언
    dp = [INF] * (k + 1)
    dp[0] = 0
    
    for coin in coins:
        for d in range(coin, k+1):
            # 동전 개수가 최소가 되도록 유지
            dp[d] = min(dp[d], 1 + dp[d - coin])
            
    # 불가능한 경우 -1 반환
    return dp[-1] if dp[-1] != INF else -1
    

def solution():
    n, k = map(int, input().split())
    
    coins = []
    
    for _ in range(n):
        coin = int(input())
        
        # k보다 값이 큰 동전은 필요없으므로 제외
        if coin <= k:
            coins.append(coin)
            
    coins.sort(key= lambda x: -x)
    
    return find_case(coins, k)
    

print(solution())