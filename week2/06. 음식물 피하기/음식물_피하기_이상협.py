from sys import stdin

input = stdin.readline

x = [0, 1, 0, -1]
y = [1, 0, -1, 0]

def find_big(trashes: dict):
    count = -1
    
    while trashes:
        
        tc = 0
        cur_v = list(trashes.keys())[0]
        
        qq = [cur_v]
        del trashes[cur_v]
        
        while qq:
            cc = qq.pop(0)
            tc += 1
            
            for i in range(4):
                cur_x = cc[1] + x[i]
                cur_y = cc[0] + y[i]
                
                if trashes.get((cur_y, cur_x)):
                    qq.append((cur_y, cur_x))
                    del trashes[(cur_y, cur_x)]
        
        count = max(count, tc)
        
    return count

def solution():
    N, M, K = map(int, input().split())
    
    trashes = dict()
    
    for _ in range(K):
        n, m = map(int, input().split())
        
        trashes[(n, m)] = True
    
    return find_big(trashes)

print(solution())