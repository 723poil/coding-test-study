from sys import stdin

input = stdin.readline

move_x = [-1, -1, -1, 0]
move_o_x = [1, 1, 1, 0]
move_y = [-1, 0, 1, 1]
move_o_y = [1, 0, -1, -1]

def spin_layer(arr, center, layer):
    
    temp = [arr[center-1+(layer * move_x[0])][center-1+(layer * move_y[0])], arr[center-1+(layer * move_o_x[0])][center-1+(layer * move_o_y[0])]]
    
    for i in range(4):
        next_x = center - 1 + (layer * move_x[(i+1) % 4])
        next_o_x = center - 1 + (layer * move_o_x[(i+1) % 4])
        next_y = center - 1 + (layer * move_y[(i+1) % 4])
        next_o_y = center - 1 + (layer * move_o_y[(i+1) % 4])

        temp_next = [arr[next_x][next_y], arr[next_o_x][next_o_y]]
        
        if i == 3:
            arr[next_x][next_y] = temp[1]
            arr[next_o_x][next_o_y] = temp[0]
        else:
            arr[next_x][next_y] = temp[0]
            arr[next_o_x][next_o_y] = temp[1]
        
        temp = temp_next

def spin_arr(arr, center):
    for layer in range(1, center):
        spin_layer(arr, center, layer)

def solution():
    
    n, d = map(int, input().split())
    
    arr = []
    
    for _ in range(n):
        arr.append(list(map(int, input().split())))
        
    d_c = d // 45 if d > 0 else (360 + d) // 45
    
    if d_c % 8 == 0:
        return arr
    
    for _ in range(d_c):
        spin_arr(arr, (n // 2) + 1)
    
    return arr


T = int(input())

for _ in range(T):
    result = solution()
    
    for row in result:
        print(" ".join(map(str, row)))