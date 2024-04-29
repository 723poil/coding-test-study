from sys import stdin

input = stdin.readline

x = [0, 1, 0, -1]
y = [1, 0, -1, 0]

def find_like_student(likes: list) -> list:
    
    result = dict()

    for st in likes:
        if not students.get(st):
            continue
        
        like_pos = students[st]
        
        for i in range(4):
            r = like_pos[0] + y[i]
            c = like_pos[1] + x[i]
            
            if not (0 < r <= N and 0 < c <= N):
                continue
            
            if empty_board[r][c] == -1:
                continue
            
            if not result.get((r, c)):
                result[(r, c)] = [1, empty_board[r][c]]
            else:
                result[(r, c)][0] += 1
            
    return result
    
def find_many_closest(closes: list) -> list:
    if not closes:
        # 가장 많이 인접한 칸 가져오기
        max_e = 0
        result = []
        
        for r in range(1, N+1):
            for c in range(1, N+1):
                if empty_board[r][c] > max_e:
                    max_e = empty_board[r][c]
                    
        for r in range(1, N+1):
            for c in range(1, N+1):
                if empty_board[r][c] == max_e:
                    result.append([r, c])
                    
        return result
        
    closes.sort(key=lambda x: (-x[1][0], -x[1][1]))

    return [[item[0][0], item[0][1]] for item in list(filter(lambda x: x[1][0] == closes[0][1][0] and x[1][1] == closes[0][1][1], closes))]
    

if __name__ == '__main__':
    
    N = int(input())
    
    empty_board = [[0 for _ in range(N+1)] for _ in range(N+1)]
    board = [[0 for _ in range(N+1)] for _ in range(N+1)]
    students = dict()
    students_likes = dict()
    
    for r in range(1, N+1):
        for c in range(1, N+1):
            if (r == 1 or r == N) and (c == 1 or c == N):
                empty_board[r][c] = 2
            elif (r == 1 or r == N) or (c == 1 or c == N):
                empty_board[r][c] = 3
            else:
                empty_board[r][c] = 4
    
    for i in range(N ** 2):
        n_list = list(map(int, input().split()))
        
        # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
        first = find_like_student(n_list[1:])
            
        # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
        second = find_many_closest(list(first.items()))
        
        # 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
        third = sorted(second, key= lambda x: (x[0], x[1]))
        
        fr = third[0][0]
        fc = third[0][1]
        
        empty_board[fr][fc] = -1
        students[n_list[0]] = [fr, fc]
        students_likes[n_list[0]] = n_list[1:]
        board[fr][fc] = n_list[0]
        
        for i in range(4):
            r = fr + y[i]
            c = fc + x[i]
            
            if not (0 < r <= N and 0 < c <= N):
                continue
            
            empty_board[r][c] = empty_board[r][c] - 1 if empty_board[r][c] > 0 else empty_board[r][c]
            
    result = 0
            
    for b in board[1:]:
        for bb in b[1:]:
            
            likes_temp = students_likes[bb]
            count = 0
            
            for i in range(4):
                r = students[bb][0] + y[i]
                c = students[bb][1] + x[i]
                
                if not (0 < r <= N and 0 < c <= N):
                    continue
                
                if board[r][c] in likes_temp:
                    count += 1
                    
            result += (10 ** (count - 1)) if count != 0 else 0
            
    print(result)