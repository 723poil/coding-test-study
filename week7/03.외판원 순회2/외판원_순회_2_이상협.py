from sys import stdin

input = stdin.readline

def dfs(paths: str, dis: int):
    global result
    
    if len(paths) == N and matrix[int(paths[-1])][int(paths[0])] > 0:
        result = min(result, matrix[int(paths[-1])][int(paths[0])] + dis)
        return
    
    if len(paths) == N:
        return
    
    for i in range(N):
        if str(i) in paths:
            continue
        
        if matrix[int(paths[-1])][i] == 0:
            continue
        
        dfs(paths + str(i), dis + matrix[int(paths[-1])][i])

    

if __name__ == '__main__':
    
    N = int(input())
    
    matrix = []
    result = int(1e9)
    
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    dfs('0', 0)
        
    print(result)