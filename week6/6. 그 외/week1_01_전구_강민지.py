def order1(lights, i, x):
    lights[i] = x
    return lights

def order2(lights, l, r):
    for i in range(l, r+1):
        lights[i] = 0 if lights[i] else 1
    return lights

def order3(lights, l, r):
    lights[l:r+1] = [0] * (r+1-l)
    return lights

def order4(lights, l, r):
    lights[l:r+1] = [1] * (r+1-l)
    return lights

def order(lights, a, b, c):
    if a == 1:
        return order1(lights, b, c)
    elif a == 2:
        return order2(lights, b, c)
    elif a == 3:
        return order3(lights, b, c)
    elif a == 4:
        return order4(lights, b, c)
    else:
        return lights

n, m = map(int, input().split())
lights = [0] + list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    lights = order(lights, a, b, c)

print(' '.join(map(str, lights[1:])))