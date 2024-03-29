from collections import deque
import collections
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
# 정점 번호가 작은 것부터 먼저 방문한다.
# 방향이 없는 그래프
graph = collections.defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# v 정점부터 방문한 순서를 출력
def dfs(st: int):
    visit = []
    visit_s = []
    stack = [st]
    while stack:
        end = stack.pop()
        if end not in visit:
            visit.append(end)
            visit_s.append(str(end))
            stack.extend(sorted(graph[end], reverse=True)) # 뒤에서 부터 빼는 방식 임으로 4, 3, 2 가 되도록 해야 함
    return ' '.join(visit_s)


def bfs(st: int):
    s_result = str(st)
    visit = [False] * (n + 1)
    visit[st] = True
    q = deque([st])
    while q:
        end = q.popleft()
        for i in sorted(graph[end]):
            if not visit[i]:
                q.append(i)
                s_result += " "
                s_result += str(i)
                visit[i] = True
    return s_result


print(dfs(v))
print(bfs(v))
