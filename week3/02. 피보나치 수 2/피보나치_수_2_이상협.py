from sys import stdin

input = stdin.readline

def solution():
    
    N = int(input())
    
    n_list = [0, 1]
    
    if N <= 1:
        return n_list[N]
    
    for i in range(2, N+1):
        n_list.append(n_list[i-2] + n_list[i-1])
        
    return n_list[N]
    

print(solution())