from sys import stdin
from collections import deque

input = stdin.readline

def find_min(zirms: dict, D: int):
    keys = sorted(list(zirms.keys()), key= lambda x: (x[0], x[1]))
    
    cur_d = deque() # 현재 위치와 지금까지 운전 거리
    cur_d.append((0, 0))
    for key in keys:
        tmp_l = deque()
        
        for cur in cur_d:
            # 지금 까지 구한 모든 경로에 현재 지름길 적용시켜서 리스트에 추가
            if cur[0] <= key[0]:
                tmp_l.appendleft((key[1], cur[1] + key[0] - cur[0] + zirms[(key[0], key[1])]))
                
        cur_d.extendleft(tmp_l)
        
    # 지름길 적용 후 도착까지 남은 거리 추가
    for i in range(len(cur_d)):
        cur_d[i] = (cur_d[i][0], cur_d[i][1] + D - cur_d[i][0])

    # 정렬해서 제일 낮게 나온 값 리턴
    return sorted(cur_d, key=lambda x: x[1])[0][1]
            
    

def solution():
    N, D = map(int, input().split())
    
    zirms = dict()
    
    for _ in range(N):
        zirm = list(map(int, input().split()))
        
        if zirm[1] > D or (zirm[1] - zirm[0] <= zirm[2]):
            continue
        
        if zirms.get((zirm[0], zirm[1])):
            zirms[(zirm[0], zirm[1])] = min(zirms[(zirm[0], zirm[1])], zirm[2])
        else:
            zirms[(zirm[0], zirm[1])] = zirm[2]
    
    return find_min(zirms, D)
    
print(solution())