from sys import stdin

input = stdin.readline

def dfs(cur_v: int, adj: dict, searched: list):
    
    if searched[cur_v]:
        return
    
    result = [cur_v]
    searched[cur_v] = True
    
    for adj_n in adj[cur_v]:
        if not searched[adj_n]:
            sub_result = dfs(adj_n, adj, searched)
            if sub_result:
                result += sub_result
                
    return result

def bfs(cur_v: int, adj: dict, searched: list):
    
    qq = [cur_v]
    searched[cur_v] = True
    result = []
    
    while qq:
        cv = qq.pop(0)
        result.append(cv)
        
        for adv in adj[cv]:
            if not searched[adv]:
                qq.append(adv)
                searched[adv] = True
                
    return result

def solution():
    N, M, V = map(int, input().split())
    
    dfs_searched = [False for _ in range(N+1)]
    bfs_searched = [False for _ in range(N+1)]
    
    
    adj = dict()
    
    for _ in range(M):
        n1, n2 = map(int, input().split())
        
        if adj.get(n1):
            adj[n1].append(n2)
        else:
            adj[n1] = [n2]
            
        if adj.get(n2):
            adj[n2].append(n1)
        else:
            adj[n2] = [n1]
            
    if not adj.get(V):
        return [V], [V]
            
    for n in adj.keys():
        adj[n].sort()
        
    dfs_result = dfs(V, adj, dfs_searched)
    bfs_result = bfs(V, adj, bfs_searched)
    
    return dfs_result, bfs_result

dfs_r, bfs_r = solution()

print(" ".join(map(str, dfs_r)))
print(" ".join(map(str, bfs_r)))