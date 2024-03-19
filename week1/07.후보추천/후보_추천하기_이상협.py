from sys import stdin

input = stdin.readline

def find_min(result, R_N):
    
    m = min(R_N)
    
    for rst in result:
        if R_N[rst] == m:
            R_N[rst] = 1001
            return rst

def solution():
    N = int(input())
    S = int(input())
    
    R = list(map(int, input().split()))
    R_N = [1001 for _ in range(101)]
    
    result = []
    
    for r in R:
        if len(result) < N and r not in result:
            result.append(r)
            R_N[r] = 1
        elif r in result:
            R_N[r] += 1
        else:
            remove_v = find_min(result, R_N)
            
            result.remove(remove_v)
            result.append(r)
            R_N[r] = 1
            
    return sorted(result, key= lambda x: x)

result = solution()

print(" ".join(map(str, result)))