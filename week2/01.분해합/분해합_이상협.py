from sys import stdin

input = stdin.readline

def divideSum(n: int):
    
    i = 1
    result = n
    
    while i <= n:
        m = n // i

        result += m % 10
        
        i *= 10
        
    return result

def solution():
    N = int(input())
    
    for i in range(1, N):
        s = divideSum(i)
        
        if s == N:
            return i
        
    return 0
                
print(solution())