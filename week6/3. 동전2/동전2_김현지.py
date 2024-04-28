def main(coins):
    dp = [k+2] * (k+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, k+1):
            dp[i] = min(dp[i], dp[i-coin] + 1)

    if dp[k] == k+2:
        print(-1)
    else:
        print(dp[k]-1)

if __name__ == '__main__':
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    main(coins)
    