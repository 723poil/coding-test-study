from sys import stdin

table = dict()
table_seat = dict()

def set_t(t: int, x: int, L: int):
    return x - t if x >= t else L + x - t

def chief_command(t: int, x: int, name: str, L: int):
    global table

    new_x = set_t(t, x, L)

    if table.get(new_x) and table[new_x].get(name):
        table[new_x][name] += 1
    elif not table.get(x-t):
        table[new_x] = {name: 1}
    else:
        table[new_x][name] = 1

def customer_command(x: int, name: str, n: int, L: int):
    global table_seat


    table_seat[x] = {name: n}

def cheese():
    global table, table_seat

    count_c = 0
    count_s = 0

    for table_key in table.keys():
        for name_key in table[table_key].keys():
            count_s += table[table_key][name_key]

    for seat_key in table_seat.keys():
        for cus_key in table_seat[seat_key].keys():
            if table_seat[seat_key][cus_key] > 0:
                count_c += 1
    return count_c, count_s

def eat_sushi(gap_t: int, real_t: int, L: int):
    global table, table_seat

    # 시간차가 클때 for문 돌지말고 바로 넘기는 로직 추가해야함

    for gt in range(real_t - gap_t + 1, real_t+1):
        mt = gt % L

        # 1. 테이블 자리별로 스시 확인
        for table_key in table.keys():
            mmt = (mt + table_key) % L
            for name_key in table[table_key].keys():
                # 2. 해당 스시에 적힌 이름이 현재 자리에 앉아있는지 확인
                if table[table_key][name_key] > 0 and table_seat.get(mmt) and table_seat[mmt].get(name_key) and table_seat[mmt][name_key] > 0:
                    can_eat = min(table_seat[mmt][name_key], table[table_key][name_key])

                    # 3. 있으면 먹이고, 0이 되면 손님 나가기
                    table_seat[mmt][name_key] -= can_eat
                    table[table_key][name_key] -= can_eat

                    


def solution():
    L, Q = map(int, input().split())
    before_t = 0

    for _ in range(Q):
        commands = list(map(str, input().rstrip().split()))

        command, t = [int(commands[0]), int(commands[1])]

        gap_t = t - before_t
        before_t = t
        t = t % L

        # 사장 초밥 만들기
        # 회전이 일어난 직후
        # 시각 t, x 위치에 name 이름을 부착한 초밥을 올려놓는다. (같은 위치에 여러개 올라갈 수 있음)
        if command == 100:
            x = int(commands[2])
            name = commands[3]
            chief_command(t, x, name, L)
            eat_sushi(gap_t, before_t, L)

        # 손님 입장
        # 회전이 일어난 직후
        # 시간 t, x위치에 name이 앉는다.
        # x 앞으로 오는 초밥 중 자신의 초밥 정확히 n개 먹고 떠남
        elif command == 200:
            x = int(commands[2])
            name = commands[3]
            n = int(commands[4])
            customer_command(x, name, n, L)
            eat_sushi(gap_t, before_t, L)
        # 사진 촬영
        # 시각 t 사진 촬영
        # 1. 초밥 회전이 일어난 뒤
        # 2. 손님이 자신의 초밥이 있으면 먹은 뒤
        else:
            eat_sushi(gap_t, before_t, L)
            c, s = cheese()
            print(c, s)

solution()