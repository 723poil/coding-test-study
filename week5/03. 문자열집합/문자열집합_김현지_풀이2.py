# 시간 초과
N, M = map(int, input().split())
# S = list()
S = set()
cnt = 0

for _ in range(N):
    # S.append(input())
    S.add(input())

for _ in range(M):
    compareString = input()
    # for check in S:
    #     if compareString == check:
    #         cnt += 1
    if compareString in S:
        cnt += 1

print(cnt)
