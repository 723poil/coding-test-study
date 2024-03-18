from sys import stdin

customer_seats = dict()
customer_names = set()
customer_times = dict()
customer_eats = dict()

sushi_cnt = 0
customer_cnt = 0

def set_commands(Q: int):
    global customer_seats, customer_names, customer_times, customer_eats

    commands = []
    for _ in range(Q):
        command = list(map(str, input().rstrip().split()))

        cmd = int(command[0])

        if cmd == 100:
            t, x, name = [int(command[1]), int(command[2]), str(command[3])]

            cc = (cmd, t, x, name)
        elif cmd == 200:
            t, x, name, n = [int(command[1]), int(command[2]), str(command[3]), int(command[4])]
            customer_seats[name] = x
            customer_names.add(name)
            customer_times[name] = t
            customer_eats[name] = n

            cc = (cmd, t, x, name, n)
        else:
            t = int(command[1])
            cc = (cmd, t)
    
        commands.append(cc)

    return commands

def solution():
    global customer_seats, customer_names, customer_times, customer_eats, sushi_cnt, customer_cnt

    L, Q = map(int, input().split())
    
    commands = set_commands(Q)
    
    # 초밥 사라지는 시간대 체크
    for command in commands:
        if command[0] != 100:
            continue
        
        t, x, name = [int(command[1]), int(command[2]), str(command[3])]

        # 1. 해당 손님이 들어오는 시간대 파악
        cus_time = customer_times[name]

        # 2. 초밥이 손님보다 먼저 올라와 있을때
        if t < cus_time:
            diff_t = cus_time - t

            expect_sushi_x = (x + diff_t) % L

            able_eat_time = customer_seats[name] - expect_sushi_x
            if expect_sushi_x > customer_seats[name]:
                able_eat_time += L
            able_eat_time += cus_time
        # 2.1 초밥보다 손님이 먼저일때
        else:
            able_eat_time = customer_seats[name] - x
            if x > customer_seats[name]:
                able_eat_time += L
            
            able_eat_time += t

        commands.append((101, able_eat_time, name))

    # t, cmd 정렬
    commands.sort(key= lambda x: (x[1], x[0]))

    for command in commands:
        cmd = command[0]

        if cmd == 100:
            sushi_cnt += 1
        elif cmd == 101:
            sushi_cnt -= 1

            name = command[2]
            customer_eats[name] -= 1
            if customer_eats[name] <= 0:
                customer_cnt -= 1
        elif cmd == 200:
            customer_cnt += 1
        else:
            print(customer_cnt, sushi_cnt)

solution()