from sys import stdin

input = stdin.readline

def count_worm(graph: dict, searched: list):
    wc = 0
    
    qq = [1]
    searched[0] = True
    
    while qq:
        node = qq.pop(0)
        wc += 1
        
        nl = graph[node]
        
        for n in nl:
            if not searched[n-1]:
                qq.append(n)
                searched[n-1] = True
                
    return wc - 1

def solution():
    cn = int(input())
    cr = int(input())
    
    if cn == 1:
        return 0
    
    graph = dict()
    searched = [False for _ in range(cn)]
    
    for _ in range(cr):
        c1, c2 = map(int, input().split())
        
        if graph.get(c1):
            graph[c1].append(c2)
        else:
            graph[c1] = [c2]
            
        if graph.get(c2):
            graph[c2].append(c1)
        else:
            graph[c2] = [c1]
            
    return count_worm(graph, searched)
    
print(solution())