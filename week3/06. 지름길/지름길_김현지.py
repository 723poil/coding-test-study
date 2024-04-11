N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]
shortcuts.sort(key=lambda x:x[0])

dp = [i for i in range(D+1)]

for start, end, distance in shortcuts:
    if end > D or start > D:
        continue
    dp[end] = min(dp[end], dp[start] + distance)
    for i in range(end, D+1):
        dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[D])

