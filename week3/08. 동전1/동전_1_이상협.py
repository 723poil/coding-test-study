from sys import stdin

input = stdin.readline

def find_case(coins: list, k: int):
    
    # 0원부터 k원까지 경우의 수 저장하기 위한 리스트 선언
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for coin in coins:
        for d in range(coin, k+1):
            # 현재 d원이 가지고 있는 경우의 수에서 지금 coin값을 더했을때의 경우의 수 추가
            dp[d] += dp[d - coin]
            
    return dp[-1]
    

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