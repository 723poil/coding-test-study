N, M = map(int, input().split())
bulbs = list(map(int, input().split()))

for _ in range(M):
    command, left, right = map(int, input().split())
    if command == 1:
        bulbs[left-1] = right
    elif command == 2:
        for i in range(left-1, right):
            if bulbs[i] == 0:
                bulbs[i] = 1
            else:
                bulbs[i] = 0
    elif command == 3:
        bulbs[left-1 :right] = [0] * (right-(left-1))
    elif command == 4:
        bulbs[left-1 :right] = [1] * (right-(left-1))

print(" ".join(map(str, bulbs)))
