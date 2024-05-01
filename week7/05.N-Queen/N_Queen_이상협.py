from sys import stdin

input = stdin.readline

N = int(input())
count = 0

def dfs(row: int):
    global N, count
    
    if row == N:
        count += 1
        return
    
    for i in range(N):
        if cols[i]:
            continue
        
        if p_yx[row + i]:
            continue
        
        if m_yx[N + row - i - 1]:
            continue
        
        cols[i] = True
        p_yx[row + i] = True
        m_yx[N + row - i - 1] = True
        dfs(row + 1)
        cols[i] = False
        p_yx[row + i] = False
        m_yx[N + row - i - 1] = False
    
    
cols = [False] * N
p_yx = [False] * (2 * (N - 1) + 1)
m_yx = [False] * (2 * (N - 1) + 1)

dfs(0)
print(count)