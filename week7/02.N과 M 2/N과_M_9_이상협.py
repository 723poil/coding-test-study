from sys import stdin

input = stdin.readline

def dfs(pos: int, enu: list, s: str):
    
    penu = ",".join(list(map(str, enu)))
    
    if penu in s:
        return
    
    if enu[0] != -1:
        s += penu
        
        if pos != M:
            s += '/'
    
    if pos == M:
        result.add(" ".join([ss.split(',')[1] for ss in s.split("/")]))
        return
    
    for idx, n in enumerate(numbers):
        dfs(pos+1, [idx, n], s)

if __name__ == '__main__':
    N, M = map(int, input().split())
    
    numbers = list(map(int, input().split()))
    numbers.sort()
    
    result = set()
    
    dfs(0, [-1, -1], "")
    
    result = list(result)
    result.sort(key= lambda x: list(map(int, x.split())))
    
    for r in result:
        print("".join(list(map(str, r))))
    