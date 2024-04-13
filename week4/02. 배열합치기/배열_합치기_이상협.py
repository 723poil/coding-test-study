from sys import stdin

input = stdin.readline

def solution():
    N, M = map(int, input().split())
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    C = A + B
    
    return sorted(C)

result = solution()

for data in result:
    print(data, end=" ")

