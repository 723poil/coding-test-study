from sys import stdin

input = stdin.readline

x = [0, 1, 0, -1]
y = [1, 0, -1, 0]

def bfs(cabbages: dict):
    
    count = 0
    
    while cabbages:
        count += 1
        cur_cabbage = list(cabbages.keys())[0]
        qq = [cur_cabbage]
        del cabbages[cur_cabbage]
        
        while qq:
            cc = qq.pop(0)
            
            for i in range(4):
                cur_m = cc[1] + x[i]
                cur_n = cc[0] + y[i]
                if cabbages.get((cur_n, cur_m)):
                    qq.append((cur_n, cur_m))
                    del cabbages[(cur_n, cur_m)]
                    
    return count
        

def solution():
    M, N, K = map(int, input().split())
    
    cabbages = dict()
    
    for _ in range(K):
        m, n = map(int, input().split())
        
        cabbages[(n, m)] = True
        
    return bfs(cabbages)


T = int(input())

for _ in range(T):
    print(solution())