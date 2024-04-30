from sys import stdin

input = stdin.readline

def dfs(l: list, idx: int):
    global result
    
    if l and sum(l) == S:
        result += 1
    
    for i in range(idx, N):
        l.append(ss[i])
        dfs(l, i+1)
        l.pop()

if __name__ == '__main__':
    N, S = map(int, input().split())
    
    ss = list(map(int, input().split()))
    
    result = 0
    
    dfs([], 0)
    
    print(result)