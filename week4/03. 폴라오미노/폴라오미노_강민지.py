"""
index를 늘려가면서 A, B 순서대로 덮을 수 있는지 확인
B로 A를 만들 수 있어서 greedy로 풀 수 있음
만약 A를 B로 만들 수 없다면 greedy로 풀 수 없음. 다양한 경우의 수를 따져야 함(탐색 문제).
"""

def main(board):
    i = 0
    while i < len(board):

        if board[i] == "X":
            if board[i:i+4] == "XXXX":
                board = board[:i] + "AAAA" + board[i+4:]
            elif board[i:i+2] == "XX":
                board = board[:i] + "BB" + board[i+2:]
            else:
                return -1   
        i += 1
    return board

board = input()
print(main(board))