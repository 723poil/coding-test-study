"""
memo : i원을 낼 수 있는 경우의 수
* 주의 
- 겹치는 경우의 수가 있음
    (예) 3월을 만드는 경우 => (1, 2) = (2, 1) => 1번으로 count!
"""

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)


memo = [[] for _ in range(k+1)] # List of sets

# 전체 금액
for i in range(1, k+1):
    print(f"--> {i}")
    # 낼 수 있는 동전
    for c in coins:
        if i-c == 0:
            update_memo = [set([c])]
        elif i-c > 0:
            print(memo[i-c])
            update_memo = [{*m, c} for m in memo[i-c]]
        else:
            continue
        memo[i] += update_memo
        print(memo[i])
print(len({frozenset(s) for s in memo[k+1]}))

