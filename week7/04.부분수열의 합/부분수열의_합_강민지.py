"""
- 틀린 이유 : 연속된 부분 수열일 필요 X
"""

from itertools import combinations

n, S = map(int, input().split())
seq = list(map(int, input().split()))
answer = 0


for i in range(1, n+1):
    comb_list = combinations(seq, i)
    
    for c in comb_list:
        if sum(c) == S:
            answer += 1

print(answer)