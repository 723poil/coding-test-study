from sys import stdin

input = stdin.readline

def dfs(i: int, c: int, s: str):
    
    if str(c) in s:
        return
    
    if c != 0:
        s += str(c)
    
    if i == M:
        print(" ".join(list(s)))
        return
    
    for n in range(1, N+1):
        dfs(i+1, n, s)

if __name__ == '__main__':
    N, M = map(int, input().split())
    
    dfs(0, 0, "")