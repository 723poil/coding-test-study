from sys import stdin

input = stdin.readline

A = 'AAAA'
B = 'BB'

def stack(board: list) -> str:
    
    result = ""
    index = 0
    
    while index < len(board):
        temp = board[index: index+4]
        
        # 1. 4개 가능한 경우
        if len(temp) == 4 and '.' not in temp:
            result += A
            index += 4
            continue
        
        # 2. 2개 가능한 경우
        temp = temp[:2]
        if len(temp) == 2 and '.' not in temp:
            result += B
            index += 2
            continue
        
        # add. 1개인데 X인 경우
        if len(temp) == 1 and temp[0] == 'X':
            return -1
        
        # 3. 1개인 경우
        if temp.index('.') == 0:
            result += '.'
            index += 1
        else:
            return -1            

    return result

def solution():    
    board = list(str(input().rstrip()))
    
    return stack(board)

print(solution())