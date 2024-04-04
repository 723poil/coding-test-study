from sys import stdin

input = stdin.readline

def solution():
    N = int(input())
    
    if N % 5 == 0:
        return N // 5
    
    max_5 = N // 5
    
    while max_5 >= 0:
        remain = N - (max_5 * 5)
        
        if remain % 3 == 0:
            return max_5 + (remain // 3)
        
        max_5 -= 1
    
    return -1

print(solution())