from sys import stdin
from collections import deque

input = stdin.readline

def bfs():
    dp = [int(1e9)] * (k + 1)
    dp[0] = 0
        
    for coin in coins:
        for c in range(coin, k+1):
            dp[c] = min(dp[c], 1 + dp[c - coin])
                
    return dp[k] if dp[k] != int(1e9) else -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    
    coins = [int(input()) for _ in range(n)]
    
    print(bfs())