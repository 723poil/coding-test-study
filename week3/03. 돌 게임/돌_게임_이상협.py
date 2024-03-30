from sys import stdin

input = stdin.readline

def solution():
    
    N = int(input())
    
    return 'SK' if N % 2 == 1 else 'CY'

print(solution())