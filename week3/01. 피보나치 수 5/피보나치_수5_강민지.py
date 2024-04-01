memo = [0, 1] + [0] * 10000000

def dp(n:int):
    
    global memo

    if n == 0 or n == 1:
        return memo[n]

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]


n = int(input())
print(dp(n))