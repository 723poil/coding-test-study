n=int(input())
dp=[-1, -1, -1, 1, -1, 1]
for i in range(6, n+1):
    if dp[i-3]==-1 and dp[i-5]==-1:
        dp.append(-1)
    elif dp[i-3]!=-1 and dp[i-5]==-1:
        dp.append(dp[i-3]+1)
    elif dp[i-3]==-1 and dp[i-5]!=-1:
        dp.append(dp[i-5]+1)
    else:
        dp.append(min(dp[i-5], dp[i-3])+1)
print(dp[n])