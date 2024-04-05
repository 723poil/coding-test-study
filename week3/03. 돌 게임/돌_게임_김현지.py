# 돌의 개수
N = int(input())

# 상근 입장에서 생각하기
dp = [False] * (N+1)

# 초기 조건
if N >= 1:
    dp[1] = True
if N >= 3:
    dp[3] = True

# 이전 단계에서 패배 = 이번 단계에서의 승리
for i in range(4, N+1):
    if not dp[i-1] or not dp[i-3]:
        dp[i] = True

if dp[N] == True:
    print("SK")
else:
    print("CY")
