import sys
from math import sqrt

input = sys.stdin.readline

move_y = [1, 0, -1, 0]
move_x = [0, 1, 0, -1]

def find_move_dir(cur, min_c, can_move):
    diff = cur - min_c
    return (diff-1) // can_move
    
    

def insert_num(count, layer, pos, snail, find_num):
    
    can_move = layer * 2
    min_count = count
    max_count = ((layer * 2) + 1) ** 2
    
    find_pos = [0, 0]
    
    for cur in range(count+1, max_count+1):
        if cur == count+1:
            pos[0] -= 1
        else:    
            dir = find_move_dir(cur, min_count, can_move)
            
            pos[0] += move_x[dir]
            pos[1] += move_y[dir]
            
        snail[pos[0]][pos[1]] = cur
        
        if cur == find_num:
            find_pos = [pos[0], pos[1]]
        
    return [find_pos, max_count, pos]
        

def solution():
    N = int(input())
    find_num = int(input())
    
    snail = [[0 for _ in range(N+1)] for _ in range(N+1)]
    center = N // 2 + 1
    
    snail[center][center] = 1
    pos = [center, center]
    cur_layer = 1
    
    result_pos = [0, 0]
    if find_num == 1:
        result_pos = [center, center]
    
    count = 1
    while count < N ** 2:
        find_pos, count, pos = insert_num(count, cur_layer, pos, snail, find_num)
        
        cur_layer += 1
        
        if find_pos[0] != 0:
            result_pos = find_pos
        
    return snail, result_pos
    
snail, pos = solution()

for i in range(1, len(snail)):
    print(" ".join(map(str, snail[i][1:])))
print(" ".join(map(str, pos)))