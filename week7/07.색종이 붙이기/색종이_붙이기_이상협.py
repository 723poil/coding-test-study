from sys import stdin

input = stdin.readline

def check(row: int, col: int, dis: int) -> bool:
    for r in range(row, row + dis):
        for c in range(col, col + dis):
            if board[r][c] == 0:
                return False
            
    return True

def use_board(row: int, col: int, dis: int, is_use: bool):
    
    value = 0 if is_use else 1
    
    for r in range(row, row + dis):
        for c in range(col, col + dis):
            board[r][c] = value
            
    able_count[dis] = able_count[dis] - 1 if is_use else able_count[dis] + 1

def dfs(row: int, col: int, cnt: int):
    global count
    
    if col == 10:
        row += 1
        col = 0
        
    if row == 10:
        count = min(count, cnt)
        return
    
    if board[row][col] == 0:
        dfs(row, col + 1, cnt)
        return
    
    for i in range(1, 6):
        if able_count[i] <= 0:
            continue
        
        if row + i > 10 or col + i > 10:
            continue
        
        if not check(row, col, i):
            continue
        
        use_board(row, col, i, True)
        dfs(row, col + 1, cnt + 1,)
        use_board(row, col, i, False)
        
        

if __name__ == '__main__':
    able_count = [5] * 6
    
    board = [list(map(int, input().split())) for _ in range(10)]
    count = int(1e9)
    
    dfs(0, 0, 0)
    
    print(count if count != int(1e9) else -1)