def solution(n, boxes):
    if n == 1:
        return 1

    # DP의 기본 아이디어: LIS(Longest Increasing Subsequence)
    # dp[i] = i번째 상자를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
    dp = [1] * (n+1)

    for i in range(2, n+1):
        for j in range(1, i):
            if boxes[i-1] > boxes[j-1]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


n = int(input())
boxes = list(map(int, input().split()))
print(solution(n, boxes))
