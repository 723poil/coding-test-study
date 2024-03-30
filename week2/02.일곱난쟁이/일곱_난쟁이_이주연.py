import sys
from itertools import combinations, permutations
input = sys.stdin.readline

# 9개중에 7개의 합이 100이 되는 경우의 수를 구해라
# 조합으로 7개 뽑고 100이 되면 그걸 출력한다. 오름차순으로
lst = []
for i in range(9):
    lst.append(int(input()))

lst.sort()
for it in combinations(lst, 7):
    if sum(it) == 100:
        t = list(it)
        t.sort()
        for s in t:
            print(s)
        break
