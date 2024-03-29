import sys
import collections
input = sys.stdin.readline

n = int(input()) # 컴퓨터의 수
m = int(input()) # 컴퓨터 쌍의 수

maps = collections.defaultdict(list)
visit = [False]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    maps[a].append(b) # 방향성이 없는 그래프임으로
    maps[b].append(a)
def bfs(n):
    q = [n]
    cnt = 0
    visit[n]=True
    while q:
        s = q.pop()
        for i in maps[s]:
            if not visit[i]:
                cnt+=1
                q.append(i)
                visit[i]=True
    return cnt

print(bfs(1))