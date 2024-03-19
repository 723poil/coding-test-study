from sys import stdin

input = stdin.readline

x = [0, 1, 0, -1]
y = [1, 0, -1, 0]

def check_dis(r, c, map_rc):
    
    r_len = len(map_rc)
    c_len = len(map_rc[0])
    
    count = 0
    
    for i in range(4):
        valid_index = 0 <= (r+x[i]) < r_len and 0 <= (c+y[i]) < c_len
        
        if not valid_index or map_rc[r+x[i]][c+y[i]] == '.':
            count += 1
    
    if count >= 3:
        return True
    
    return False

def del_map(map_rc):
    
    sr = -1
    er = -1
    
    si = 0
    ei = len(map_rc)-1
    
    while sr == -1 or er == -1:
        if sr == -1 and 'X' in map_rc[si]:
            sr = si
        
        if er == -1 and 'X' in map_rc[ei]:
            er = ei
        
        si += 1
        ei -= 1

    sc = -1
    ec = -1
    
    sj = 0
    ej = len(map_rc[0])-1
    
    while sc == -1 or ec == -1:
        for i in range(len(map_rc)):
            if sc == -1 and map_rc[i][sj] == 'X':
                sc = sj
            
            if ec == -1 and map_rc[i][ej] == 'X':
                ec = ej
                
        sj += 1
        ej -= 1
    
    return [[sr, er], [sc, ec]]
            
    
def solution():
    
    R, C = map(int, input().split())
    
    map_rc = []
    check_arr = []
    
    for _ in range(R):
        map_rc.append(list(map(str, input().strip())))
    
    for r in range(R):
        for c in range(C):
            valid = check_dis(r, c, map_rc)
            
            if valid:
                check_arr.append([r, c])
                
    for row in check_arr:
        map_rc[row[0]][row[1]] = '.'
        
    rr, cc = del_map(map_rc)

    return map_rc[rr[0]:rr[1]+1], cc
    

result, c = solution()

for row in result:
    print("".join(row[c[0]:c[1]+1]))