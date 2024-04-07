n=int(input())
MAX_NUM = 10**6+1
dp = [ MAX_NUM for _ in range(max(4, n+1))]
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(min(4, n+1), n+1):
    dp[i] = dp[i-1]
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2])
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3])
    dp[i]+=1

print(dp[n])