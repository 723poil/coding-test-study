from sys import stdin

input = stdin.readline

s_like = {}

x = [1, 0, -1, 0]
y = [0, 1, 0, -1]
                    
def find_like_student(me: int):
    global s_like
    
    likes = []

    for like in s_like[me][1]:
        if s_like.get(like) and s_like[like][0] != 0:
            likes.append(like)
            
    return likes

def find_empty_seat(seats: list):
    
    n = len(seats)
    max_able = 0
    
    for row in seats[1:]:
        for col in row[1:]:
            max_able = max(max_able, col[1])
    
    for row in range(1, n):
        for col in range(1, n):
            if seats[row][col][1] == max_able and seats[row][col][0] == 0:
                return [(row, col)]

def find_like_student_adj(like_students:list, seats: list):
    global s_like
    
    n = len(seats) - 2
    likes = {}
    
    for like in like_students:
        r, c = s_like[like][0]
        
        for i in range(4):
            if 1 <= r + x[i] <= n and 1 <= c + y[i] <= n:
                
                if seats[r + x[i]][c + y[i]][0] == 0:
                    n_r = r + x[i]
                    n_c = c + y[i]
                    if likes.get((n_r, n_c)):
                        likes[(n_r, n_c)] += 1
                    else:
                        likes[(n_r, n_c)] = 1
                        
    likes_keys = sorted(likes.keys(), key=lambda x: -likes[x])
    likes_items = sorted(likes.items(), key=lambda x: -x[1])
    
    for i in range(len(likes_keys)):
        if likes_items[i][1] != likes_items[0][1]:
            return likes_keys[:i]
        
    return likes_keys
        

def find_max_empty_seats(able_seats:list, seats: list):
    
    max_s = seats[able_seats[0][0]][able_seats[0][1]][1]
    likes = [able_seats[0]]
    
    for able in able_seats[1:]:
        r = able[0]
        c = able[1]
        
        if max_s == seats[r][c][1]:
            likes.append(able)
        elif max_s < seats[r][c][1]:
            likes = [able]
            max_s = seats[r][c][1]
            
    return likes

def find_min_row_seats(able_seats:list):
    
    able_seats.sort(key= lambda x: x[0])
    
    for i in range(len(able_seats)):
        if able_seats[i][0] != able_seats[0][0]:
            return able_seats[:i]
        
    return able_seats

def find_min_col_seats(able_seats:list):
    
    able_seats.sort(key= lambda x: x[1])
    
    return [able_seats[0]]

def calc_score(me: int):
    global s_like
    
    r, c = s_like[me][0]
    
    count = 0
    
    for like in s_like[me][1]:
        n_r, n_c = s_like[like][0]
        
        if abs(n_r - r) + abs(n_c - c) == 1:
            count += 1
            
    if count == 0:
        return 0
    if count == 1:
        return 1
    if count == 2:
        return 10
    if count == 3:
        return 100
    return 1000

def solution():
    global s_like

    N = int(input()) 
    
    seats = [[[0, 0] for _ in range(N+2)] for _ in range(N+2)]
    
    score = 0
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if (i == 1 and j == 1) or (i == N and j == N) or (i == 1 and j == N) or (i == N and j == 1):
                seats[i][j][1] = 2
            elif i == 1 or i == N or j == 1 or j == N:
                seats[i][j][1] = 3
            else:
                seats[i][j][1] = 4
    
    for _ in range(N ** 2):
        S = list(map(int, input().split()))
        
        s_like[S[0]] = [(0, 0)] + [S[1:]]

        # 좋아하는 학생이 자리가 선정됐는지 확인
        like_students = find_like_student(S[0])
        
        # 없으면 가장 빨리 찾을수있고 빈곳이 많이 인접한 자리 찾기
        if len(like_students) == 0:
            able_seats = find_empty_seat(seats)
        
        else:
            # 비어있는 칸 중 좋아하는 학생 인접 많이 한 곳 찾기
            able_seats = find_like_student_adj(like_students, seats)
            
            # 여러개면 그 중에 비어있는 칸 많은 곳 선정
            if len(able_seats) > 1:
                able_seats = find_max_empty_seats(able_seats, seats)
                
            # # 여러개면 행 번호 작은 곳 선정
            if len(able_seats) > 1:
                able_seats = find_min_row_seats(able_seats)
                
            # # 여러개면 열 번호 작은 곳 선정
            if len(able_seats) > 1:
                able_seats = find_min_col_seats(able_seats)
                
        if len(able_seats) == 0:
            able_seats = find_empty_seat(seats)
              
        (r, c) = able_seats[0]
        s_like[S[0]][0] = able_seats[0]
        seats[r][c] = [S[0], 0]
        
        for i in range(4):
            seats[r+x[i]][c+y[i]][1] -= 1
        
    for row in seats[1:N+1]:
        for col in row[1:N+1]:
            score += calc_score(col[0])
            
    return score

result = solution()

print(result)