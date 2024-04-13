N = int(input())

# 상근이가 배달하는 봉지의 최소 개수, 정확하게 N 킬로그램을 만들 수 없다면 -1 출력
MAX = N+1
dp = [MAX] * (N+1)

# 초기화
dp[3] = 1
if N >= 5:
    dp[5] = 1

for i in range(4, N+1):
    minCnt = min(dp[i-3], dp[i-5])
    if dp[i-3] == 0 and dp[i-5] == 0:
        continue
    elif dp[i-3] != 0 and dp[i-5] != 0:
        dp[i] = min(dp[i-3], dp[i-5]) + 1
    elif dp[i-3] == 0 and dp[i-5] != 0:
        dp[i] = dp[i-5] + 1
    elif dp[i-3] != 0 and dp[i-5] == 0:
        dp[i] = dp[i-3] + 1

if dp[N] != 0:
    print(dp[N])
else:
    print(-1)
