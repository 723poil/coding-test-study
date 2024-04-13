def solution(board, boardSize):
    cnt = 0
    for i in range(boardSize):
        if cnt == 4:
            board[i-4:i] = ['A', 'A', 'A', 'A']
            cnt = 0
        if cnt == 2:
            board[i-2:i] = ['B', 'B']
        if board[i] == '.':
            cnt = 0
            continue
        cnt += 1

def isCoverable(board, boardSize):
    for i in range(boardSize):
        if board[i] == 'X':
            return False
    return True


board = list(input()) + ['L']
boardSize = len(board)
solution(board, boardSize)
coverable = isCoverable(board, boardSize)
if coverable:
    print("".join(board[:-1]))
else:
    print(-1)
