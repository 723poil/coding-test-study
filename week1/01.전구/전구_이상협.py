import sys

input = sys.stdin.readline

def act_1 (i, x, bulbs):
    bulbs[i-1] = x
    
def act_2 (l, r, bulbs):
    for i in range(l-1, r):
        bulbs[i] = 1 if bulbs[i] == 0 else 0
        
def act_3 (l, r, bulbs):
    for i in range(l-1, r):
        bulbs[i] = 0
        
def act_4 (l, r, bulbs):
    for i in range(l-1, r):
        bulbs[i] = 1

def solution():
    
    N, M = map(int, input().split())
    
    bulbs = list(map(int, input().split()))
    
    for _ in range(M):
        a, b, c = map(int, input().split())
        
        if a == 1:
            act_1(b, c, bulbs)
        elif a == 2:
            act_2(b, c, bulbs)
        elif a == 3:
            act_3(b, c, bulbs)
        elif a == 4:
            act_4(b, c, bulbs)
            
    return bulbs

result = solution()

print(" ".join(map(str, result)))