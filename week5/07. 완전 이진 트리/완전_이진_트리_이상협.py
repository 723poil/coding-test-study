from sys import stdin

input = stdin.readline

def tree(si: int, ei: int, level: int):
    
    mi = (si + ei) // 2
    
    if not result.get(level):
        result[level] = [buildings[mi]]
    else:
        result[level].append(buildings[mi])
    
    if si == ei:
        return
    
    tree(si, mi-1, level + 1)
    tree(mi+1, ei, level + 1)
    

if __name__ == '__main__':
    K = int(input())
    buildings = list(map(int, input().split()))
    
    result = dict()
    
    tree(0, len(buildings)-1, 0)
    
    for value in result.values():
        for v in value:
            print(v, end=' ')
        print()