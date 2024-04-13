"""
* 루돌프 이동
1-1) 충돌 X => 끝
1-2) 충돌 O => 산타 이동 
    밀려나기, 상호작용, 기절상태 업데이트(루돌프 충돌)
"""
INF = int(1e5)

def get_dist(coord1, coord2):
    """두 좌표 사이의 거리 구하기"""
    coord = coord1 - coord2
    dist = coord[0]**2 + coord[1]**2
    return dist


def find_closest_santa(r_coord, santa_loc, santa_break):
    """
    :input: 정렬된 santa_loc
    """

    min_dist = INF
    closest_santa = 0

    for s, s_coord in santa_loc.items():
        # 밀려난 산타 => pass 
        if s_coord[0] == 0:
            continue
        # 기절한 산타 = > pass
        elif santa_break[s] == 1:
            santa_break[0] == 0
        else:
            dist = get_dist(s_coord, r_coord)
            if dist < min_dist:
                closest_santa = s
    return closest_santa


n, m, p, c, d = map(int, input().split())
r_r, r_c = map(int, input().split())
r_coord = (r_r, r_c)


santa_break = [0 for _ in range(p+1)] # 기절 상태
santa_score = [0 for _ in range(p+1)] # 점수

santa_loc = {i: (0, 0) for i in range(1, p+1)} # 위치 (밀려나면 (0, 0)) 
for _ in range(p):
    s, s_r, s_c = map(int, input().split())
    santa_loc[s] = (s_r, s_c)
## 정렬 : 거리가 같을 때, 앞 쪽에 있는 산타 선택할 수 있게 정렬
santa_loc = {k: v for k, v in sorted(santa_loc.items(), key=lambda x: (-x[1][0], -x[1][1]))} 


print(santa_loc)
print(f"closest_santa: {find_closest_santa(r_coord, santa_loc, santa_break)}")