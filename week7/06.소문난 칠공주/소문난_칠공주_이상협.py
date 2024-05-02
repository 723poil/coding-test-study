from sys import stdin
from collections import deque

input = stdin.readline

def check_7() -> bool:
    global dx, dy, visited, seven
    
    init()
    
    q = deque()
    q.append([seven[0][0], seven[0][1]])
    
    for p in seven:
        visited[p[0]][p[1]] = True
    
    visited[seven[0][0]][seven[0][1]] = False
    
    count = 1
    while q:
        row, col = q.popleft()
        
        for i in range(4):
            xx = col + dx[i]
            yy = row + dy[i]
            
            if not (0 <= xx < 5 and 0 <= yy < 5):
                continue
            
            if not visited[yy][xx]:
                continue
            
            visited[yy][xx] = False
            q.append([yy, xx])
            count += 1
    
    if count == 7:
        return True
    
    return False
    

def find_7(count: int, y_c: int, cur: int):
    global students, result, visited, dx, dy, seven
    
    if count == 7:
        if check_7():
            result += 1
        return
    
    for i in range(cur, 25):
        new_y_c = y_c
        
        row = i // 5
        col = i % 5
        
        if students[row][col] == 'Y':
            new_y_c += 1
        
        if new_y_c > 3:
            continue
        
        seven.append([row, col])
        find_7(count + 1, new_y_c, i + 1)
        seven.pop()

def init():
    global visited
    
    for y in range(5):
        for x in range(5):
            visited[y][x] = False
    

if __name__ == '__main__':
    students = [list(str(input().rstrip())) for _ in range(5)]
    result = 0
    visited = [[False for _ in range(5)] for _ in range(5)]
    seven = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    find_7(0, 0, 0)
            
    print(result)