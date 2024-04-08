"""
- memo : 해당 위치에 있는 node까지의 최대 상자 수
    > j번째 node의 최대 상자 수 = 이전 node들의 최대 상자수와 관련 있음
    => 주어진 조건을 만족하는 경우, i번째 node의 최대 상자수 + 1 저장
    => 주어진 조건을 만족하지 않는 경우, pass
"""

n = int(input())
box_list = list(map(int, input().split()))
memo = [1] * n

for i in range(n):
    for j in range(i):
        if box_list[j] < box_list[i]:
            memo[i] = max(memo[i], memo[j]+1)

print(max(memo))