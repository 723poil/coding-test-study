from sys import stdin

input = stdin.readline

def check_num(x, y, arr, n):
    
    chk = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
    
    count = 0
    
    for i, j in chk:
        if 0 <= i < n and 0 <= j < n and arr[j][i] == '*':
            count += 1
            
    return count

def find_num(arr, result_arr, n):
    
    hasBoom = False
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '*':
                if result_arr[i][j] == 0:
                    hasBoom = True
                    
                result_arr[i][j] = '*'
                
            if result_arr[i][j] == '.' or result_arr[i][j] == '*':
                continue
            
            result_arr[i][j] = check_num(j, i, arr, n)
            
    return hasBoom
            

def solution():
    n = int(input())
    
    arr = []
    searched = []
    result_arr = [['.' for _ in range(n)] for _ in range(n)]
    
    for _ in range(n):
        arr.append(list(input().rstrip()))
    
    for _ in range(n):
        searched.append(list(input().rstrip()))
        
        for i in range(n):
            if searched[-1][i] == 'x':
                result_arr[_][i] = 0
        
    hasBoom = find_num(arr, result_arr, n)
    
    if not hasBoom:
        for i in range(n):
            for j in range(n):
                if result_arr[i][j] == '*':
                    result_arr[i][j] = '.'
    
    return result_arr

result = solution()

for row in result:
    print("".join(map(str, row)))