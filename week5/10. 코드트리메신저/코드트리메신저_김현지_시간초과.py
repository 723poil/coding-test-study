def countRooms(parents, authority, active, N, target):
    cnt = 0

    for start in range(1, N+1):
        # 자기 자신은 제외
        if start == target:
            continue

        current = start
        steps = 0

        while current != 0 and active[current] and steps <= authority[start]:
            current = parents[current]
            steps += 1
            if current == target and steps <= authority[start]:
                cnt += 1
                break

    return cnt

def main():
    # N: 채팅방의 수, Q: 명령의 수
    N, Q = map(int, input().split())
    commands = list(map(int, input().split()))

    parents = [0] * (N+1)
    authority = [0] * (N+1)
    active = [True] * (N+1)

    for i in range(1, N+1):
        parents[i] = commands[i]

    for i in range(N+1, 2*N+1):
        authority[i-N] = commands[i]

    for _ in range(Q-1):
        commands = list(map(int, input().split()))
        command = commands[0]
        if command == 200:
            c = commands[1]
            active[c] = not active[c]
        elif command == 300:
            c, power = commands[1], commands[2]
            authority[c] = power
        elif command == 400:
            c1, c2 = commands[1], commands[2]
            parents[c1], parents[c2] = parents[c2], parents[c1]
        elif command == 500:
            c = commands[1]
            current = c
            print(countRooms(parents, authority, active, N, c))


if __name__ == "__main__":
    main()
